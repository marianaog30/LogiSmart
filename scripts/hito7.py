"""Adaptador determinista de Maestro: carga reglas desde SKILL.md, sin red."""
import copy
import hashlib
import json
import math
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cargar(nombre, root=ROOT):
    path = root / 'skills' / nombre / 'SKILL.md'
    raw = path.read_bytes()
    bloques = re.findall(r'```json\s*\n(.*?)\n```', raw.decode(), re.S)
    if len(bloques) != 1:
        raise ValueError('Contrato del skill ausente o ambiguo')
    reglas = json.loads(bloques[0])
    if not 1 <= reglas['max_iteraciones'] <= 3 or not 0 < reglas['tiempo_limite_s'] <= 5:
        raise ValueError('Límites de skill inválidos')
    return reglas, {'evento': 'skill_cargado', 'responsable': 'Maestro',
                    'ruta': str(path.relative_to(root)), 'version': reglas['version'],
                    'sha256': hashlib.sha256(raw).hexdigest()}


def canonica(solicitud, reglas):
    if not isinstance(solicitud, dict):
        raise ValueError('Solicitud inválida')
    caso = solicitud.get('caso_id')
    if not isinstance(caso, str) or not re.fullmatch(r'[A-Z0-9-]{1,64}', caso):
        raise ValueError('caso_id inválido')
    if solicitud.get('modo') != 'SIMULADO':
        raise ValueError('Solo modo SIMULADO')
    items = solicitud.get('productos')
    if not isinstance(items, list) or not 1 <= len(items) <= len(reglas['productos']):
        raise ValueError('Lista de productos vacía o fuera de catálogo')
    lineas, vistos = [], set()
    for item in items:
        if not isinstance(item, dict):
            raise ValueError('Línea inválida')
        nombre, cantidad = item.get('producto'), item.get('cantidad')
        if nombre not in reglas['productos'] or nombre in vistos:
            raise ValueError('Producto desconocido o duplicado; solicitar aclaración')
        cat = reglas['productos'][nombre]
        if type(cantidad) is not int or not 1 <= cantidad <= cat['inventario']:
            raise ValueError('Cantidad inválida o superior al inventario ficticio')
        vistos.add(nombre)
        lineas.append({'producto': nombre, 'cantidad': cantidad,
                       'precio_centavos': cat['precio_centavos'],
                       'subtotal_centavos': cantidad * cat['precio_centavos']})
    return {'caso_id': caso, 'modo': 'SIMULADO', 'datos_ficticios': True,
            'fuente': reglas['fuente'], 'moneda': reglas['moneda'], 'lineas': lineas,
            'total_centavos': sum(x['subtotal_centavos'] for x in lineas),
            'estado_final': 'PENDIENTE_APROBACION', 'aprobacion_humana': 'PENDIENTE'}


def calidad(solicitud, propuesta=None, root=ROOT):
    reglas, carga = cargar('logismart-cotizar', root)
    inicio = time.monotonic()
    traza = [carga]
    try:
        esperado = canonica(solicitud, reglas)
    except (ValueError, TypeError) as error:
        return {'estado': 'ACLARACION_REQUERIDA', 'propuesta': None,
                'traza': traza + [{'diagnostico': str(error), 'costo_api_usd': 0}]}
    actual = copy.deepcopy(esperado if propuesta is None else propuesta)
    for n in range(1, reglas['max_iteraciones'] + 1):
        if time.monotonic() - inicio >= reglas['tiempo_limite_s']:
            break
        diferencias = [k for k, v in esperado.items() if actual.get(k) != v]
        traza.append({'caso_id': esperado['caso_id'], 'version_propuesta': 'V' + str(n),
                      'iteracion': n, 'diagnostico': diferencias,
                      'validacion': 'CORRECTA' if not diferencias else 'FALLIDA',
                      'total_centavos': actual.get('total_centavos'), 'costo_api_usd': 0,
                      'costo_adicional_api_usd': 0,
                      'duracion_acumulada_ms': round((time.monotonic() - inicio) * 1000, 3)})
        if not diferencias:
            return {'estado': 'VALIDADA', 'propuesta': actual, 'traza': traza}
        # Una decisión humana declarada en una entrada no se modifica ni se libera.
        if any(k in diferencias for k in ('caso_id', 'estado_final', 'aprobacion_humana', 'modo', 'datos_ficticios')):
            return {'estado': 'DETENIDO_IDENTIDAD_O_DECISION', 'propuesta': None, 'traza': traza}
        # Corrección con fuente: solo derivados del catálogo, nunca la solicitud original.
        for k in diferencias:
            actual[k] = copy.deepcopy(esperado[k])
    return {'estado': 'LIMITE_AGOTADO', 'propuesta': None, 'traza': traza}


def seguridad(propuesta, autorizado, operacion='validar_local', costo_api_usd=0, root=ROOT):
    reglas, carga = cargar('logismart-revisar', root)
    inicio, consumo = time.monotonic(), 0
    traza = [carga]
    actual = copy.deepcopy(propuesta)
    for n in range(1, reglas['max_iteraciones'] + 1):
        if time.monotonic() - inicio >= reglas['tiempo_limite_s']:
            break
        estado = None
        if autorizado is not True:
            estado = 'DETENIDO_PERMISOS'
        elif costo_api_usd is None:
            estado = 'DETENIDO_COSTO_NO_VERIFICABLE'
        elif type(costo_api_usd) not in (int, float) or not math.isfinite(costo_api_usd) or costo_api_usd < 0 or consumo + costo_api_usd > reglas['presupuesto_api_usd']:
            estado = 'DETENIDO_PRESUPUESTO'
        elif operacion not in reglas['operaciones_permitidas']:
            estado = 'DETENIDO_OPERACION'
        elif not isinstance(actual, dict) or actual.get('modo') != 'SIMULADO' or actual.get('datos_ficticios') is not True:
            estado = 'DETENIDO_POLITICA'
        elif actual.get('estado_final') != reglas['estado_requerido'] or actual.get('aprobacion_humana') != reglas['decision_requerida']:
            estado = 'DETENIDO_DECISION_HUMANA'
        if estado:
            return {'estado': estado, 'propuesta': None, 'traza': traza + [
                {'iteracion': n, 'decision': estado, 'operacion_ejecutada': False,
                 'costo_api_usd': consumo}]}
        extras = set(actual) - set(reglas['campos_publicos'])
        lineas = actual.get('lineas')
        if not isinstance(lineas, list) or any(not isinstance(x, dict) for x in lineas):
            return {'estado': 'DETENIDO_FORMATO', 'propuesta': None, 'traza': traza}
        extras_linea = any(set(x) - set(reglas['campos_linea']) for x in lineas)
        consumo += costo_api_usd
        traza.append({'caso_id': actual.get('caso_id'), 'iteracion': n,
                      'decision': 'SANITIZAR_Y_REVISAR' if extras or extras_linea else 'LIBERAR',
                      'campos_extra_eliminados': len(extras), 'lineas_con_extras': extras_linea,
                      'operacion_ejecutada': True, 'costo_api_usd': consumo,
                      'costo_adicional_api_usd': costo_api_usd,
                      'duracion_acumulada_ms': round((time.monotonic() - inicio) * 1000, 3)})
        if extras or extras_linea:
            actual = {k: v for k, v in actual.items() if k in reglas['campos_publicos']}
            actual['lineas'] = [{k: v for k, v in x.items() if k in reglas['campos_linea']} for x in lineas]
            continue
        if time.monotonic() - inicio >= reglas['tiempo_limite_s']:
            break
        return {'estado': 'LIBERADA', 'propuesta': actual, 'traza': traza}
    return {'estado': 'LIMITE_AGOTADO', 'propuesta': None, 'traza': traza}


def precontrol(a, b, caso_id):
    """Usado por GitHub antes del webhook; nunca declara ejecutados los agentes n8n."""
    solicitud = {'caso_id': caso_id, 'modo': 'SIMULADO', 'productos': [
        {'producto': 'Producto A', 'cantidad': a}, {'producto': 'Producto B', 'cantidad': b}]}
    negocio = calidad(solicitud)
    if negocio['estado'] != 'VALIDADA':
        raise ValueError('Precontrol de calidad no superado: ' + negocio['estado'])
    revision = seguridad(negocio['propuesta'], autorizado=True)
    if revision['estado'] != 'LIBERADA':
        raise ValueError('Precontrol de seguridad no superado: ' + revision['estado'])
    return {'calidad': negocio, 'seguridad': revision,
            'limite': 'Costos API n8n no medidos por este precontrol local.'}


def evidencia():
    solicitud = {'caso_id': 'H7-CASO-001', 'modo': 'SIMULADO', 'productos': [
        {'producto': 'Producto A', 'cantidad': 8}, {'producto': 'Producto B', 'cantidad': 30}]}
    reglas, _ = cargar('logismart-cotizar')
    v1 = canonica(solicitud, reglas)
    v1['total_centavos'] = 1  # Fallo deliberado del experimento; no es un resultado real.
    negocio = calidad(solicitud, v1)
    con_extra = dict(negocio['propuesta'], dato_privado_de_prueba='VALOR_NO_PUBLICABLE')
    revision = seguridad(con_extra, True)
    reutilizacion = precontrol(2, 3, 'H7-CASO-002')
    return {'tipo': 'PRUEBAS_DETERMINISTAS_FICTICIAS', 'ejecucion_n8n': False,
            'calidad_v1_v2_mismo_caso': negocio, 'seguridad_sanitizacion': revision,
            'segundo_caso': reutilizacion,
            'sin_permiso': seguridad(negocio['propuesta'], False),
            'costo_desconocido': seguridad(negocio['propuesta'], True, costo_api_usd=None),
            'presupuesto_excedido': seguridad(negocio['propuesta'], True, costo_api_usd=0.01),
            'operacion_prohibida': seguridad(negocio['propuesta'], True, operacion='enviar_telegram'),
            'limite': 'API 0 USD solo para estos loops locales, sin llamadas a proveedores; no incluye infraestructura ni ejecución n8n.'}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--precontrol', nargs=3, metavar=('A', 'B', 'RUN_ID'))
    args = parser.parse_args()
    if args.precontrol:
        a, b, run = args.precontrol
        if not re.fullmatch(r'\d{1,15}', run):
            raise SystemExit('run_id fuera de formato')
        resultado = precontrol(int(a), int(b), 'LOG-9' + run)
        nombre = 'precontrol_actual.json'
    else:
        resultado = evidencia()
        nombre = 'ejecucion.json'
    path = ROOT / 'evidencias' / nombre
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + '\n')
    for r in (resultado.get('calidad', resultado.get('calidad_v1_v2_mismo_caso')), resultado.get('seguridad', resultado.get('seguridad_sanitizacion'))):
        carga = r['traza'][0]
        print(json.dumps({'skill': carga['ruta'], 'version': carga['version'], 'sha256': carga['sha256'], 'resultado': r['estado']}, ensure_ascii=False))
    print('Dos skills cargados desde SKILL.md; loops ejecutados y evidencia sanitizada guardada.')

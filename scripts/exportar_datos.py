"""Exportación pública de LogiSmart; no solicita ni almacena credenciales."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import urllib.request

ENDPOINT = 'https://mariana30.app.n8n.cloud/webhook/logismart-dashboard'
CAMPOS = ('folio_publico', 'fecha_registro', 'productos', 'importe_total', 'moneda',
          'estado_final', 'aprobacion_humana', 'duracion_total_ms', 'origen',
          'completa_primer_intento', 'sin_correcciones_auditoria')
ESTADOS = {'APROBADA', 'RECHAZADA', 'PENDIENTE_APROBACION', 'DETENIDO', 'DEVUELTO',
           'ACLARACION_REQUERIDA', 'ERROR_INCONSISTENTE'}


def fecha(valor):
    if not isinstance(valor, str):
        raise ValueError('Fecha ausente o inválida')
    parsed = datetime.fromisoformat(valor.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('Fecha sin zona horaria')
    return parsed


def sanitizar(datos):
    if not isinstance(datos, dict) or datos.get('datos_ficticios') is not True:
        raise ValueError('La fuente debe declarar datos ficticios')
    fecha(datos.get('consultado_en'))
    filas = datos.get('registros')
    if not isinstance(filas, list) or not filas or datos.get('total_registros') != len(filas):
        raise ValueError('Conteo de registros inconsistente o vacío; se conserva la exportación anterior')
    if datos.get('fuente') != 'Data Table LogiSmart' or datos.get('zona_horaria') != 'America/Mexico_City':
        raise ValueError('Fuente o zona no reconocida')
    excluidos = datos.get('registros_excluidos')
    if type(excluidos) is not int or excluidos < 0:
        raise ValueError('Conteo de exclusiones inválido')
    vistos, salida = set(), []
    for r in filas:
        if not isinstance(r, dict) or any(k not in r for k in CAMPOS):
            raise ValueError('Faltan campos del contrato público')
        folio = r['folio_publico']
        if not isinstance(folio, str) or not re.fullmatch(r'MUESTRA-\d{3,}', folio) or folio in vistos:
            raise ValueError('Folio público inválido o duplicado')
        vistos.add(folio)
        if r['fecha_registro'] is not None:
            fecha(r['fecha_registro'])
        if not isinstance(r['productos'], list) or any(p not in ('Producto A', 'Producto B') for p in r['productos']):
            raise ValueError('Producto fuera de catálogo')
        if r['moneda'] != 'MXN' or r['estado_final'] not in ESTADOS:
            raise ValueError('Moneda o estado inválido')
        for campo in ('importe_total', 'duracion_total_ms'):
            v = r[campo]
            if v is not None and (type(v) not in (int, float) or not 0 <= v < float('inf')):
                raise ValueError('Importe o duración inválido')
        for campo in ('completa_primer_intento', 'sin_correcciones_auditoria'):
            if r[campo] is not None and type(r[campo]) is not bool:
                raise ValueError('Evaluación debe ser booleana o null')
            if r['origen'] != 'DEMO_IMPORTADA_H5' and r[campo] is not None:
                raise ValueError('Evaluación de calidad sin evidencia definida para registros del workflow')
        if r['origen'] not in ('WORKFLOW', 'DEMO_IMPORTADA_H5'):
            raise ValueError('Origen no reconocido')
        decision = r['aprobacion_humana']
        if decision not in ('APROBADA', 'RECHAZADA', 'PENDIENTE', 'NO_SOLICITADA'):
            raise ValueError('Decisión humana no reconocida')
        estado = r['estado_final']
        if (estado in ('APROBADA', 'RECHAZADA') and decision != estado
                or decision in ('APROBADA', 'RECHAZADA') and estado != decision
                or estado == 'PENDIENTE_APROBACION' and decision != 'PENDIENTE'):
            raise ValueError('Estado y decisión humana inconsistentes')
        salida.append({k: r[k] for k in CAMPOS})
    # Lista cerrada también para metadatos; descarta texto libre y propiedades privadas.
    return {'fuente': 'Data Table LogiSmart', 'datos_ficticios': True,
            'consultado_en': datos['consultado_en'], 'zona_horaria': 'America/Mexico_City',
            'total_registros': len(salida), 'registros_excluidos': excluidos, 'registros': salida}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archivo', type=Path, help='JSON local previamente exportado para revisión sin red')
    parser.add_argument('--salida', type=Path, default=Path('web/datos/cotizaciones.json'))
    args = parser.parse_args()
    if args.archivo:
        raw = args.archivo.read_bytes()
    else:
        request = urllib.request.Request(ENDPOINT, headers={'Accept': 'application/json'})
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.headers.get_content_type() != 'application/json':
                raise ValueError('La fuente no devolvió JSON')
            raw = response.read(2_000_001)
    if len(raw) > 2_000_000:
        raise ValueError('La exportación supera el límite de tamaño')
    def invalido(_):
        raise ValueError('Constante numérica JSON inválida')
    publico = sanitizar(json.loads(raw, parse_constant=invalido))
    contenido = json.dumps(publico, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    if re.search(r'sk-[A-Za-z0-9_-]{20,}|\d{8,}:AA[A-Za-z0-9_-]+', contenido):
        raise ValueError('Posible secreto: exportación detenida')
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    temporal = args.salida.with_suffix('.tmp')
    temporal.write_text(contenido)
    temporal.replace(args.salida)
    print(f'Exportación sanitizada: {publico["total_registros"]} registros; consultado_en={publico["consultado_en"]}.')


if __name__ == '__main__':
    main()

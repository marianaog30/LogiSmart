"""Registro reproducible de costos; sin red, credenciales ni generaciones."""
import csv,json,hashlib,importlib.util
from pathlib import Path
from decimal import Decimal as D
P=Path(__file__).resolve().parent
ROOT=P.parent
casos=[]
for file in sorted((P/'evidencias').glob('Caso_0*_real.json')):
 j=json.loads(file.read_text());p=j['presupuesto']
 casos.append(dict(caso_id=j['caso_id'],fecha_utc=j['fecha_utc'],registros=p['registros'],costo_usd=str(p['consumo_usd']),cantidades=j['cantidades'],estado_cierre=j['estado'],fuente=j.get('run_url',j.get('fuente')),version=j.get('version','H8-1.0.0; Telegram con costos'),importe_mxn=j['importe_mxn'],categoria=j.get('categoria','OPERACION')))
assert len({c['caso_id'] for c in casos})==len(casos)
rows=[]
def add(**kw):
 base=dict(fecha_utc='',caso_id='',llamada_id='',etapa='',agente='',proveedor='',modelo_version='',tokens_entrada='',tokens_cache='',tokens_salida='',duracion_voz_segundos='',duracion_sesion_segundos='',unidad_cobro='',tarifa_entrada_usd_millon='',tarifa_cache_usd_millon='',tarifa_salida_usd_millon='',costo_usd='',creditos='',moneda='USD',estado='',reintento='',origen='',fuente='',fecha_tarifa='',precision_fecha='',referencias_llamadas='',nota='')
 base.update(kw);rows.append(base)
names={1:'Alfa',2:'Beta',3:'Gamma',4:'Omega'}
for case in casos:
 total=D(0);refs=[]
 assert {r['agente'] for r in case['registros']}=={1,2,3,4}
 for r in case['registros']:
  i,c,o=[r[k] for k in ['tokens_entrada','tokens_cache','tokens_salida']]
  assert all(type(v) is int and v>=0 for v in [i,c,o]) and c<=i
  assert i+o==r['tokens_total']
  cost=((i-c)*D('.25')+c*D('.025')+o*D('2'))/1000000
  assert cost==D(str(r['costo_usd']));total+=cost
  lid=case['caso_id']+'-L'+str(r['agente']);refs.append(lid)
  add(fecha_utc=case['fecha_utc'],caso_id=case['caso_id'],llamada_id=lid,etapa='Agentes 1 a 4',agente=names[r['agente']],proveedor='OpenAI',modelo_version=r['modelo'],tokens_entrada=i,tokens_cache=c,tokens_salida=o,unidad_cobro='millón tokens',tarifa_entrada_usd_millon='.25',tarifa_cache_usd_millon='.025',tarifa_salida_usd_millon='2',costo_usd=str(cost),estado='COMPLETADO',reintento='0 automáticos; flujo sin reintentos',origen='USAGE_PROVEEDOR_COSTO_CALCULADO',fuente=case['fuente'],fecha_tarifa=r['tarifa_consultada'],precision_fecha='cierre del caso; hora individual no conservada',nota='Costo calculado, no factura. ID de llamada es alias de auditoría, no ID del proveedor.')
 assert total==D(case['costo_usd'])
 case['entrada']=sum(r['tokens_entrada'] for r in case['registros']);case['salida']=sum(r['tokens_salida'] for r in case['registros'])
 for stage,agent in [('Orquestación','Maestro'),('Telegram y n8n','Plataforma'),('Revisión y guardrails','Determinista'),('Publicación y operación','GitHub Actions')]:
  add(fecha_utc=case['fecha_utc'],caso_id=case['caso_id'],etapa=stage,agente=agent,estado='SIN LLM ADICIONAL',unidad_cobro='plataforma; tarifa pendiente',origen='TOKENIZACION_NO_APLICA',fuente=case['fuente'],nota='Tokens no aplican a esta lógica sin LLM. Cargo de plataforma desconocido, no cero.')
 add(fecha_utc=case['fecha_utc'],caso_id=case['caso_id'],etapa='Skills y loops',agente='Maestro',estado='REFERENCIA SIN DOBLE CONTEO',origen='REFERENCIA',referencias_llamadas=';'.join(refs),nota='No se suma otra vez el costo de las llamadas referidas. No implica carga nativa SKILL.md en n8n.')
for row in rows:
 if row['caso_id']=='H10-CASO-05':
  row['nota']='EXPERIMENTO DE DESARROLLO; separar de operación mensual. '+row['nota']
el=json.loads((P/'evidencias/ElevenLabs_texto_medido.json').read_text())
add(caso_id='H10-CASO-02',llamada_id='EL-TEXTO-01-LLM',etapa='ElevenLabs',agente='WALL-E',proveedor='ElevenLabs',modelo_version='No disponible para esta versión histórica',duracion_sesion_segundos=el['duracion_sesion_segundos'],unidad_cobro='LLM por conversación',costo_usd=el['costo_llm_reportado_usd'],estado='CONSULTA TEXTO COMPLETADA',origen='COSTO_REPORTADO_PROVEEDOR',fuente='evidencias/ElevenLabs_texto_medido.json',precision_fecha='2026-11-12 13:01 America/Mexico_City; minuto de UI',nota='8 turnos LLM. Tokens no disponibles. 427 créditos LLM son otra unidad del mismo consumo, no sumar nuevamente.')
add(caso_id='H10-CASO-02',llamada_id='EL-TEXTO-01-PLATAFORMA',etapa='ElevenLabs',agente='WALL-E',proveedor='ElevenLabs',duracion_sesion_segundos=157,unidad_cobro='créditos plataforma',creditos=210,moneda='CREDITOS',estado='CONSUMO REGISTRADO; CONVERSION USD PENDIENTE',origen='CREDITOS_PROVEEDOR',fuente='evidencias/ElevenLabs_texto_medido.json',nota='637 créditos totales = 210 plataforma + 427 LLM. No inferir voz de duración de sesión ni convertir créditos sin plan.')
add(fecha_utc='2026-11-13T03:26:55Z',caso_id='H10-ERROR-01',etapa='Precontrol',agente='Maestro',tokens_entrada=0,tokens_cache=0,tokens_salida=0,unidad_cobro='LLM no invocado',costo_usd='0',estado='ACLARACION_REQUERIDA',reintento=0,origen='PASO_EXTERNO_OMITIDO',fuente='https://github.com/marianaog30/LogiSmart/actions/runs/43359007060',precision_fecha='error de job, precisión a segundo',nota='101 A y 4 B. n8n/LLM omitidos por precontrol fallido; no equivale a cargo de Actions cero.')
add(etapa='Diseño y construcción',agente='Desarrollo',estado='PENDIENTE',origen='NO_DISPONIBLE',nota='Inversión de desarrollo separada: faltan consumo y costos auditables de herramientas usadas.')
with (P/'costos.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(P/'costos_datos.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
llm=sum((D(c['costo_usd']) for c in casos),D(0))
operacion=sum((D(c['costo_usd']) for c in casos if c['categoria']=='OPERACION'),D(0))
patterns={tuple(sorted(c['cantidades'].items())) for c in casos}
summary=dict(casos=casos,ejecuciones_completas=len(casos),casos_con_cantidades_distintas=len(patterns),llamadas_medidas=sum(len(c['registros']) for c in casos),subtotal_openai_usd=str(llm),subtotal_llm_elevenlabs_usd=el['costo_llm_reportado_usd'],subtotal_usd_conocido=str(llm+D(el['costo_llm_reportado_usd'])),costo_integral_usd=None,criterio_tres_casos_distintos=len(patterns)>=3,criterio_voz=False,corte='2026-11-13',filas_costos=len(rows))
summary.update(subtotal_openai_operacion_usd=str(operacion),subtotal_openai_experimento_desarrollo_usd=str(llm-operacion))
(P/'registro_resumen.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
# Auditor independiente TOKENIA: replica valores preservados, no contador nuevo.
skill=dict(currency='USD',date='2026-11-13',calls=[100,1000,10000],rows=[])
for c in casos:
 for r in c['registros']:
  skill['rows'].append(dict(scenario=c['caso_id']+' '+names[r['agente']],model=r['modelo'],evidence='uso_observado',source=c['fuente'],method='usage preservado',price_input='.25',price_cached='.025',price_output='2',input_tokens=r['tokens_entrada'],cached_tokens=r['tokens_cache'],output_tokens=r['tokens_salida']))
(P/'entrada_auditor_tokenia.json').write_text(json.dumps(skill,ensure_ascii=False,indent=2))
print(f'PASS: {len(casos)} ejecuciones, {len(patterns)} combinaciones distintas, {summary["llamadas_medidas"]} llamadas. Subtotal USD conocido {summary["subtotal_usd_conocido"]}; integral pendiente.')

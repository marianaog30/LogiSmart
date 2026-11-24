"""Audita el registro de costos sin red ni credenciales."""
import csv,json
from decimal import Decimal as D
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'costos'
rows=list(csv.DictReader((P/'costos.csv').open(encoding='utf-8-sig')))
required=['agente', 'caso_id', 'costo_usd', 'duracion_voz_segundos', 'estado', 'etapa', 'fecha_tarifa', 'fecha_utc', 'fuente', 'llamada_id', 'modelo_version', 'moneda', 'origen', 'precision_fecha', 'proveedor', 'reintento', 'tarifa_cache_usd_millon', 'tarifa_entrada_usd_millon', 'tarifa_salida_usd_millon', 'tokens_cache', 'tokens_entrada', 'tokens_salida', 'unidad_cobro']
assert rows and set(required)<=set(rows[0]), 'Faltan columnas exigidas por la guía'
ids=[r['llamada_id'] for r in rows if r['llamada_id']]
assert len(ids)==len(set(ids)), 'Alias de llamada duplicado'
total=D(0);agents=0
for r in rows:
 if r['costo_usd']:
  assert r['moneda']=='USD' and D(r['costo_usd'])>=0
  total+=D(r['costo_usd'])
 if r['proveedor']=='OpenAI' and r['tokens_entrada']!='':
  i,c,o=(int(r[k]) for k in ('tokens_entrada','tokens_cache','tokens_salida'))
  assert 0<=c<=i and o>=0
  a,b,d=(D(r[k]) for k in ('tarifa_entrada_usd_millon','tarifa_cache_usd_millon','tarifa_salida_usd_millon'))
  assert ((i-c)*a+c*b+o*d)/1000000==D(r['costo_usd']), 'Costo por llamada inconsistente'
  agents+=1
closure=json.loads((P.parent/'evidencias/cierre/Conciliacion_22.json').read_text())
assert agents==closure['llamadas_conciliadas_csv']
voice24=json.loads((P.parent/'evidencias/cierre/Voz_publica_24.json').read_text())
text24=json.loads((P.parent/'evidencias/interfaz/Texto_y_UTC_24.json').read_text())
assert total==D(closure['subtotal_conocido_usd'])+D(voice24['costos']['llm_usd_reportado'])+D(text24['consumo']['llm_usd_reportado']), 'Subtotal no concilia con evidencia preservada'
for case in closure['casos']:
 selected=[r for r in rows if r['caso_id']==case['caso_id'] and r['proveedor']=='OpenAI' and r['tokens_entrada']]
 assert len(selected)==4 and {r['agente'] for r in selected}=={'Alfa','Beta','Gamma','Omega'}
 assert sum(D(r['costo_usd']) for r in selected)==D(case['costo_ia_usd'])
case=json.loads((P/'Caso_196.json').read_text())
assert {r['agente'] for r in case['presupuesto']['registros']}=={1,2,3,4}
assert sum(D(str(r['costo_usd'])) for r in case['presupuesto']['registros'])==D('.0008019')
voice=json.loads((P/'Voz_exitosa.json').read_text())
assert voice['caso_id']=='MUESTRA-196' and voice['audio_disponible'] is True
assert voice['tokens_entrada'] is None and voice['modelo_llm'] is None
print(f'PASS: {len(rows)} filas; {agents} llamadas reconciliadas; USD conocido {total}; total integral no disponible.')

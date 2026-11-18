"""Audita el registro de costos sin red ni credenciales."""
import csv,json
from decimal import Decimal as D
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'costos'
rows=list(csv.DictReader((P/'costos.csv').open(encoding='utf-8-sig')))
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
assert agents==24
assert total==D('.09140165'), 'Subtotal no concilia con evidencia preservada'
case=json.loads((P/'Caso_196.json').read_text())
assert {r['agente'] for r in case['presupuesto']['registros']}=={1,2,3,4}
assert sum(D(str(r['costo_usd'])) for r in case['presupuesto']['registros'])==D('.0008019')
voice=json.loads((P/'Voz_exitosa.json').read_text())
assert voice['caso_id']=='MUESTRA-196' and voice['audio_disponible'] is True
assert voice['tokens_entrada'] is None and voice['modelo_llm'] is None
print(f'PASS: {len(rows)} filas; 24 llamadas reconciliadas; USD conocido {total}; total integral no disponible.')

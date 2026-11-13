"""Auditoría independiente del registro generado. No llama servicios externos."""
import csv,json
from pathlib import Path
from decimal import Decimal as D

P=Path(__file__).resolve().parent
def check(ok,message):
 if not ok:raise ValueError(message)
def calculate(i,c,o):
 check(all(type(v) is int and v>=0 for v in (i,c,o)), 'Tokens inválidos')
 check(c<=i,'Caché mayor que entrada')
 return ((i-c)*D('.25')+c*D('.025')+o*D('2'))/D(1000000)

for values in [(-1,0,0),(1,2,0),(True,0,0)]:
 try:calculate(*values)
 except ValueError:pass
 else:raise ValueError('No se rechazó una entrada inválida')
check(calculate(1000,1000,300)==D('.000625'),'Doble conteo de caché')
summary=json.loads((P/'registro_resumen.json').read_text())
rows=list(csv.DictReader((P/'costos.csv').open(encoding='utf-8-sig',newline='')))
ids=[r['llamada_id'] for r in rows if r['llamada_id']]
check(len(ids)==len(set(ids)),'ID de llamada duplicado')
subtotal=D(0)
for r in rows:
 if r['proveedor']=='OpenAI':
  expected=calculate(*(int(r[k]) for k in ['tokens_entrada','tokens_cache','tokens_salida']))
  check(expected==D(r['costo_usd']),'Costo OpenAI no coincide')
 if r['costo_usd']!='':
  check(r['moneda']=='USD','Monedas mezcladas')
  subtotal+=D(r['costo_usd'])
check(subtotal==D(summary['subtotal_usd_conocido']),'Subtotal monetario no concilia')
check(summary['costo_integral_usd'] is None,'Costo integral inventado')
check(summary['casos_con_cantidades_distintas']>=3,'Muestra sin tres casos diferentes')
for c in summary['casos']:
 check({x['agente'] for x in c['registros']}=={1,2,3,4},'Falta un agente')
 check(sum(calculate(x['tokens_entrada'],x['tokens_cache'],x['tokens_salida']) for x in c['registros'])==D(c['costo_usd']),'Costo de caso no concilia')
err=json.loads((P/'evidencias/Rechazo_real.json').read_text())
check(err['llamadas_llm']==0 and err['paso_n8n']=='skipped','Rechazo no documentado')
el=json.loads((P/'evidencias/ElevenLabs_texto_medido.json').read_text())
check(el['creditos_totales']==el['creditos_plataforma']+el['creditos_llm'],'Créditos no concilian')
check(el['duracion_voz_segundos'] is None,'Sesión de texto convertida en voz')
cmp=json.loads((P/'evidencias/Comparacion_Gamma.json').read_text())
check(D(cmp['despues_usd'])-D(cmp['antes_usd'])==D(cmp['delta_usd']),'Delta de comparación incorrecto')
check(cmp['qa_antes']==cmp['qa_despues']==10,'Comparación sin calidad equivalente')
for f in (P/'n8n').glob('*.json'):
 workflow=json.loads(f.read_text())
 check(workflow.get('active') is not True,'Exportación activa')
 check(not workflow.get('pinData'),'Datos fijados en exportación')
 check(all(not n.get('credentials') for n in workflow['nodes']),'Credenciales en exportación')
print(f'PASS: {len(rows)} filas; {summary["llamadas_medidas"]} llamadas; USD conocido {subtotal}; integral pendiente; tres casos distintos y rechazo documentados.')

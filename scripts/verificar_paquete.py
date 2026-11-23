"""Comprueba archivos de entrega y referencias locales; no certifica restauración ni servicios externos."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,csv
B=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.paths=[]
 def handle_starttag(self,tag,attrs):
  if tag=='a':
   href=dict(attrs).get('href','');u=urlsplit(href)
   if href and not u.scheme and not u.netloc and u.path:self.paths.append(unquote(u.path))
index=Links();index.feed((B/'ABRIR_PRIMERO.html').read_text())
missing=[p for p in index.paths if not (B/p).is_file()]
assert not missing, f'Enlaces internos inexistentes:{missing}'
files=['LogiSmart_Telegram_ACTUAL.json','LogiSmart_GitHub_ACTUAL.json','LogiSmart_Avisos_ACTUAL.json','LogiSmart_Voz_ACTUAL.json']
workflows=[]
for name in files:
 d=json.loads((B/'n8n'/name).read_text());names=[n['name'] for n in d['nodes']]
 assert len(names)==len(set(names)),name
 known=set(names)
 for src,ports in d['connections'].items():
  assert src in known,(name,src)
  for branch in ports.values():
   for group in branch:
    for edge in group:assert edge['node'] in known,(name,edge)
 assert all(not n.get('credentials') for n in d['nodes']),f'Export con referencia privada de credencial:{name}'
 workflows.append({'archivo':name,'nodos':len(names),'conexiones_validas':True})
required=['web/index.html','web/archivos.html','web/datos/cotizaciones.json','web/datos/muestra_historial.csv','costos/costos.csv','costos/Resumen_por_caso.csv','costos/Resumen_por_etapa.csv','costos/escenarios.csv','costos/Campos_y_completitud.json','tests/pruebas.csv','datos/Mapa_casos_del_corte.json','docs/Recorrido_de_prueba_y_video.md','docs/ElevenLabs_recreacion.md','.env.example','.github/workflows/publicar.yml']
for p in required:assert (B/p).is_file(),p
assert not list(B.rglob('.env')), 'No entregar .env real'
assert not (B/'docs/Informe_tecnico_empresarial.pdf').exists(),'Informe académico debe quedar fuera'
with (B/'tests/pruebas.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
assert {r['ID'] for r in rows}=={f'P{i:02}' for i in range(1,15)}
report={'resultado':'PASS','enlaces_internos_index':len(index.paths),'archivos_esenciales_comprobados':len(required),'workflows_operativos':workflows,'pruebas_ids':len(rows),'alcance':'Verificación estructural local. No demuestra importación completa, credenciales, disponibilidad ni reproducción por otra persona.'}
print(json.dumps(report,ensure_ascii=False))

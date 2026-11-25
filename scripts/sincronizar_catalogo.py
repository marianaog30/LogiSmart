"""CSV maestro -> instantáneas autorizadas. No cambia instancias n8n remotas."""
import argparse,csv,json,re,hashlib
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def cargar():
    path=ROOT/'web/datos/catalogo_productos.csv'
    rows=list(csv.DictReader(path.open(encoding='utf-8-sig',newline='')))
    if len(rows)!=12 or {r['producto_id'] for r in rows}!=set('ABCDEFGHIJKL'):
        raise ValueError('Se requieren exactamente doce productos A-L, sin duplicados')
    products={}
    for r in rows:
        price=Decimal(r['precio_mxn']);stock=int(r['inventario_ficticio'])
        if r['producto']!='Producto '+r['producto_id'] or r['unidad_venta']!='paquete' or r['origen']!='SINTETICO_DEMOSTRACION' or r['version_catalogo']!='2.0':raise ValueError('Contrato del catálogo')
        if price<=0 or price!=price.quantize(Decimal('.01')) or not 0<stock<=9999:raise ValueError('Precio o inventario inválido')
        if r['proveedor_demo'] not in ['Proveedor demo '+s for s in 'ABCD'] or not 1<=len(r['descripcion'])<=160:raise ValueError('Descripción o proveedor no permitido')
        products[r['producto_id'].lower()]={'nombre':r['producto'],'descripcion':r['descripcion'],'precio':float(price) if price%1 else int(price),'inventario':stock,'unidad':'paquete','proveedor_demo':r['proveedor_demo']}
    return {'version':'2.0','vigente_desde':'2026-11-25','fuente':'catalogo_ficticio_logismart_v2','csv_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'moneda':'MXN','datos_ficticios':True,'productos':products}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();c=cargar();j=json.dumps(c,ensure_ascii=False,separators=(',',':'));problems=[]
    def output(path,text):
        path=ROOT/path
        if args.check:
            if path.read_text()!=text:problems.append(str(path.relative_to(ROOT)))
        else:path.write_text(text)
    output('web/datos/catalogo_productos.json',json.dumps(c,ensure_ascii=False,indent=2)+'\n')
    # Comparación semántica; la cabecera legible del archivo JS puede cambiar sin alterar los datos.
    p=ROOT/'web/catalogo.js';s=p.read_text();expected=re.sub(r'const c=.*?;for\(',lambda m:'const c='+json.dumps(c,ensure_ascii=False)+';for(',s,count=1)
    output('web/catalogo.js',expected)
    p=ROOT/'skills/logismart-cotizar/SKILL.md';s=p.read_text();match=re.search(r'```json\n(.*?)\n```',s,re.S);rules=json.loads(match[1]);rules.update(version='2.0.0',fuente=c['fuente'],productos={p['nombre']:{'precio_centavos':int(Decimal(str(p['precio']))*100),'inventario':p['inventario']} for p in c['productos'].values()});updated=s[:match.start(1)]+json.dumps(rules,ensure_ascii=False,separators=(',',':'))+s[match.end(1):];output('skills/logismart-cotizar/SKILL.md',updated)
    for filename in ['LogiSmart_Telegram_ACTUAL.json','LogiSmart_GitHub_ACTUAL.json','LogiSmart_H7_Consumo_Medible.json']:
        path=ROOT/'n8n'/filename;w=json.loads(path.read_text())
        for n in w['nodes']:
            s=n.get('parameters',{}).get('jsCode')
            if not s:continue
            s=re.sub(r'const CATALOGO=.*?;\n',lambda m:'const CATALOGO='+j+';\n',s)
            s=re.sub(r'const catalogo = \{.*?;\n',lambda m:'const catalogo = '+j+';\n',s)
            n['parameters']['jsCode']=s
        output('n8n/'+filename,json.dumps(w,ensure_ascii=False,indent=2)+'\n')
    if problems:raise SystemExit('Desincronizado: '+', '.join(problems))
    print('CATALOGO_2_OK · 12 productos · CSV SHA256 '+c['csv_sha256']+' · '+('verificado sin cambios' if args.check else 'instantáneas generadas; publicar n8n y GitHub por separado'))
if __name__=='__main__':main()

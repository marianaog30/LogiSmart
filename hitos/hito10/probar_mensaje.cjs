const fs=require('fs'),assert=require('assert');
const root=__dirname;
const expr=fs.readFileSync(root+'/mensaje_telegram.txt','utf8');
const render=new Function('$','return '+expr.slice(2,-2));
const hist=JSON.parse(fs.readFileSync(root+'/evidencias/Caso_02_real.json','utf8'));
const r={caso_id:'H10-PRUEBA',estado_final:'PENDIENTE_APROBACION',importe_total:495,moneda:'MXN',unidad_venta:'paquete',detalle_lineas:[{producto:'Producto A',cantidad:2,precio_unitario:120,subtotal:240},{producto:'Producto B',cantidad:3,precio_unitario:85,subtotal:255}],trazas:[],revision_tecnica:{dictamen:'APROBADO_TECNICAMENTE'},presupuesto:hist.presupuesto};
function run(){return render(()=>({first:()=>({json:r})}));}
let s=run();assert(s.includes('USD 0.00173475'));assert(s.includes('2 paquetes'));assert(s.includes('$495.00 MXN'));assert(s.includes('ALCANCE'));assert(s.length<3900);fs.writeFileSync(root+'/evidencias/Mensaje_ejemplo_local.txt',s);
r.presupuesto=undefined;s=run();assert(s.includes('Medición no disponible'));assert(!s.includes('USD 0.00000000'));
r.presupuesto={medicion_directa:true,registros:[{tokens_entrada:4,tokens_cache:9,tokens_salida:1,costo_usd:0,tipo:'USAGE_PROVEEDOR_COSTO_CALCULADO'}]};assert(run().includes('Medición no disponible'));
console.log('PASS: costo conciliado, monedas separadas, paquetes, límite Telegram y datos ausentes/inválidos');

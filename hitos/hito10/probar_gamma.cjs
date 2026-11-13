const fs=require('fs'),assert=require('assert');const root=__dirname;
const OldDate=Date;class Clock extends OldDate{static now(){return OldDate.parse('2026-11-13T00:00:00Z')}}
const state={caso_id:'H10-OPT-01',modo:'SIMULADO',estado_flujo:'OK',_t_inicio:Clock.now(),limite_costo_usd:.1,cotizacion:{lineas:[{producto:'Producto A',cantidad:4,precio_unitario:120,subtotal:480},{producto:'Producto B',cantidad:2,precio_unitario:85,subtotal:170}],subtotal:650,total:650,moneda:'MXN'}};
function run(file){return new Function('$input','Date',fs.readFileSync(root+'/'+file,'utf8'))({first:()=>({json:JSON.parse(JSON.stringify(state))})},Clock)[0].json;}
const a=run('Gamma_v1.js'),b=run('Gamma_v2.js');
assert.deepStrictEqual({...a.request,instructions:null},{...b.request,instructions:null});
assert.deepStrictEqual(a.request.instructions.split('\n\n').slice(1),b.request.instructions.split('\n\n').slice(1));
assert.strictEqual(b.count_request.instructions,b.request.instructions);assert(b.request.instructions.length<a.request.instructions.length);
assert(b.request.instructions.includes('aprobación humana pendiente'));assert(b.request.instructions.includes('SEGURIDAD LOGISMART'));
console.log('PASS: misma entrada, modelo, presupuesto, contrato y catálogo/seguridad; instrucciones compactas también en conteo previo.');

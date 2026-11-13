import fs from 'node:fs/promises';
import vm from 'node:vm';
const root=new URL('../',import.meta.url);
const wf=JSON.parse(await fs.readFile(new URL('n8n/LogiSmart_Ecosistema_Agentes_H8.json',root),'utf8'));
const code=n=>wf.nodes.find(x=>x.name===n).parameters.jsCode;
const resultados=[];
function prueba(n,fn){try{fn();resultados.push({prueba:n,resultado:'PASS'})}catch(e){resultados.push({prueba:n,resultado:'FAIL',motivo:e.message})}}
function ejecutar(src,input,prev={},now=Date.parse('2026-11-12T20:00:00Z')){class Reloj extends Date{static now(){return now}}return new vm.Script('(function(){'+src+'\n})()').runInNewContext({$input:{first:()=>({json:input}),all:()=>[{json:input}]},$:(n)=>({first:()=>({json:prev[n]})}),$execution:{id:'H8-LOCAL'},Date:Reloj});}
function bloquea(fn){let ok=false;try{fn()}catch{ok=true}if(!ok)throw Error('No se bloqueó')}
prueba('usuario no autorizado antes de LLM',()=>bloquea(()=>ejecutar(code('Preparar solicitud telegram'),{update_id:100,message:{from:{id:-1},chat:{id:-1},text:'/nuevo Necesito 2 Producto A'}})));
prueba('evento inválido',()=>bloquea(()=>ejecutar(code('Preparar solicitud telegram'),{})));
const p={_estado:{limite_costo_usd:.1,presupuesto:{consumo_unidades:0}},request:{max_output_tokens:2500}};
const prev={'Preparar llamada 1':p};
prueba('reserva previa',()=>{if(ejecutar(code('Autorizar presupuesto 1'),{input_tokens:100},prev)[0].json.reserva_unidades!==201000)throw Error('Incorrecta')});
prueba('presupuesto insuficiente',()=>bloquea(()=>ejecutar(code('Autorizar presupuesto 1'),{input_tokens:100},{'Preparar llamada 1':{...p,_estado:{limite_costo_usd:.0001,presupuesto:{consumo_unidades:0}}}})));
for(const c of [undefined,0,-1,1.5])prueba('conteo inválido '+String(c),()=>bloquea(()=>ejecutar(code('Autorizar presupuesto 1'),{input_tokens:c},prev)));
prueba('tarifa vencida',()=>bloquea(()=>ejecutar(code('Autorizar presupuesto 1'),{input_tokens:100},prev,Date.parse('2026-11-15T00:00:00Z'))));
const st={modo:'SIMULADO',estado_flujo:'OK',_t_inicio:Date.parse('2026-11-12T20:00:00Z'),caso_id:'LOG-123',solicitud:'Necesito 2 Producto A',usuario:'MARCADOR_PRIVADO',chat_id:'MARCADOR_PRIVADO',limite_costo_usd:.1,presupuesto:{medicion_directa:true,consumo_unidades:0,llamadas_ia_realizadas:0}};
prueba('identidad no enviada al modelo',()=>{if(JSON.stringify(ejecutar(code('Preparar llamada 1'),st)[0].json.request).includes('MARCADOR_PRIVADO'))throw Error('Fuga')});
prueba('máximo cuatro generaciones',()=>bloquea(()=>ejecutar(code('Preparar llamada 1'),{...st,presupuesto:{...st.presupuesto,llamadas_ia_realizadas:4}})));
prueba('tiempo agotado',()=>bloquea(()=>ejecutar(code('Preparar llamada 1'),{...st,_t_inicio:0})));
prueba('destinos HTTP permitidos',()=>{if(wf.nodes.filter(n=>n.type==='n8n-nodes-base.httpRequest').some(n=>!['https://api.openai.com/v1/responses','https://api.openai.com/v1/responses/input_tokens'].includes(n.parameters.url)))throw Error('Destino inesperado')});
const fuente='catalogo_ficticio_logismart_v1';
const qa={caso_id:'LOG-123',modo:'SIMULADO',trazas:[],catalogo:{fuente,productos:{a:{precio:120,inventario:100}}},agente1:{caso_id:'LOG-123',productos:[{nombre:'Producto A',cantidad:2}]},agente2:{caso_id:'LOG-123',fuente},agente3:{caso_id:'LOG-123',total:240,moneda:'MXN',impuestos:0,envio:0,descuentos:0},cotizacion:{caso_id:'LOG-123',lineas:[{producto:'Producto A',cantidad:2,precio_unitario:120,subtotal:240}],total:240,subtotal:240,moneda:'MXN',impuestos:0,envio:0,descuentos:0,fuente}};
function checks(s){return ejecutar(code('Validaciones deterministas QA'),s)[0].json.checks_deterministas;}
prueba('QA válido: diez controles',()=>{const c=checks(structuredClone(qa));if(c.length!==10||c.some(x=>!x.ok))throw Error('Incorrecto')});
for(const [nombre,cambiar,id] of [
 ['precio alterado',s=>s.cotizacion.lineas[0].precio_unitario=121,'precios_vs_catalogo'],
 ['fuente alterada',s=>s.agente2.fuente='NO_AUTORIZADA','fuente_catalogo'],
 ['total alterado',s=>s.cotizacion.total=1,'total']
])prueba(nombre,()=>{const s=structuredClone(qa);cambiar(s);if(checks(s).find(x=>x.id===id)?.ok!==false)throw Error('No detectado')});
await fs.writeFile(new URL('evidencias/Pruebas_nodos_exportados.json',root),JSON.stringify({tipo:'NODOS_EXPORTADOS_SANITIZADOS_CON_ENTRADAS_SINTETICAS',llamadas_api:false,resultados},null,2)+'\n');
if(resultados.some(x=>x.resultado==='FAIL'))throw Error('Falló un control de nodos');
console.log(resultados.length+' pruebas de nodos correctas; no se ejecutaron llamadas HTTP.');

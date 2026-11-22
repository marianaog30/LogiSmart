/* Pruebas de los exports actuales con entradas sintéticas. Nunca llama APIs. */
const fs=require('fs'),vm=require('vm'),assert=require('assert');let checks=0;
for(const flow of ['Telegram','GitHub']){
 const wf=JSON.parse(fs.readFileSync('n8n/LogiSmart_'+flow+'_ACTUAL.json'));
 const code=n=>wf.nodes.find(x=>x.name===n).parameters.jsCode;
 const policy=vm.runInNewContext(code('Preparar llamada 1').split('\n')[0]+';POLICY');
 assert.equal(policy.model,'gpt-4o-mini-2024-07-18');assert.equal(policy.input,6);assert.equal(policy.cached,3);assert.equal(policy.output,24);
 const names=[1,2,3,4].flatMap(i=>['Preparar llamada '+i,'Autorizar presupuesto '+i,'Medir consumo '+i]);
 for(const name of names){
  const src=code(name);new vm.Script('(function(){'+src+'})');checks++;
  if(name!=='Preparar llamada 1')assert(src.startsWith("const POLICY=$('Preparar llamada 1').first().json.tarifas;"));
  const prefix=src.split('const integer=')[0];
  for(const [time,expired] of [['2026-11-21T19:00:00Z',false],['2026-11-29T05:59:59Z',false],['2026-11-29T06:00:00Z',true]]){
   const context={$:()=>({first:()=>({json:{tarifas:policy}})}),Date:{now:()=>Date.parse(time),parse:Date.parse}};
   if(expired)assert.throws(()=>vm.runInNewContext(prefix,context),/TARIFA_VENCIDA/);else vm.runInNewContext(prefix,context);checks++;
  }
  if(name!=='Preparar llamada 1'){
   assert.throws(()=>vm.runInNewContext(prefix,{$:()=>({first:()=>({json:{tarifas:{...policy,vigencia_hasta:'invalida'}}})}),Date}),/TARIFA_INVALIDA/);checks++;
  }
 }
 const src=code('Autorizar presupuesto 1');const p={tarifas:policy,_estado:{limite_costo_usd:.1,presupuesto:{consumo_unidades:0}},request:{max_output_tokens:2500}};
 function reserve(count,limit=.1){const q=structuredClone(p);q._estado.limite_costo_usd=limit;class Clock extends Date{static now(){return Date.parse('2026-11-21T19:00:00Z')}}return vm.runInNewContext('(function(){'+src+'})()',{$:()=>({first:()=>({json:q})}),$input:{first:()=>({json:{input_tokens:count}})},Date:Clock});}
 assert.equal(reserve(100)[0].json.reserva_unidades,60600);checks++;
 assert.throws(()=>reserve(100,.0001),/PRESUPUESTO/);checks++;
 for(const count of [undefined,0,-1,1.5]){assert.throws(()=>reserve(count),/CONTEO/);checks++;}
 for(const n of wf.nodes){assert(!n.credentials);assert(!n.webhookId);}assert.equal(wf.active,false);assert.equal(Object.keys(wf.pinData||{}).length,0);checks++;
}
const alerts=JSON.parse(fs.readFileSync('n8n/LogiSmart_Avisos_ACTUAL.json'));const original=alerts.nodes.find(n=>n.type==='n8n-nodes-base.code').parameters.jsCode;
const code=original.replace('const permitidos=[]','const permitidos=["TEST-A","TEST-B"]');
function notify(event,state={},src=code){return vm.runInNewContext('(function(){'+src+'})()',{$input:{first:()=>({json:event})},$getWorkflowStaticData:()=>state,Date,JSON,Object,String,Array,RegExp});}
const e={workflow:{id:'TEST-A'},execution:{id:'AVISO-PRUEBA',error:{message:'DETENIDO_TARIFA_VENCIDA DATO_PRIVADO_NO_PROPAGAR'}}};
const state={};const result=notify(e,state);assert.equal(result.length,1);assert(!result[0].json.texto.includes('DATO_PRIVADO_NO_PROPAGAR'));assert.equal(notify(e,state).length,0);assert.equal(notify(e,{},original).length,0);checks+=4;
for(const [msg,want] of [['DETENIDO_LIMITE_LLAMADAS','Límite'],['timeout','Tiempo'],['401','acceso'],['otro','Fallo']]){assert(notify({workflow:{id:'TEST-B'},execution:{id:msg,error:{message:msg}}})[0].json.texto.includes(want));checks++;}
const many={alertas:Object.fromEntries(Array.from({length:300},(_,i)=>['x'+i,i]))};notify(e,many);assert(Object.keys(many.alertas).length<=200);checks++;
console.log(JSON.stringify({tipo:'EXPORTS_ACTUALES_ENTRADAS_SINTETICAS',controles:checks,resultado:'PASS',llamadas_api:0,limite:'No prueba red, credenciales ni restauración en n8n.'}));

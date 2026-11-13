// Reemplaza el contenido de Preparar datos publicos, en modo Run Once for All Items.
const estados=new Set(['PENDIENTE_APROBACION','APROBADA','RECHAZADA','DETENIDO','ACLARACION_REQUERIDA','DEVUELTO','ERROR_INCONSISTENTE']);
const decisiones=new Set(['PENDIENTE','APROBADA','RECHAZADA','NO_SOLICITADA']);
const num=v=>typeof v==='number'&&Number.isFinite(v)&&v>=0?v:null;
const registros=[];let registros_excluidos=0;
for(const {json:f} of $input.all()){
 if(!f.caso_id){registros_excluidos++;continue;}
 let r;try{r=typeof f.resultado_json==='string'?JSON.parse(f.resultado_json):f.resultado_json}catch{registros_excluidos++;continue}
 if(!r||r.modo!=='SIMULADO'||!estados.has(f.estado_final)){registros_excluidos++;continue}
 const imported=r.origen==='DEMO_IMPORTADA_H5'&&r.lote==='H5_180_V1'&&/^DEMO-H5-\d{4}$/.test(f.caso_id);
 const date=typeof f.fecha_registro==='string'?Date.parse(f.fecha_registro):NaN;
 registros.push({
 folio_publico:'MUESTRA-'+String(registros.length+1).padStart(3,'0'),
 fecha_registro:Number.isFinite(date)?new Date(date).toISOString():null,
 productos:Array.isArray(r.productos)?r.productos.filter(p=>['Producto A','Producto B'].includes(p)):[],
 importe_total:num(f.importe_total),moneda:f.moneda==='MXN'?'MXN':null,
 estado_final:f.estado_final,aprobacion_humana:decisiones.has(f.aprobacion_humana)?f.aprobacion_humana:null,
 duracion_total_ms:num(r.duracion_total_ms),
 origen:imported?'DEMO_IMPORTADA_H5':'WORKFLOW',
 completa_primer_intento:imported&&typeof r.completa_primer_intento==='boolean'?r.completa_primer_intento:null,
 sin_correcciones_auditoria:imported&&typeof r.sin_correcciones_auditoria==='boolean'?r.sin_correcciones_auditoria:null
 });
}
const meta={fuente:'Data Table LogiSmart',datos_ficticios:true,consultado_en:new Date().toISOString(),zona_horaria:'America/Mexico_City'};
let query={};try{query=$('Webhook dashboard').first().json.query||{}}catch{}
if(!query||typeof query!=='object'||Array.isArray(query)||Object.keys(query).some(k=>k!=='folio')||('folio' in query&&(typeof query.folio!=='string'||query.folio.length>64))){
 return [{json:{...meta,tipo:'error',encontrado:false,error:'ENTRADA_NO_PERMITIDA',mensaje:'Consulta de solo lectura: usa un folio publico o RESUMEN.'}}];
}
if(Object.prototype.hasOwnProperty.call(query,'folio')){
 const folio=String(query.folio||'').trim().toUpperCase();
 if(folio==='RESUMEN'){
  const conteos=Object.fromEntries([...estados].map(e=>[e,registros.filter(r=>r.estado_final===e).length]));
  return [{json:{...meta,tipo:'resumen',total_registros:registros.length,por_estado:conteos,importados_simulados:registros.filter(r=>r.origen==='DEMO_IMPORTADA_H5').length,nota:'Solo lectura; los importados no son ejecuciones de agentes.'}}];
 }
 if(!/^MUESTRA-[0-9]{3,}$/.test(folio))return [{json:{...meta,tipo:'error',encontrado:false,error:'FORMATO_INVALIDO',mensaje:'Usa el alias publico MUESTRA-001 del dashboard o RESUMEN.'}}];
 const registro=registros.find(r=>r.folio_publico===folio);
 return [{json:{...meta,tipo:'consulta_folio',encontrado:Boolean(registro),registro:registro||null,nota:'Alias de presentacion de la consulta actual; no es el folio operativo Telegram. No autoriza modificaciones.'}}];
}
return [{json:{...meta,total_registros:registros.length,registros_excluidos,registros}}];

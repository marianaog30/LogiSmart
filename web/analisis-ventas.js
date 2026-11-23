(function(root){
'use strict';
const PRODUCTS=['Producto A','Producto B'];
function products(row){return new Set(String(row.products||'').split(',').map(s=>s.trim()).filter(s=>PRODUCTS.includes(s)));}
function analyze(rows,assignments=[]){
 const amounts=rows.map(r=>r.total).filter(n=>typeof n==='number'&&Number.isFinite(n)&&n>=0).sort((a,b)=>a-b);
 const mix=[['Solo cajas · A',0],['Solo cinta · B',0],['Cajas y cinta · A + B',0],['Sin producto identificado',0]];
 for(const r of rows){const p=products(r);mix[p.size===2?2:p.has(PRODUCTS[0])?0:p.has(PRODUCTS[1])?1:3][1]++;}
 const bands=[['$0 a $250',0],['Más de $250 a $1,000',0],['Más de $1,000 a $2,500',0],['Más de $2,500',0]];
 for(const a of amounts)bands[a<=250?0:a<=1000?1:a<=2500?2:3][1]++;
 const bySupplier=assignments.map(a=>[a.proveedor,rows.filter(r=>products(r).has(a.producto)).length]);
 const m=amounts.length;
 return {rows:rows.length,known:m,missing:rows.length-m,average:m?amounts.reduce((s,n)=>s+n,0)/m:null,median:m?(m%2?amounts[(m-1)/2]:(amounts[m/2-1]+amounts[m/2])/2):null,mix,bands,bySupplier};
}
function parseAssignments(csvRows){
 if(!Array.isArray(csvRows)||csvRows.length!==3||csvRows[0].join(',')!=='producto,proveedor,origen')throw Error('Catálogo complementario no válido');
 if(csvRows.slice(1).some(r=>!Array.isArray(r)||r.length!==3))throw Error('Columnas demo no válidas');
 const out=csvRows.slice(1).map(r=>({producto:r[0],proveedor:r[1],origen:r[2]}));
 if(out.some(r=>!PRODUCTS.includes(r.producto)||!['Proveedor demo A','Proveedor demo B'].includes(r.proveedor)||r.origen!=='ASIGNACION_SINTETICA')||new Set(out.map(r=>r.producto)).size!==2||new Set(out.map(r=>r.proveedor)).size!==2)throw Error('Asignación demo fuera de contrato');
 return out;
}
function weightedScore(weights,scores){if(!Array.isArray(weights)||!Array.isArray(scores)||weights.length!==6||scores.length!==6||weights.some(n=>!Number.isFinite(n)||n<0||n>100)||scores.some(n=>!Number.isFinite(n)||n<0||n>10)||Math.abs(weights.reduce((a,b)=>a+b,0)-100)>1e-8)throw Error('Los seis pesos deben sumar100%; puntuaciones entre0y10.');return weights.reduce((sum,w,i)=>sum+w*scores[i],0)/100;}
const api={analyze,parseAssignments,weightedScore};if(typeof module==='object')module.exports=api;else root.LogiVentas=api;
})(typeof globalThis==='object'?globalThis:this);

(function(root){
'use strict';
function averageMinutes(rows){const valid=rows.filter(r=>['APROBADA','RECHAZADA','PENDIENTE_APROBACION'].includes(r.state)&&Number.isFinite(r.duration)&&r.duration>=0);return valid.length?valid.reduce((s,r)=>s+r.duration,0)/valid.length/60000:null;}
function percent(rows,key){const valid=rows.filter(r=>typeof r[key]==='boolean');return valid.length?100*valid.filter(r=>r[key]).length/valid.length:null;}
const api={averageMinutes,percent};if(typeof module==='object')module.exports=api;else root.LogiSmartMetricas=api;
})(typeof globalThis==='object'?globalThis:this);

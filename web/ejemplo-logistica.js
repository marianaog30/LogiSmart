(function(){
'use strict';
const original=[15,20,5,10,30,20],a=[7,6,9,8,3,5],b=[6,8,5,4,8,7];const el=id=>document.getElementById(id);const inputs=original.map((_,i)=>el('peso-'+i));
function update(){const weights=inputs.map(i=>i.value.trim()===''?NaN:Number(i.value));const sum=weights.reduce((s,n)=>s+n,0);el('pesos-total').textContent=Number.isFinite(sum)?'Suma de pesos: '+sum+' %.':'Completa los seis pesos.';
 try{const sa=LogiVentas.weightedScore(weights,a),sb=LogiVentas.weightedScore(weights,b);el('puntuacion-a').textContent=sa.toFixed(2)+' / 10';el('puntuacion-b').textContent=sb.toFixed(2)+' / 10';el('medidor-a').hidden=false;el('medidor-b').hidden=false;el('medidor-a').value=sa;el('medidor-b').value=sb;el('pesos-resultado').textContent=sa===sb?'Empate entre alternativas del ejercicio.':`Con estos pesos, la alternativa ${sa>sb?'A':'B'} del ejercicio obtiene mayor puntuación. No autoriza una compra.`;
 }catch{el('puntuacion-a').textContent='—';el('puntuacion-b').textContent='—';el('medidor-a').hidden=true;el('medidor-b').hidden=true;el('pesos-resultado').textContent='No calculable: cada peso debe estar entre 0 y 100 y la suma debe ser 100%.';}}
inputs.forEach(i=>i.addEventListener('input',update));el('pesos-reset').addEventListener('click',()=>{inputs.forEach((i,n)=>i.value=original[n]);update();});update();
})();

// LogiSmart H8 v1.0.0. Contrato cerrado antes de cualquier llamada LLM.
function validarSolicitudLogiSmart(s) {
  if (!s || typeof s !== 'object' || Array.isArray(s)) throw Error('H8_ESQUEMA');
  if (!/^LOG-\d{1,24}$/.test(s.caso_id || '')) throw Error('H8_CASO');
  if (s.modo !== 'SIMULADO' || s.objetivo !== 'cotizar_productos') throw Error('H8_ALCANCE');
  if (typeof s.limite_costo_usd !== 'number' || !Number.isFinite(s.limite_costo_usd) || s.limite_costo_usd <= 0 || s.limite_costo_usd > 0.10) throw Error('H8_PRESUPUESTO');
  if (typeof s.solicitud !== 'string' || !s.solicitud.trim() || s.solicitud.length > 1000) throw Error('H8_LONGITUD');
  let text=s.solicitud.normalize('NFKC').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  if (/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(text)) throw Error('H8_CARACTERES');
  // No URLs, datos personales, instrucciones ni código: solo gramática de cotización.
  const products=[];
  text=text.replace(/\b(\d{1,4})\s*(?:(?:paquetes?|unidades?|piezas?|pzas?)\s*)?(?:de(?:l)?\s*)?producto\s+([ab])\b/g,(_,number,id)=>{
    const cantidad=Number(number),limite=id==='a'?100:80;
    if(!Number.isSafeInteger(cantidad)||cantidad<1||cantidad>limite)throw Error('H8_CANTIDAD');
    if(products.some(p=>p.id===id))throw Error('H8_DUPLICADO_PRODUCTO');
    products.push({id,cantidad});return ' ';
  });
  const rest=text.replace(/\b(?:hola|por|favor|necesito|quiero|cotizar|cotiza|solicito|me|gustaria|una|cotizacion|de|del|el|la|los|las|para|y|e|mas|con)\b/g,'').replace(/[\s.,;:]/g,'');
  if(rest || !products.length) throw Error('H8_ACLARACION_REQUERIDA');
  // Minimización: el modelo recibe únicamente productos/cantidades canónicos.
  return {solicitud:'Necesito cotizar '+products.map(p=>p.cantidad+' unidades de Producto '+p.id.toUpperCase()).join(' y '),productos:products,version:'H8-1.0.0'};
}

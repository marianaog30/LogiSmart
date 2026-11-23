(function(root){'use strict';
const catalogo=Object.freeze({'Producto A':{precio:120,stock:100},'Producto B':{precio:85,stock:80}});
function csv(text){
 if(typeof text!=='string'||text.length>50000)throw Error('Texto vacío o demasiado extenso.');
 text=text.replace(/^\uFEFF/,'').replace(/\r\n?/g,'\n');
 const delimiter=text.split('\n')[0].includes(';')?';':',';
 const rows=[];let row=[],v='',quote=false;
 for(let i=0;i<text.length;i++){const c=text[i];if(c==='"'){if(quote&&text[i+1]==='"'){v+='"';i++;}else if(!quote&&v!=='')throw Error('Comillas CSV no válidas.');else quote=!quote;}else if(!quote&&(c===delimiter||c==='\n')){row.push(v.trim());v='';if(c==='\n'){if(row.some(Boolean))rows.push(row);row=[];}}else v+=c;}
 if(quote)throw Error('Comillas CSV sin cerrar.');row.push(v.trim());if(row.some(Boolean))rows.push(row);
 if(rows.length>501)throw Error('Máximo 500 filas de datos.');return rows;
}
function solicitudes(text){
 let rows;if(text.trim().startsWith('[')||text.trim().startsWith('{')){
 let o;try{o=JSON.parse(text);}catch{throw Error('JSON no válido.');}const a=Array.isArray(o)?o:o.productos;
 if(!Array.isArray(a)||a.length>100)throw Error('JSON: usa una lista de objetos producto y cantidad (máximo 100).');
 rows=a.map(x=>{if(!x||typeof x!=='object'||Array.isArray(x)||typeof x.producto!=='string')throw Error('Cada objeto requiere producto y cantidad.');return[x.producto,x.cantidad];});
 }else{rows=csv(text);if(rows[0]?.[0].toLowerCase()==='producto'&&rows[0]?.[1].toLowerCase()==='cantidad')rows.shift();}
 if(!rows.length||rows.length>100)throw Error('Usa entre 1 y 100 líneas de producto,cantidad.');
 const cantidades=new Map();for(const row of rows){if(row.length!==2)throw Error('Cada línea requiere exactamente producto,cantidad.');const p=String(row[0]).trim();const match=/^producto\s+([ab])$/i.exec(p);if(!match)throw Error('Producto no autorizado: revisa el catálogo. Solo Producto A y Producto B.');const name='Producto '+match[1].toUpperCase();if(!/^\d+$/.test(String(row[1]).trim()))throw Error('La cantidad debe ser un entero positivo de paquetes.');const q=Number(row[1]);if(!Number.isSafeInteger(q)||q<1)throw Error('Cantidad no válida.');cantidades.set(name,(cantidades.get(name)||0)+q);}
 const lineas=[...cantidades].map(([producto,cantidad])=>{const c=catalogo[producto];if(cantidad>c.stock)throw Error('Cantidad superior al inventario ficticio de '+producto+'. Solicita aclaración.');return{producto,cantidad,unidad:'paquete',precio_unitario:c.precio,subtotal:c.precio*cantidad};});
 return{modo:'SIMULADO',origen:'VISTA_PREVIA_LOCAL',catalogo_version:'1.1',moneda:'MXN',aprobacion_humana:'NO_SOLICITADA',lineas,total:lineas.reduce((a,l)=>a+l.subtotal,0)};
}
const api={csv,solicitudes,catalogo};if(typeof module!=='undefined')module.exports=api;else root.LogiArchivos=api;
})(typeof window==='undefined'?globalThis:window);

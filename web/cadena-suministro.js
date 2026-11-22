/* Widget explicativo de LogiSmart: sin red, sin métricas ni decisiones operativas. */
(()=>{'use strict';
const root=document.getElementById('supply-chain');if(!root)return;
const stages={
proveedores:['Proveedores de materiales de empaque','En una distribuidora, los proveedores abastecen los productos que después se ofrecen a clientes. Aquí se explica su posición en la cadena.','Conceptual: no hay compras ni integración con proveedores.','No se publican proveedores, órdenes de compra ni plazos inventados.','El abastecimiento antecede a la disponibilidad; este prototipo no calcula reabastecimiento.'],
recepcion:['Recepción y almacenamiento','Recibir, revisar y ubicar materiales permite disponer de productos para su distribución.','Conceptual: no existe un almacén físico conectado ni recepción automatizada.','No se simulan escaneos, ubicaciones ni entradas físicas como si fueran reales.','Conecta el abastecimiento con el inventario; no se mide exactitud de almacén en este panel.'],
catalogo:['Catálogo y disponibilidad ficticia','Beta contrasta Producto A y Producto B con el catálogo autorizado. Las nuevas cantidades se expresan en paquetes.','Implementado sobre un catálogo académico; no representa existencias físicas ni reservas.','Precio autorizado, cantidad solicitada, disponibilidad ficticia y fuente del catálogo.','Una cotización necesita una referencia coherente de producto y disponibilidad antes de proponer un importe.'],
cotizacion:['Cotización provisional','Alfa interpreta la solicitud, Beta contrasta el catálogo, Gamma redacta la propuesta y Omega verifica su coherencia. Maestro coordina las etapas.','Implementado con servicios reales y datos ficticios; propuesta pendiente de decisión humana.','Productos, cantidades, precios autorizados, subtotales, total y dictamen técnico del mismo caso.','Ayuda a evitar errores de especificación antes de preparar un pedido. No mide entregas ni ahorro logístico.'],
decision:['Decisión humana en Telegram','La persona autorizada revisa la propuesta y utiliza el botón de aprobar o rechazar vinculado al caso y su versión.','Implementado: registra una decisión de prueba; Omega no sustituye a la persona.','Estado persistido y notificación del resultado. El dashboard solo consulta la exportación.','Es un punto de control previo a cualquier compromiso; no autoriza cobros o despachos reales.'],
entrega:['Preparación, despacho y entrega','Después de aceptar una propuesta, una operación logística completa prepararía el pedido y coordinaría su entrega.','Conceptual: esta etapa está fuera del alcance implementado.','No hay rastreo, transportistas, fechas de entrega, costos de flete ni pruebas de recepción verificadas.','Completa el contexto de la cadena de suministro; no debe confundirse con funcionalidades disponibles.']
};
for(const button of root.querySelectorAll('button[data-stage]'))button.addEventListener('click',()=>{
const values=stages[button.dataset.stage];if(!values)return;
for(const other of root.querySelectorAll('button[data-stage]'))other.setAttribute('aria-pressed',String(other===button));
['supply-stage-title','supply-description','supply-scope','supply-evidence','supply-logistics'].forEach((id,i)=>document.getElementById(id).textContent=values[i]);
});
})();

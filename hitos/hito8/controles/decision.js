// Comprobar además el cambio condicional PENDIENTE -> decisión en Data Table.
function validarDecisionLogiSmart(fila,d,ahora) {
  if (!fila || !d || d.datos_validos !== true || !['APROBAR','RECHAZAR'].includes(d.accion))return 'Datos de decisión inválidos.';
  if(!fila.caso_id || fila.caso_id!==d.caso_id)return 'La cotización no existe o no coincide.';
  if(String(fila.usuario_id)!==String(d.usuario_id)||String(fila.chat_id)!==String(d.chat_id))return 'Usuario o chat no autorizado.';
  if(!Number.isSafeInteger(d.version)||d.version<1||Number(fila.version_propuesta)!==d.version)return 'La versión de la cotización no coincide.';
  if(fila.estado_final!=='PENDIENTE_APROBACION'||fila.aprobacion_humana!=='PENDIENTE')return 'La cotización ya fue procesada o no está pendiente.';
  const fecha=Date.parse(fila.fecha_registro),ttl=24*60*60*1000;
  if(!Number.isFinite(fecha)||!Number.isFinite(ahora)||fecha>ahora||ahora-fecha>=ttl)return 'La propuesta expiró: solicita una nueva cotización.';
  return '';
}

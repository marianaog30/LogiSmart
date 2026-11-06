# Hito 6 · Publicación y actualización

El panel publica únicamente `web/`, con 188 registros ficticios en la exportación inicial. La fecha `consultado_en` es la consulta al registro, no la fecha de decisión ni de modificación de cada caso. Los casos importados conservan su origen simulado. Los KPI de calidad de esos casos son simulados; los valores sin evidencia permanecen null.

## Actualizar

Exportación manual reproducible: consultar el webhook público sanitizado existente de n8n, conservar únicamente los campos enumerados en `scripts/validar.mjs`, sustituir `web/datos/cotizaciones.json`, ejecutar `node scripts/validar.mjs` y hacer commit en main. Actions valida y publica si pasa. No existe actualización programada: el retraso es el tiempo hasta la próxima exportación manual más la ejecución de Actions. El botón del panel solo relee el archivo publicado. Después de 24 horas desde la exportación muestra aviso de antigüedad (umbral de interfaz, no SLA).

El asistente consulta n8n en vivo; puede responder con información posterior a la exportación. GitHub Pages no ejecuta n8n ni Python. Las credenciales, decisiones operativas, conversaciones y trazas privadas permanecen fuera del sitio.

## Evidencia de bloqueo

En Actions → Verificar y publicar LogiSmart → Run workflow, activar `probar_fallo`. Solo en el runner se incrementa `total_registros`; el mismo validador detecta que no coincide con las filas y el job publicar queda omitido. El archivo del repositorio no se modifica. Reejecutar manualmente con `probar_fallo` desactivado valida los datos correctos y permite publicar. Guardar ambos enlaces en la entrega.

## Validación pública

Abrir la URL de Pages, confirmar conteo, fecha, filtros y reset, historial y avisos. Autorizar el hostname de Pages en ElevenLabs conservando los orígenes existentes. Probar consulta de folio y resumen con consentimiento del usuario; conservar resultado de herramienta y respuesta sin publicar conversaciones completas. La interacción por voz exige aceptación y permiso de micrófono del usuario.

## Ejecuciones conservadas

- Bloqueo deliberado comprobado: https://github.com/marianaog30/LogiSmart/actions/runs/42273907767 — verificar falló y publicar quedó omitido. Los datos del repositorio permanecieron intactos.
- Datos correctos y despliegue exitoso: https://github.com/marianaog30/LogiSmart/actions/runs/42274092137.
- URL pública: https://marianaog30.github.io/LogiSmart/.
- Verificación pública: 188 registros cargados, búsqueda de MUESTRA-008 devuelve una fila (120 MXN, aprobada, importada simulada), reset restaura 188. El widget oficial muestra sus controles; dominio marianaog30.github.io autorizado conservando hosts previos.
- La repetición de las dos consultas desde el widget público requiere la aceptación de términos por la usuaria. No se presenta como conversación pública ya comprobada hasta realizarla.

Referencia de configuración: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages.

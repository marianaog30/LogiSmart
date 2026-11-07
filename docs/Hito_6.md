# Hito 6 — Publicación y actualización verificables

Mariana Orozco · LogiSmart Solutions · Empresa ficticia distribuidora.

## Estado y separación pública/privada

El sitio público es https://marianaog30.github.io/LogiSmart/. Pages publica únicamente `web/`, nunca ejecuta n8n, Python ni los agentes. `web/datos/cotizaciones.json` es un corte ficticio sanitizado; `consultado_en` indica cuándo se consultó la fuente, no cuándo cambió o se decidió cada caso. Se conserva `null` cuando falta evidencia. Los indicadores de primera validación y auditoría disponibles corresponden a casos importados y simulados, no a mediciones de mejora del negocio.

GitHub conserva README, fuente, datos ficticios sanitizados, JSON n8n exportables, skills, loops y pruebas. Las claves de OpenAI/Telegram y los datos de autorización se configuran solo en la instancia privada de n8n. La simulación de GitHub usa su Secret compartido; el workflow de actualizar datos no necesita secretos. El identificador público del widget ElevenLabs es visible por diseño, pero ninguna API key se publica en HTML, datos o artifacts.

## Actualización manual reproducible, sin terminal

1. Abre Actions → **Actualizar datos sanitizados y publicar** → Run workflow → main → Run workflow.
2. El exportador lee únicamente el endpoint público sanitizado existente de n8n, sin autenticación privada. Aplica una lista cerrada de metadatos/campos, conserva ausencias como null y comprueba folios, tipos, orígenes y coherencia de decisiones.
3. Ejecuta pruebas del exportador y `node scripts/validar.mjs`: datos, fórmulas, campos y archivos requeridos. Si algo falla no se guarda el corte ni se publica.
4. Con controles correctos, guarda únicamente `web/datos/cotizaciones.json` en un commit y publica el artifact de `web/`. El workflow despliega explícitamente en la misma ejecución: no depende de que un commit del bot active otro workflow.
5. Abre Pages, pulsa Actualizar exportación y comprueba conteo, fecha y un folio del corte. El botón de la web relee el archivo; no consulta directamente la tabla ni genera cotizaciones.

Frecuencia: manual, después de las pruebas o decisiones que deban reflejarse en la entrega; no existe horario automático ni actualización inmediata por aprobar en Telegram. Retraso esperado: hasta la siguiente ejecución manual más su duración y la propagación de Pages; sin SLA ni plazo garantizado. Tras 24 horas el panel avisa antigüedad (umbral de interfaz).

Alternativa local con Python 3: `python3 scripts/exportar_datos.py`, después `node scripts/validar.mjs` y commit del JSON. Para revisión sin red: `python3 scripts/exportar_datos.py --archivo archivo_sanitizado.json`. El exportador no reemplaza el destino si la fuente falla o no satisface el contrato. Un fallo de publicación conserva el sitio anterior; el último commit puede existir aunque el despliegue haya fallado, por lo que siempre se comprueba Pages.

## Verificación y bloqueo obligatorios

El workflow **Verificar y publicar LogiSmart** se activa por cambios en main y manualmente. Publica solo si el job verificar pasa.

- [Fallo deliberado conservado](https://github.com/marianaog30/LogiSmart/actions/runs/42273907767): altera el conteo solo en el runner, verificar falla y publicar queda omitido. No se modificó la exportación del repositorio.
- [Corrección y publicación exitosa](https://github.com/marianaog30/LogiSmart/actions/runs/42274092137): datos válidos y despliegue correcto.
- [Publicación del corte de 190 casos](https://github.com/marianaog30/LogiSmart/actions/runs/42319093404). Es un conteo de registros ficticios, no de ejecuciones reales de agentes.

Para repetir la evidencia sin tocar datos persistentes: ejecutar el workflow de publicación con `probar_fallo=true`, comprobar publicación omitida y repetir con false. Conservar los enlaces de ambas ejecuciones. La falla se elimina al acabar el runner; la ejecución siguiente usa el JSON correcto.

## Comprobación pública y pendiente de cierre

El dominio de Pages está autorizado en ElevenLabs; el widget oficial se mantiene conectado al servicio y la consulta usa la herramienta n8n de solo lectura. Ver controles visibles no prueba una conversación completa. La usuaria confirmó que aún no ha realizado la prueba desde la web pública; las pruebas locales anteriores no la sustituyen.

Prueba pendiente que realiza Mariana:

1. Abrir Pages y elegir Consultar por texto.
2. Leer y aceptar personalmente el aviso de ElevenLabs si desea continuar.
3. Escribir `Sí, acepto. Consulta MUESTRA-008`. Contrastar con la fila del dashboard: Producto A, 120 MXN, origen importado/simulado. Si el estado cambia en n8n, actualizar el corte antes de comparar.
4. Pedir `Dame el resumen general de cotizaciones`. Comparar contra la exportación recién actualizada; el agente consulta n8n en vivo y puede responder un dato más reciente.
5. Conservar solo una ficha de resultado: fecha, caso, coincidencia, resultado de herramienta y captura sanitizada si procede. No subir exportaciones completas de conversaciones ni datos de acceso.

El Hito 6 permanece **pendiente de esa comprobación pública del asistente**, incluso si Actions y Pages pasan. La medición del costo de modelos n8n corresponde al pendiente del Hito 7, no se presenta como requisito ya resuelto del Hito 6.

## Prueba del mecanismo de actualización — 6 de noviembre de 2026

[Ejecución de lectura, validación, commit y publicación](https://github.com/marianaog30/LogiSmart/actions/runs/42320519192). El job actualizar pasó las pruebas del exportador, obtuvo 190 registros y superó el validador del dashboard. Guardó la exportación en el commit `3d48c3e`, con consulta de la fuente a las 18:49:08 de Ciudad de México. El corte conserva MUESTRA-189 como rechazada y MUESTRA-190 como aprobada; sus importes provisionales son 3,510 y 495 MXN. Son datos ficticios. La comprobación visual de Pages debe leer ese mismo corte; la prueba del widget público aún corresponde a Mariana.

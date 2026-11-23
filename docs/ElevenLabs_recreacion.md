# Configuración vigente y recreación de WALL-E

Corte22 de noviembre de2026. Propósito: explicar LogiSmart y consultar folios ficticios; no aprobar, cobrar ni despachar. Español, identificación como IA y consentimiento del proveedor. El permiso de micrófono lo concede la persona.

## Configuración que debe recrearse

1. Crear el agente y cargar `agentes/WALL_E_instrucciones_recreacion.txt`. Es un respaldo del12nov: base de recreación, no export nativo actual garantizado. Revisar nombre WALL-E, alcance de consulta y catálogo A/B. Voz histórica Eric; no se declara verificada la selección actual de voz/modelo.
2. Añadir conocimiento de `docs/LogiSmart_Contexto_Empresarial_Logistica.md` y `docs/Catalogo_descriptivo_v1_1.md`. Las descripciones no sustituyen precios e inventarios autorizados de n8n.
3. Importar y configurar `n8n/LogiSmart_Voz_ACTUAL.json` según `n8n/README.md`.
4. Crear herramienta de servidor `consultar_logismart`: GET `https://orozco08.app.n8n.cloud/webhook/logismart-voz`, query obligatoria `folio` de tipo cadena. Admitir alias público MUESTRA o RESUMEN, sin parámetros arbitrarios.
5. Configurar encabezado `X-LogiSmart-Voice-Key`, valor de tipo Secreto. La persona guarda el mismo valor privadamente en ElevenLabs y Header Auth de n8n. No usar la clave OpenAI o la de escritura de Actions. Nunca ponerlo en HTML, URL ni archivos de entrega.
6. Autorizar el host `marianaog30.github.io`, mantener alternativa textual y publicar los cambios del agente. Conservar el identificador público usado en `web/index.html`; duplicar el agente crea otro identificador y exige actualizar el widget. No ampliar dominios sin necesidad.
7. Aceptar el aviso personalmente, abrir conversación nueva y consultar un alias verificado del dashboard; después pedir RESUMEN. Comparar estado e importe con la tabla del mismo corte. Las decisiones se hacen solo en Telegram.

## Evidencia y límites

La conexión protegida está instalada: el22nov se verificaron desde «Probar herramienta» MUESTRA-199 aprobada205MXN y RESUMEN del corte199. No confundir esa prueba HTTP con una conversación nueva de micrófono.

La voz histórica está respaldada en `costos/Voz_exitosa.json`: MUESTRA-196 aprobada495MXN,99s de sesión, USD0.0119 de LLM. No se publican audio ni transcripciones privadas; tokens/modelo desconocidos. Duración de sesión no equivale a duración exacta hablada.

Estado observado22nov: widget no conecta y planFree sin créditos. La captura aportada por Mariana indica reinicio23nov; comprobar saldo tras esa fecha, sin garantizar renovación por adelantado. Pendientes: conversación nueva por micrófono tras migración y permiso denegado con alternativa textual. No presentar estas rutas como aprobadas por el éxito histórico.

El webhook público `/webhook/logismart-dashboard` se reserva al panel de datos ficticios; no es el destino vigente de la herramienta de voz. La ruta protegida consulta ese registro público en el servidor y no escribe ni aprueba. Cada consulta de voz puede implicar aproximadamente dos ejecuciones n8n.

Los alias MUESTRA dependen del orden de consulta. `datos/Mapa_casos_del_corte.json` congela la relación de los casos de entrega; no usar ese alias para aprobar en Telegram.

Documentación oficial del método: https://elevenlabs.io/docs/eleven-agents/customization/widget y https://elevenlabs.io/docs/eleven-agents/customization/tools/webhook-tools . No se contrató ningún plan ni se publica ningún secreto.

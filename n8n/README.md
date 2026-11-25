# Importación de los workflows actuales

Usar únicamente estos cuatro archivos para una nueva instalación:

- `LogiSmart_Telegram_ACTUAL.json`: 65 nodos; Telegram, decisiones, registro y consultas públicas.
- `LogiSmart_GitHub_ACTUAL.json`: 45 nodos; entrada protegida de Actions y cuatro agentes con consumo medido.
- `LogiSmart_Avisos_ACTUAL.json`: tres nodos; notifica errores sin IA.
- `LogiSmart_Voz_ACTUAL.json`: siete nodos; entrada GET protegida de solo lectura para ElevenLabs, sin LLM ni decisiones.

Los demás JSON de esta carpeta y de hitos/ son versiones históricas y laboratorios; no activarlos como receptores del mismo bot.

## Catálogo 2.0

Los dos flujos de cotización aceptan los doce productos A–L del catálogo sintético `web/datos/catalogo_productos.csv`. A y B conservan los precios anteriores; D×2 + E×3 produce $645 MXN en la prueba determinista. Los exports se entregan desactivados y sin identificadores de nodos, credenciales, webhooks ni datos fijados. Al importar, vincular la tabla y las credenciales nuevas antes de publicar. La ampliación ya se publicó en la instancia de demostración; importar estos JSON en otra cuenta requiere configurar sus dependencias y volver a verificar.

En el flujo de voz, `Consultar registro sanitizado` contiene el marcador `https://CONFIGURAR_HOST_N8N/webhook/logismart-dashboard`. Sustituirlo por el host del webhook público sanitizado de la cuenta donde se importe. El marcador evita publicar una dirección interna de instancia en el export.

## Importar y configurar

1. Importar los cuatro JSON sin publicar todavía. Los archivos se exportaron sanitizados; sus nombres originales pueden ser confusos, por lo que deben identificarse por esta guía y por sus nodos.
2. Crear una Data Table privada. Campos: `caso_id` texto, `usuario_id` texto, `chat_id` texto, `solicitud` texto, `estado_final` texto, `importe_total` número, `moneda` texto, `aprobacion_humana` texto, `version_propuesta` número, `fecha_registro` fecha, `resultado_json` texto. Los exports actuales guardan esos once campos y actualizan estado_final/aprobacion_humana; no crear id/createdAt/updatedAt como columnas de negocio: son columnas de sistema.
3. Vincular esa tabla en cada nodo Data Table de ambos workflows. No usar los identificadores de la cuenta anterior.
4. Crear las credenciales privadas OpenAI, Telegram y Header Auth. Seleccionar la misma OpenAI en los ocho nodos HTTP de generación/conteo de cada flujo que los contenga. Las claves no vienen dentro del ZIP.
5. Completar las listas autorizadas vacías de los nodos de entrada y decisión y el destinatario autorizado del flujo GitHub y de avisos. Por defecto el export sanitizado deniega acceso. No abrir permisos a cualquier usuario para hacer funcionar la prueba.
6. En Header Auth usar nombre `LogiSmart-key`; guardar el mismo valor privado en GitHub `N8N_SIMULATION_KEY`. No mostrarlo en video.
7. Publicar el notificador; seleccionarlo en Settings → Error workflow de los otros dos. Configurar su lista de IDs permitidos con los IDs nuevos. Los IDs privados y enlaces de error se quitaron de los archivos públicos.
8. En cada flujo, `Preparar llamada 1` posee la política de tarifas. Verificar modelo, precios, consulta y vigencia antes de usar; los otros once nodos leen esa política, no mantener copias divergentes.
9. Publicar solo un Telegram Trigger para @L0g1SmartBot. No mantener activo el receptor de una cuenta anterior ni probar manualmente ese trigger mientras esté publicado.
10. Actualizar host/path en `scripts/exportar_datos.py`, `scripts/ejecutar_simulacion.py` y la herramienta de ElevenLabs si se cambia de cuenta. Probar primero GET sanitizado; después un caso y su decisión humana.

Estas exportaciones no contienen el historial privado completo ni el estado histórico de deduplicación. El respaldo privado se conserva aparte de la entrega. No se ha demostrado restauración completa en una tercera cuenta. Parar: despublicar primero el receptor que se va a retirar y verificar el nuevo antes de trasladar el bot; requiere coordinación humana.

## Ruta de voz protegida (verificada el22 de noviembre)

En `Entrada voz protegida`, seleccionar Header Auth independiente: nombre del encabezado `X-LogiSmart-Voice-Key`. Guardar su valor únicamente en la credencial privada n8n y en un secreto ElevenLabs del mismo valor. La herramienta `consultar_logismart` usa GET `https://orozco08.app.n8n.cloud/webhook/logismart-voz`, parámetro obligatorio `folio` y encabezado de tipo Secreto. No reutilizar la clave de escritura de Actions ni la de OpenAI. Si se cambia de instancia, actualizar también el destino fijo de `Consultar registro sanitizado`.

Publicar el flujo y probar desde la herramienta ElevenLabs `MUESTRA-200` (aprobada,290MXN en el corte201 de entrega) y `RESUMEN`. El resumen debe coincidir con la tabla consultada en ese momento, no con un número histórico fijo. La prueba de herramienta autenticada conservada corresponde al corte anterior199; no reinterpretarla como consulta nueva201. No guardar la prueba como mock: debe ejecutar la herramienta real. La ruta hace una consulta adicional al webhook público sanitizado: aproximadamente dos ejecuciones n8n por consulta de voz, sin nuevos tokens de agentes. Los datos públicos siguen siendo ficticios; esta ruta no concede acceso a registros privados ni modifica casos.


## Laboratorios opcionales de verificación

`tests/QA_manual_sin_consumo.json` comprueba12componentes con fixtures; `tests/QA_HTTP_manual_sin_claves.json` comprueba rechazo401 y timeout en HTTP real sin clave. Importar por separado, ejecutar manualmente, no publicar. No son workflows operativos ni sustituyen los cuatro de arriba. Resultados y límites: `evidencias/cierre/QA_componentes_n8n_22.json` y `QA_HTTP_n8n_22.json`.

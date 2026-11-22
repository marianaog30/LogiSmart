# Configuración y recreación de WALL-E

Propósito: explicar LogiSmart y consultar folios ficticios, sin crear aprobaciones ni ejecutar despachos. Español, voz elegida en la cuenta, identificación como IA y consentimiento del proveedor antes de voz. La selección histórica de voz fue Eric; la voz/modelo publicados actuales requieren nueva inspección, no se declaran verificados aquí.

`agentes/WALL_E_instrucciones_recreacion.txt` conserva el sistema respaldado el 12 de noviembre; es base de recreación, no export nativo actual garantizado. Adjuntar `docs/LogiSmart_Contexto_Empresarial_Logistica.md` y `docs/Catalogo_descriptivo_v1_1.md` como conocimiento. El catálogo descriptivo no sustituye al catálogo autorizado de n8n para importes/stock.

Herramienta `consultar_logismart`: GET `https://orozco08.app.n8n.cloud/webhook/logismart-dashboard`, parámetro `folio` obligatorio, cadena; admite MUESTRA-196 o RESUMEN. Folio inexistente → encontrado=false; parámetros adicionales y formato inválido se rechazan. Widget oficial en `web/index.html`, ID público del agente permitido por diseño. Autorizar el dominio `marianaog30.github.io`; mantener texto como alternativa. Nunca incrustar API keys.

## Brecha frente a la guía

El endpoint actual es público de solo lectura y ficticio. La guía, página 5, exige herramienta de servidor autenticada. Minimizar datos no sustituye esa autenticación. Antes de declarar cumplimiento completo: crear una ruta exclusiva de voz con Header Auth, guardar el secreto solo en el servidor de ElevenLabs, vincular la misma tabla y validar consultas. Mantener GET público para el dashboard. No incluir la credencial en HTML, URL ni documentos. Este cambio no está instalado ni verificado en la versión entregada.

También se requiere un identificador público persistente o un mapa sanitizado congelado para reconciliar `caso_id` interno con MUESTRA; los alias de la consulta actual dependen del orden y no deben usarse para aprobar.

## Pruebas y evidencia

Voz verificada históricamente: `costos/Voz_exitosa.json`, MUESTRA-196 APROBADA por MXN495, 99s de sesión, USD0.0119 LLM; tokens/modelo no entregados en el desglose. No se publican audio/transcripciones privadas. Última prueba no garantiza saldo actual. Deben repetirse micrófono denegado y alternativa textual, caída del servicio y el nuevo endpoint autenticado si se instala. Consentimiento y permiso de micrófono siempre los completa la persona.

Recrear: crear agente → cargar instrucciones y documentos → configurar herramienta → configurar dominio/widget → publicar → aceptar aviso personalmente → consultar folio y RESUMEN → contrastar respuesta con registro y fecha. Fuente del método oficial: https://elevenlabs.io/docs/eleven-agents/customization/widget y https://elevenlabs.io/docs/eleven-agents/customization/tools/webhook-tools .

# Simulación GitHub → n8n → Telegram

Workflow manual: `.github/workflows/simular-cotizacion.yml`. Solicita cantidades ficticias A (1–100) y B (1–80); por defecto 8 y 30. Activa el flujo separado de n8n `LogiSmart - GitHub Actions a agentes y Telegram`. No modifica el flujo original del bot.

## Estado de preparación

Código subido y sintaxis/conexiones revisadas. El flujo privado nuevo se importó con las credenciales y tabla existentes; todavía está inactivo, pendiente de Header Auth. No se afirma ejecución integral ni envío Telegram desde Actions hasta completar la clave y probar.

## Configuración privada pendiente

En el webhook Entrada GitHub protegida, crear Header Auth con Name `X-LogiSmart-Key` y Value una clave aleatoria larga guardada privadamente. Crear en GitHub Actions el Secret `N8N_SIMULATION_KEY` con exactamente ese mismo valor. No utilizar aquí las API keys de los modelos ni el token del bot. El usuario introduce la nueva credencial directamente en las dos plataformas.

Tras guardar la credencial, publicar el flujo n8n y ejecutar manualmente Simular cotización y enviar a Telegram. Los agentes procesan la solicitud, guardan el caso y envían la propuesta. Solo la respuesta final sanitizada confirma el envío; Actions no registra destinatarios, credenciales ni la respuesta completa. La decisión se toma con los botones del bot original.

Una comprobación previa por folio evita repetir casos ya guardados del mismo run_id. No es una garantía transaccional ante solicitudes concurrentes ni reintenta automáticamente si hay un timeout. Si se guardó el caso y falló el envío, revisar y recuperar privadamente en n8n antes de repetir.

La copia importable pública omite credenciales, tabla y destinatario; requiere configurarlos. Esta simulación no actualiza por sí sola la exportación estática del dashboard. Los resultados simulados importados permanecen diferenciados de nuevas ejecuciones reales de agentes sobre datos ficticios.

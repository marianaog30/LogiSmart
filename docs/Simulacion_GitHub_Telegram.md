# Simulación GitHub → n8n → Telegram

Workflow manual: `.github/workflows/simular-cotizacion.yml`. Solicita cantidades ficticias A (1–100) y B (1–80); por defecto 8 y 30. Activa el flujo separado de n8n `LogiSmart - GitHub Actions a agentes y Telegram`. No modifica el flujo original del bot.

## Estado de preparación

Integración publicada y comprobada el 6 de noviembre de 2026. Actions completó la ejecución #2 en 55 segundos; n8n terminó correctamente en 46.612 segundos y confirmó enviado_telegram=true, estado PENDIENTE_APROBACION y decisión humana PENDIENTE. Los cuatro agentes recorrieron el flujo. No se tomó la decisión humana.

## Configuración privada

En el webhook Entrada GitHub protegida, crear Header Auth con Name `LogiSmart-key` y Value una clave aleatoria larga guardada privadamente. Crear en GitHub Actions el Secret `N8N_SIMULATION_KEY` con exactamente ese mismo valor. No utilizar aquí las API keys de los modelos ni el token del bot. El usuario introduce la nueva credencial directamente en las dos plataformas.

Tras guardar la credencial, publicar el flujo n8n y ejecutar manualmente Simular cotización y enviar a Telegram. Los agentes procesan la solicitud, guardan el caso y envían la propuesta. Solo la respuesta final sanitizada confirma el envío; Actions no registra destinatarios, credenciales ni la respuesta completa. La decisión se toma con los botones del bot original.

Una comprobación previa por folio evita repetir casos ya guardados del mismo run_id. No es una garantía transaccional ante solicitudes concurrentes ni reintenta automáticamente si hay un timeout. Si se guardó el caso y falló el envío, revisar y recuperar privadamente en n8n antes de repetir.

La copia importable pública omite credenciales, tabla y destinatario; requiere configurarlos. Esta simulación no actualiza por sí sola la exportación estática del dashboard. Los resultados simulados importados permanecen diferenciados de nuevas ejecuciones reales de agentes sobre datos ficticios.

## Evidencia integral

[Actions: simulación #2 exitosa](https://github.com/marianaog30/LogiSmart/actions/runs/42278436741). La primera prueba devolvió 403 porque el nombre del encabezado difería entre n8n y el script; se alineó el script a `LogiSmart-key` sin modificar ni exponer el Secret. No se publican logs de entrada del webhook, claves, destinatarios ni conversaciones completas.

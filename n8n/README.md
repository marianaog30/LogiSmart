# Importación de los workflows actuales

Usar únicamente estos tres archivos para una nueva instalación:

- `LogiSmart_Telegram_ACTUAL.json`: 65 nodos; Telegram, decisiones, registro y consultas públicas.
- `LogiSmart_GitHub_ACTUAL.json`: 45 nodos; entrada protegida de Actions y cuatro agentes con consumo medido.
- `LogiSmart_Avisos_ACTUAL.json`: tres nodos; notifica errores sin IA.

Los demás JSON de esta carpeta y de hitos/ son versiones históricas y laboratorios; no activarlos como receptores del mismo bot.

## Importar y configurar

1. Importar los tres JSON sin publicar todavía. Los archivos se exportaron sanitizados; sus nombres originales pueden ser confusos, por lo que deben identificarse por esta guía y por sus nodos.
2. Crear una Data Table privada. Campos: `caso_id` texto, `usuario_id` texto, `chat_id` texto, `solicitud` texto, `estado_final` texto, `importe_total` número, `moneda` texto, `aprobacion_humana` texto, `version_propuesta` número, `fecha_registro` fecha, `resultado_json` texto. Reproducir cualquier campo adicional requerido por los nodos de actualización según su mapeo; no importar id/createdAt/updatedAt como columnas de negocio.
3. Vincular esa tabla en cada nodo Data Table de ambos workflows. No usar los identificadores de la cuenta anterior.
4. Crear las credenciales privadas OpenAI, Telegram y Header Auth. Seleccionar la misma OpenAI en los ocho nodos HTTP de generación/conteo de cada flujo que los contenga. Las claves no vienen dentro del ZIP.
5. Completar las listas autorizadas vacías de los nodos de entrada y decisión y el destinatario autorizado del flujo GitHub y de avisos. Por defecto el export sanitizado deniega acceso. No abrir permisos a cualquier usuario para hacer funcionar la prueba.
6. En Header Auth usar nombre `LogiSmart-key`; guardar el mismo valor privado en GitHub `N8N_SIMULATION_KEY`. No mostrarlo en video.
7. Publicar el notificador; seleccionarlo en Settings → Error workflow de los otros dos. Configurar su lista de IDs permitidos con los IDs nuevos. Los IDs privados y enlaces de error se quitaron de los archivos públicos.
8. En cada flujo, `Preparar llamada 1` posee la política de tarifas. Verificar modelo, precios, consulta y vigencia antes de usar; los otros once nodos leen esa política, no mantener copias divergentes.
9. Publicar solo un Telegram Trigger para @L0g1SmartBot. No mantener activo el receptor de una cuenta anterior ni probar manualmente ese trigger mientras esté publicado.
10. Actualizar host/path en `scripts/exportar_datos.py`, `scripts/ejecutar_simulacion.py` y la herramienta de ElevenLabs si se cambia de cuenta. Probar primero GET sanitizado; después un caso y su decisión humana.

Estas exportaciones no contienen los 202 registros privados ni el estado histórico de deduplicación. El respaldo privado se conserva aparte de la entrega. No se ha demostrado restauración completa en una tercera cuenta. Parar: despublicar primero el receptor que se va a retirar y verificar el nuevo antes de trasladar el bot; requiere coordinación humana.

# Workflow n8n actualizado

`LogiSmart_Ecosistema_Agentes.json` es la exportación pública sanitizada del flujo actual: Telegram, cuatro agentes, Maestro, aprobación humana y consulta del dashboard/ElevenLabs. Conserva 53 nodos y sus conexiones. Incluye la corrección de `/new` y `/nuevo` y los nombres Alfa, Beta, Gamma y Omega en la respuesta de Telegram.

## Configurar después de importar

1. Importar como workflow nuevo e inactivo; conservar la instancia operativa existente.
2. Asignar credenciales privadas de Telegram y de los cuatro modelos. No incluirlas en GitHub.
3. Seleccionar la Data Table LogiSmart en los cinco nodos de tabla. El marcador `CONFIGURAR_ID_TABLA_LOGISMART` no es un identificador operativo. Crear la tabla y sus columnas según los mapeos del JSON si no existe; sus filas no se exportan aquí.
4. Configurar en `Preparar solicitud telegram` la lista `usuariosPermitidos` con IDs autorizados, únicamente dentro de la instancia privada. La lista publicada está vacía: deniega solicitudes hasta configurarla.
5. Revisar webhook, origen permitido y URL de consulta del dashboard/herramienta en cada entorno. Publicar solo después de probar las credenciales y autorizaciones. Un bot de Telegram no debe tener dos workflows activos compitiendo por su webhook.

## Límites y validación

La exportación no contiene credenciales, IDs privados de acceso/tabla, datos fijados ni registros o decisiones humanas almacenadas. `active` es false. Los IDs internos de nodos solo conservan la estructura del diagrama.

Se validaron JSON, 53 nombres únicos, destinos de conexiones y sintaxis de 15 nodos Code. Esta copia sanitizada no se importó ni ejecutó contra servicios; requiere configuración privada. El flujo operativo de n8n no se modificó al publicar esta copia.

Empresa, catálogo y cotizaciones ficticias. La aprobación técnica no sustituye la decisión humana. Los casos importados simulados no son evidencia de ejecuciones reales. GitHub almacena la configuración: no ejecuta n8n. Este cambio no configura Pages ni Actions.

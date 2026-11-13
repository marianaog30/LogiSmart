# Hito 10 · Costos y evidencia de LogiSmart

Abre **Costos_LogiSmart.xlsx** para ver resumen, escenarios editables y registro. **costos.csv** contiene las mismas fuentes y campos auditables en UTF-8 con BOM. El informe explica resultados, fuentes y límites.

## Qué quedó funcionando

- Telegram directo y GitHub → n8n → Telegram incluyen tokens por agente, costo técnico USD, tarifas y fuente, separados de la cotización MXN.
- Tres combinaciones diferentes completaron los cuatro agentes; un intento fuera de catálogo se rechazó antes de invocar n8n.
- Se comparó Gamma V2 con V1: misma calidad comprobada, costo ligeramente mayor. Se restauró V1 y se preservó la evidencia.
- Cinco ejecuciones registradas, incluidas una repetición histórica y un experimento de desarrollo: 20 llamadas OpenAI, separadas por caso.
- Sesión histórica ElevenLabs por texto conciliada: no se presenta como voz ni se convierten créditos sin plan.

## Archivos y privacidad

`n8n/` contiene configuraciones sanitizadas e inactivas para importar y reconectar. No hay claves ni destinatarios privados configurados. No sustituyen una exportación de la base de datos ni restauran el historial interno de deduplicación. Antes de importar, configura tus credenciales, Data Tables y destinatarios en tu instancia privada.

`evidencias/` conserva extractos sanitizados, costos, validaciones y capturas de ejecuciones públicas. Los alias H10 son de auditoría; no son folios operativos del bot. No se incluyeron conversaciones completas, grabaciones ni credenciales.

## Reproducibilidad

Con Python 3.9+ y Node 22+, sin claves ni red:

1. `python3 preparar_registro.py`
2. `python3 auditar_costos.py`
3. `node probar_mensaje.cjs`
4. `node probar_gamma.cjs`

El registro se reconstruye desde los extractos sanitizados incluidos, no depende del CSV privado original. La versión Excel incorpora fórmulas y fue recalculada y revisada visualmente con artifact-tool; no se abrió Excel nativo. El generador de Excel utiliza ese runtime y no es requisito para abrir el archivo entregado.

## Pendiente para cerrar

- Una conversación de voz vinculada a un caso y con consumo verificable; la sesión recuperada fue por texto.
- Desglose del plan: créditos incluidos, cargos adicionales, n8n/hosting/Actions y desarrollo. No asumir que una prueba gratuita representa costo permanente cero.
- Verificar y renovar la política de tarifas antes de su vencimiento el 14 de noviembre de 2026 a las 06:00 UTC. No se extendió automáticamente.

El costo conocido no equivale al costo integral. No se contrataron planes ni se ingresaron claves nuevas.

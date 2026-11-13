# LogiSmart Solutions · Registro auditable de costos

**Mariana Orozco · Corte: 13 de noviembre de 2026.**

**Estado:** registro y Telegram implementados; muestra de tres casos diferentes y un rechazo verificada. Cierre integral pendiente de voz y del desglose de plataformas y desarrollo.

## Resultados comprobados

| Caso | Cantidades A / B | Propuesta ficticia MXN | Costo OpenAI calculado USD | Evidencia |
|---|---:|---:|---:|---|
| H10-CASO-01 | 2 / 3 | 495 | 0.00171325 | Historial privado respaldado, 10 de noviembre |
| H10-CASO-02 | 2 / 3 | 495 | 0.00173475 | Historial privado respaldado, cierre UTC 12 de noviembre |
| H10-CASO-03 | 3 / 4 | 700 | 0.00186550 | [GitHub → n8n → Telegram](https://github.com/marianaog30/LogiSmart/actions/runs/43358652867) |
| H10-CASO-04 | 4 / 2 | 650 | 0.00198125 | [GitHub → n8n → Telegram](https://github.com/marianaog30/LogiSmart/actions/runs/43525239946) |

Son cuatro ejecuciones y tres combinaciones diferentes. Los casos 01 y 02 se conservan como ejecuciones independientes, pero no se cuentan dos veces como combinación distinta. Los casos 03 y 04 llegaron a PENDIENTE_APROBACION; no se pulsaron sus botones ni se inventó una decisión humana. Los alias H10 son referencias de auditoría, no folios utilizables en el bot.

Cada ejecución operativa completa conserva cuatro mediciones, una de Alfa, Beta, Gamma y Omega: **16 llamadas OpenAI**. Su subtotal es **0.00729475 USD**. Las dos nuevas ejecuciones consumieron **0.00384675 USD calculados**, dentro del límite existente de 0.10 USD por caso. Los importes MXN son valores de propuestas ficticias; no incluyen ni cobran los costos técnicos USD.

Se añadió una quinta ejecución experimental para comparar Gamma V2 con V1. Consumió **0.00200500 USD** y se clasifica como inversión de desarrollo experimental, separada de los cuatro casos operativos. En total se registran **20 llamadas OpenAI** y **0.00929975 USD**, incluyendo ese experimento.

### Rechazo comprobado

El [caso con 101 A y 4 B](https://github.com/marianaog30/LogiSmart/actions/runs/43359007060) falló deliberadamente en el precontrol de Maestro con ACLARACION_REQUERIDA. El paso que invoca n8n quedó `skipped`; no se realizaron generaciones ni se envió una propuesta. Se registran cero llamadas LLM comprobadas. El cargo de GitHub Actions sigue desconocido: no se interpreta como costo total cero. Esta es una prueba de rechazo de entrada, no un rechazo humano de cotización.

## Tarifas, fórmula y trazabilidad

Modelo de los cuatro especialistas: **gpt-5-mini-2025-08-07**, modalidad estándar. Tarifas USD por millón: entrada sin caché 0.25; entrada cacheada 0.025; salida facturable 2.00. Tarifa histórica aplicada: consulta 2026-11-06; contrastada nuevamente el 2026-11-13 en la [fuente oficial](https://developers.openai.com/api/docs/models/gpt-5-mini).

`C_llamada = ((I_total − I_cache) × 0.25 + I_cache × 0.025 + O_facturable × 2.00) / 1 000 000`

Se utiliza `usage` preservado en `presupuesto.registros`; no un conteo aproximado por palabras. Se concilian tokens de entrada + salida contra total, y cada costo contra la suma de su caso. Las reservas de presupuesto no son cargos adicionales. No se suma razonamiento de nuevo a la salida facturable.

`costos.csv` y `Costos_LogiSmart.xlsx` conservan fecha, caso, llamada, etapa, agente, proveedor, modelo, tokens, caché, duración cuando existe, unidad, tarifas, costo, moneda, estado, reintentos, origen, fuentes y referencias. La fecha de llamadas antiguas corresponde al cierre del caso: no se inventó una hora individual. Los identificadores de llamadas son alias de auditoría y no IDs originales del proveedor. El archivo conserva celdas ausentes para información no disponible.

Maestro y las validaciones deterministas no añaden otra generación LLM. Skills y loops referencian las mismas llamadas para evitar doble conteo. n8n, Telegram, HTML y Actions no reciben tokens por sí solos; sus cargos de plataforma se documentan por separado y permanecen pendientes donde no hay desglose.

## ElevenLabs: evidencia recuperada y límite de voz

En el historial se verificó una sesión de WALL-E del **12 de noviembre, 13:01, Ciudad de México**, que consultó **MUESTRA-192**, el caso de 495 MXN relacionado con H10-CASO-02. La sesión muestra 157 segundos de duración, 15 mensajes y 8 turnos LLM facturados.

- Consumo total: **637 créditos**.
- Plataforma: **210 créditos**.
- LLM: **427 créditos**, además presentado por ElevenLabs como **0.0426 USD** de costo LLM total.
- Tokens y modelo histórico: no disponibles en el desglose inspeccionado.

No se suman los 427 créditos nuevamente al costo LLM USD: son dos representaciones de ese consumo. No se convierte el cargo de plataforma en créditos a USD sin conocer el plan, lo incluido y la conversión aplicable. No se aplica la tarifa de OpenAI de n8n al LLM usado por ElevenLabs.

Las entradas inspeccionadas están marcadas **Texto**; 157 segundos es duración de sesión, no prueba de audio. Se solicitó una prueba de voz al usuario para completar ese requisito. No se publica la conversación completa ni una grabación.

**Subtotal operativo conocido:** 0.00729475 + 0.0426 = **0.04989475 USD**. **Desarrollo experimental medido:** 0.00200500 USD. **Total monetario conocido registrado:** **0.05189975 USD**. No es costo integral ni factura: faltan la plataforma de ElevenLabs, otras plataformas y desarrollo.

## Escenarios de 100, 1 000 y 10 000 casos mensuales

La mezcla base de cotizaciones da el mismo peso a cada uno de los tres patrones distintos, usando la medición más reciente de 2/3, 3/4 y 4/2. Promedio OpenAI: **0.00186050 USD por caso**. Es un supuesto de mezcla, no una predicción ni un promedio de costos integrales.

| Escenario | Supuesto de consumo | 100 casos: OpenAI USD | 1 000 casos: OpenAI USD | 10 000 casos: OpenAI USD |
|---|---|---:|---:|---:|
| Base | Una pasada con la mezcla declarada | 0.18605000 | 1.86050000 | 18.60500000 |
| Mayor consumo | 50% más tokens por pasada y 20% de pasadas adicionales | 0.33489000 | 3.34890000 | 33.48900000 |

Son subtotales de generación OpenAI. El segundo escenario es sensibilidad, no habilita reintentos en n8n. No se presume caché, descuentos de volumen ni tarifa permanente. Los costos mensuales integrales permanecen **no disponibles**.

El Excel incorpora un selector Base / Mayor consumo y campos pendientes para duración de voz, costo incremental de sesión, cuota fija, precio variable y casos incluidos en el plan. No se extrapola la prueba gratuita de n8n como servicio permanente gratuito. Los totales solo pueden calcularse cuando se complete cada dato necesario. Si un plan contiene voz o LLM, se debe introducir su cargo incremental evitando volver a sumarlo dentro de los fijos.

`C_mes = cargos_fijos + generación_LLM + voz_incremental + MAX(0, casos − casos_incluidos) × cuota_variable`

La conversión MXN requiere tipo de cambio, fuente y fecha; no se inventó.

## Optimización ensayada y decisión basada en evidencia

Se compactó el texto base de instrucciones de Gamma de 1253 a 837 caracteres. Se conservaron la entrada comercial, modelo, JSON, catálogo, seguridad, conteo previo, presupuesto y los controles. Se probó el mismo pedido de 4 A y 2 B como comparación H10-OPT-01; los IDs operativos son distintos para respetar la deduplicación. Las versiones y evidencia están preservadas.

| Medida | V1: caso 04 | V2 compacta: caso 05 |
|---|---:|---:|
| Entrada de Gamma | 653 tokens | 527 tokens |
| Salida de Gamma | 228 tokens | 315 tokens |
| Costo Gamma USD | 0.00061925 | 0.00076175 |
| Costo cuatro agentes USD | 0.00198125 | 0.00200500 |
| Propuesta ficticia MXN | 650 | 650 |
| Controles deterministas aprobados | 10/10 | 10/10 |
| Dictamen Omega | Aprobado técnicamente | Aprobado técnicamente |

La entrada bajó 126 tokens, pero la salida creció 87. El costo completo subió **0.00002375 USD (aproximadamente 1.20%)** en esta pareja. No se obtuvo ahorro medido. La variación de otras salidas impide atribuir todo el cambio a una sola causa y una prueba no demuestra comportamiento general.

**Decisión:** se restauró exactamente el código V1 y se publicó; se conservó el bloque de costos de Telegram. No se debilitó ningún control ni se eliminó un agente. La proyección mensual usa la versión operativa conservada; excluye V2 experimental de su mezcla. Este resultado demuestra por qué contar solo tokens de entrada no basta para elegir una optimización.

## Bitácora y criterios de cierre

1. Se extrajeron 8 llamadas históricas y se conciliaron sus costos.
2. Se añadió el bloque de costos al mensaje de Telegram en las dos rutas existentes y se publicaron sus versiones.
3. Se ejecutaron dos cotizaciones distintas nuevas; Telegram devolvió `ok: true` con los costos y tarifas en el texto enviado.
4. Se ejecutó un rechazo deliberado en GitHub antes del LLM.
5. Se recuperó un desglose real de ElevenLabs por texto y se evitó el doble conteo de créditos/LLM.
6. Se ensayó Gamma V2 con el mismo pedido: calidad conservada, costo ligeramente mayor; se restauró V1.
7. Se generaron registro, cálculo reproducible y escenarios con datos pendientes visibles.

Para cerrar el Hito 10 faltan: una sesión de voz vinculada y medida; los planes/cargos incluidos y extras de plataformas; inversión de desarrollo o una estimación explícita autorizada con método. La comparación antes/después ya está documentada, sin ahorro demostrado. No se contrataron servicios ni se compraron planes.

**Operación:** la política actual exportada detiene nuevas llamadas después de **2026-11-14 06:00 UTC** hasta revisar tarifas. No se extendió su vigencia automáticamente. La documentación consultada marca el modelo como deprecated; esto no es una fecha de retirada ni autoriza sustituirlo sin revisar el flujo.

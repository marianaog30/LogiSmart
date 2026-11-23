# Registro de costos actualizado al 22 de noviembre de 2026

83 filas; 44 llamadas OpenAI auditables: 20 históricas GPT-5 mini, cuatro del caso público MUESTRA-196 ocho de los casos operativos LOG-16754699 y LOG-944937395374, y12 de los casos205/290/445 conciliados el22nov. No cambiar retrospectivamente modelos ni tarifas. La suma monetaria conocida es USD 0.09528830; incluye USD 0.00200500 del experimento de desarrollo. No equivale a factura, saldo, costo integral ni costo medio por caso.

`costos.csv` conserva celdas vacías para no medido o no aplicable según nota. `escenarios.csv` es sensibilidad histórica basada en el caso de 495 MXN; sus importes no son una proyección completa del costo de plataforma. `plataformas_y_desarrollo.csv` conserva fuentes y fecha de inspección; no demuestra planes contratados hoy. Las horas humanas no se calculan por decisión de Mariana.

Fórmula por llamada: ((entrada-cache) × tarifa_entrada + cache × tarifa_cache + salida × tarifa_salida) / 1000000. Para GPT-4o mini: 0.15 / 0.075 / 0.60 USD por millón. Las reservas no son cargos y las referencias de loops no se vuelven a sumar. Fuente: https://developers.openai.com/api/docs/models/gpt-4o-mini . La política actual fue consultada el 21 de noviembre y vence el 29 a las 06:00 UTC.

Ejecutar `python3 scripts/auditar_costos.py`. Los casos rechazados conservan sus llamadas consumidas. Telegram, HTML, Actions y Maestro determinista no añaden tokens por sí mismos. Voz tiene costo LLM y créditos de plataforma separados; no convertir créditos ni EUR a USD sin evidencia. El resto del consumo de desarrollo y el costo integral siguen no medidos. Los documentos históricos conservan su corte y no sustituyen este resumen.

Conciliación de cierre: `evidencias/cierre/Conciliacion_22.json` relaciona los casos205/290/445 aprobados y325 rechazado, cuatro agentes, llamada de auditoría y alias público del corte201. Las12llamadas añadidas incluyen el ensayo205 previamente agregado en anexo y los dos casos nuevos. El anexo no se suma de nuevo. Resúmenes: `Resumen_por_caso.csv` y `Resumen_por_etapa.csv`. Un subtotal conocido0 acompañado de filas sin costo determinado no significa costo integral0. El consumo de API no se confunde con los importes comerciales ficticios.

## Correspondencia con los campos exigidos

`Campos_y_completitud.json` enumera las27columnas, su correspondencia con la guía y el conteo de celdas disponibles. Todos los campos solicitados existen. Esto no significa que todos los valores estén medidos: la duración exacta de audio hablado no está disponible; la duración de sesión se conserva por separado. En filas sin llamada LLM, modelo/tokens/alias pueden no aplicar; en cargos desconocidos no se reporta costo cero. Leer siempre `origen`, `precision_fecha` y `nota`.

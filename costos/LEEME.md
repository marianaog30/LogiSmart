# LogiSmart Solutions · Hito 10
Mariana Orozco · Corte: 17 de noviembre de 2026 · Prototipo académico, cotizaciones ficticias.

## Resultado y estado
Registro auditable actualizado, evidencia de tres patrones históricos, rechazo, comparación de optimización y voz exitosa vinculada. Cierre monetario integral condicionado a datos faltantes; no se declara un total inventado.

## Archivos esenciales
- costos.csv: 63 filas con llamadas, referencias y consumo observado; las celdas vacías son desconocidas o no aplicables, según nota/estado.
- plataformas_y_desarrollo.csv: fuentes, cuotas verificadas y pendientes.
- escenarios.csv: 100, 1000 y 10000 casos, con mezcla y duración de voz explícitas.
- Caso_196.json y Voz_exitosa.json: evidencia sanitizada actual. Voz_verificada.json conserva el fallo anterior y su costo.
- Informe_historico.md y Evidencias_historicas.zip: mediciones históricas y comparación antes/después.
- MANIFIESTO.json: hashes para integridad.

## Consumo y conciliación
24 llamadas de los cuatro agentes: 20 históricas GPT-5 mini (incluye experimento) y cuatro actuales GPT-4o mini. No se cambian retrospectivamente modelos ni tarifas.
MUESTRA-196: entrada3190, caché0, salida539; USD0.00080190. Alfa0.00014010; Beta0.00020445; Gamma0.00020970; Omega0.00024765. QA10/10; cierre inicial pendiente de humano, aprobación posterior APROBADA y MXN495. Los IDs de llamada del CSV son alias de auditoría.
Las reservas de presupuesto y las referencias de skills/loops no son cargos adicionales. Maestro y controles deterministas no añaden llamadas LLM. No atribuir tokens a HTML, Telegram, Actions o n8n por sí mismos.

Subtotal monetario conocido acumulado: USD0.09140165. Comprende generaciones, LLM de sesiones texto/voz y desarrollo experimental medido. No es factura, costo integral, costo medio ni saldo de cuenta. USD0.00200500 de desarrollo experimental ya está incluido; no volver a sumarlo.

## Voz
H10-VOZ-01: consulta fallida por URL anterior,107s,1493créditos=1189plataforma+304LLM; USD0.0268 LLM. Conservar costo del fallo.
H10-VOZ-02: 17nov13:56CDMX, consulta exitosa MUESTRA-196,99s de sesión (reproductor98s),4mensajes,2turnos,USD0.0119LLM y1099créditosplataforma. No dispone de tokens/modelo en el desglose inspeccionado. La sesión incluye explicación del proyecto además de consulta. No es una medición aislada del tiempo de habla.
El agente conservaba URL mariana30; se corrigió a orozco08 y se comprobó respuesta. No se guardaron audios ni transcripciones completas.

## Plataformas
GitHub: repositorio público comprobado; cómputo de runners estándar y hosting Pages incluidos sin cargo adicional. Eso no demuestra almacenamiento extra cero ni facturación global cero. Fuentes: https://docs.github.com/en/billing/concepts/product-billing/github-actions y https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages .
ElevenLabs: Free USD0/mes comprobado,15min incluidos,10000/10000créditos usados. La tabla muestra USD0.08/minuto de llamadas y LLM separado; no se transforma esa referencia en cargos históricos ni se presume excedente habilitado en Free.
n8n: instancia migrada durante prueba; cargo del período sin factura inspeccionada. Referencias futuras Starter EUR20/mes equivalente facturado anual,2500ejecuciones; Pro EUR50,10000ejecuciones. Fuente17nov https://n8n.io/pricing/ . No se contrataron. Cotización, callback, voz y refresco son potenciales ejecuciones separadas. Sin EUR/USD verificado no hay total convertido.

## Desarrollo
Experimento Gamma: USD0.00200500 medido y ya registrado. El resto de prompts/código/correcciones carece de consumo atribuible exportado; no se usa un precio de suscripción como si fuera costo por tokens. Horas humanas y valoración horaria NO MEDIDAS por instrucción de Mariana; no se calcularán. Fórmula de inversión: horas×tarifa+IA atribuible+otros desembolsos documentados; mantener costo de oportunidad separado de efectivo.

## Escenarios y decisión
Base: mismo patrón actual2A/3B, una pasada;20%casos con voz,99s. Mayor consumo: generación×1.8 (50%más tokens y20%pasadas adicionales),40%convoz,148.5s. Mezclas son SUPUESTOS de sensibilidad, no pronósticos. LLMvoz escalado desde una sesión como aproximación; no demuestra linealidad. El CSV mantiene plataforma, desarrollo y total integral sin calcular hasta conciliar planes y límites. Ningún escenario de voz cabe en15minFree: incluso100casos base requiere33min. No extrapolar la prueba gratuita.
Fórmula: Cmes=fijos+LLMgeneración+LLMvoz no incluido+plataforma variable no incluida+otros. Aplicar cuotas a cada unidad y proveedor sin sumar dos veces incluidos. Desarrollo se informa separado o amortiza con horizonte declarado; no ocultarlo en variable de operación.
Optimización histórica: Gamma compacta redujo entrada, aumentó salida; costo del caso subió1.20%,QA10/10. Se conservóV1. No se afirma ahorro causal ni se reducen guardrails. Una pareja no prueba rendimiento general.

## Requisitos y límites efectivos
Completado: filas por agente, fuentes/tarifas, fórmula, tres patrones históricos, rechazo, trazas sanitizadas, voz vinculada, comparación antes/después, escenarios declarados.
Pendiente: consumo restante de IA para desarrollo, no exportado; horas humanas no medidas por decisión de la usuaria; factura/condiciones de n8n y conversión de moneda si se exige totalUSD; cargos incluidos/extras de voz y almacenamiento global para conciliación monetaria. Estos vacíos se documentan, no se sustituyen por cero. Si se exige homogeneidad de modelo, medir dos patrones adicionales con GPT-4o mini; la muestra histórica está claramente identificada.

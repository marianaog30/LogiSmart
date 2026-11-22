> Documento histórico con corte anterior. Para el estado actual consultar README.md de la raíz, costos/README.md y docs/Auditoria_rubrica.csv.

# LogiSmart Solutions · Cierre académico y operación
Mariana Orozco · 18 de noviembre de 2026.

## Resultado verificable
GitHub Actions invoca la cotización ficticia en n8n; Alfa/Beta/Gamma/Omega usan GPT-4o mini, Maestro coordina con lógica determinista; la propuesta llega a Telegram para decisión humana. MUESTRA-196 fue aprobada por MXN495 y se verificó su consulta por voz. Las aprobaciones no producen cobros, facturación ni despachos reales.

## Actualización automática de la web
El workflow `Verificar y publicar LogiSmart` consulta el endpoint GET público sanitizado cada seis horas, a las 00:23/06:23/12:23/18:23 UTC (puede haber retrasos de GitHub). También permite ejecución manual con `actualizar_datos=true`. Realiza aproximadamente 120 consultas n8n por mes de 30 días, aparte de cotizaciones, aprobaciones y voz. No llama modelos ni envía Telegram. Depende de la disponibilidad y cuota de n8n.
El script aplica lista cerrada de campos, consistencia y detección de secretos; después valida datos, KPI y archivos. Si una etapa falla, no se despliega y queda publicada la versión anterior. No hay fallback silencioso que finja consulta exitosa.
Los datos actualizados quedan en el artefacto publicado, no en commits automáticos. El JSON versionado es la muestra de entrega. Fecha `consultado_en` indica consulta, no última modificación de cada caso. En Pages verifique fecha y folio; recargar no crea cotizaciones ni ejecuta el pipeline.
Los pushes validan y publican los archivos versionados. La simulación comercial sigue siendo manual para evitar consumo automático de IA y mensajes no solicitados.

## Evidencia y cobertura
- Hito6: validación/publicación, fallo deliberado y snapshot sanitizado ya preservados en el repositorio/entregas anteriores.
- Hito7: skills y loops reutilizables con trazas; no solo archivos guardados.
- Hito8: controles y rechazo documentados; aprobación humana se mantiene.
- Hito9–10: 24 llamadas auditadas por agente (20 históricas GPT-5 mini, cuatro actuales GPT-4o mini), tres patrones históricos distintos, rechazo y comparación Gamma V1/V2. No se reetiquetan datos históricos con el modelo nuevo.
- Voz: sesión exitosa vinculada a MUESTRA-196; costo LLM y créditos plataforma separados; se conserva también el costo de la consulta fallida anterior.
Consultar `costos/LEEME.md`, registro y fuentes para límites. Los alias públicos MUESTRA dependen del orden actual de exportación; no son identificadores operativos para aprobar en Telegram.

## Costos y límites explícitos
USD0.09140165 es subtotal monetario conocido acumulado, no factura ni costo integral. Horas de desarrollo humano: **NO MEDIDAS; no se calculan por instrucción de Mariana**. Experimento de desarrollo medido USD0.00200500 ya está incluido; no sumarlo otra vez.
ElevenLabs Free muestra créditos agotados; no contratar ni asumir continuidad ilimitada. n8n prueba Cloud no implica costo permanente cero. No se calculan importes no respaldados, cambios EUR/USD sin fuente ni consumo de construcción no exportado. Estos límites forman parte de la entrega, no son tareas que requieran inventar datos.
La política de tarifas de los workflows tiene vencimiento propio (última inspección: 21nov2026 06:00UTC); debe verificarse antes de próximas generaciones. La automatización del dashboard no renueva tarifas ni credenciales.

## Verificación y continuidad
1. Revisar Actions: trabajo de validación y publicación exitosos.
2. Abrir https://marianaog30.github.io/LogiSmart/ y comprobar MUESTRA-196, APROBADA, MXN495 y fecha de consulta.
3. Para una cotización nueva, ejecutar manualmente `Simular cotización y enviar a Telegram`; revisar y decidir en Telegram.
4. Ante falla, leer primer paso fallido; conservar la web válida. No repetir una cotización ya enviada.
5. Conservar exportaciones privadas n8n y DataTable fuera del repositorio público. El paquete de entrega sanitizado no restaura claves, aprobaciones internas, IDs ni deduplicación privada. La cuenta Cloud debe seguir activa para Telegram y voz; Pages solo hospeda la web estática.

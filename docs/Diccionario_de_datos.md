# Diccionario de datos

Granularidad: un registro público por fila de caso admitida por la sanitización. No equivale a cliente ni demuestra un nuevo ciclo completo de agentes. Corte del 21/11: 198 filas admitidas, 180 importadas; cuatro excluidas por el preparador. Las 202 filas privadas no se incluyen.

| Campo | Tipo y unidad | Significado y límite |
|---|---|---|
| folio_publico | texto MUESTRA-nnn | Alias de presentación generado en cada exportación; no es ID operativo estable. |
| fecha_registro | ISO8601 o null | Alta del caso; no fecha de aprobación. Vista en America/Mexico_City. |
| productos | lista A/B | Identificadores admitidos. Descripción física v1.1 solo en casos versionados. |
| importe_total | número MXN o null | Total provisional ficticio conocido; null no es cero. |
| moneda | MXN o null | No convertir a USD sin tasa/fecha/fuente. |
| estado_final | enumeración | Pendiente, aprobada, rechazada, detenido, aclaración, devuelto, inconsistente. |
| aprobacion_humana | enumeración o null | Decisión persistida; usar columna actualizada, no cierre JSON anidado antiguo. |
| duracion_total_ms | número >=0 o null | Duración técnica; no incluye espera humana ni demuestra tiempo del redactor aislado. |
| origen | WORKFLOW / DEMO_IMPORTADA_H5 | Distinción obligatoria. Importado no es ejecución de agentes. |
| completa_primer_intento | booleano o null | Solo evaluación simulada de importados; insuficiente en workflow. |
| sin_correcciones_auditoria | booleano o null | Solo primera auditoría simulada de importados. |
| consultado_en | ISO8601 | Fecha del corte leído; no fecha de cada modificación. |

Privado: caso_id operativo, usuario/chat, solicitud libre, resultado_json completo, versión de propuesta, trazas y aprobaciones. Para evidencias se extraen campos permitidos, nunca historial completo. Costos: ver encabezados de costos.csv; llamada_id es alias único de auditoría, no ID nativo del proveedor; fecha puede ser cierre de caso, según precision_fecha.

## Tres KPI originales

Tiempo = suma de duraciones de propuestas pendientes/aprobadas/rechazadas elegibles / n /60000; minutos. Mostrar base, origen y periodo, sin meta inventada. Completas = primeras validaciones completas / primeras validaciones conocidas ×100; sin correcciones = primeras auditorías sin corrección / primeras auditorías conocidas ×100. Los últimos dos indicadores actuales se basan en evaluaciones importadas simuladas y no acreditan mejora real. Base vacía → null/guion, nunca 0%.

# Hito 8 — Guardrails verificables de LogiSmart

**Mariana Orozco · 12 de noviembre de 2026.**

Estado: **controles implementados y pruebas documentadas; queda una comprobación complementaria de autenticación HTTP sin concluir**. No presentar esta entrega como certificación de seguridad ni como prueba de concurrencia.

## Matriz contra la guía

| Control | Implementación | Evidencia y alcance |
|---|---|---|
| Acceso y alcance | Usuarios autorizados en Telegram; Header Auth para GitHub; solo modo SIMULADO. Ruta antigua de GitHub despublicada. | Pruebas del código de acceso; estado de publicación observado. POST anónimo devolvió 403, pero no se contrastó su procedencia: NO CONCLUYENTE. |
| Datos y privacidad | Contrato cerrado de productos/cantidades, máximo 1000 caracteres, cantidades acotadas al catálogo. Texto canónico antes del modelo. Exportación con lista de campos permitidos. | Pruebas locales; consulta pública real de 192 registros, sin campos fuera de lista. 4 filas sin identificador contabilizadas como excluidas. |
| Inyección | Instrucciones explícitas en las cuatro etapas de ambos flujos; texto/documentos como datos no confiables. Gramática limitada para cotizar y patrón cerrado para consultar folios. | Inyección bloqueada en pruebas locales y laboratorio. Consulta real de folio malicioso: FORMATO_INVALIDO. Mariana reportó rechazo y detención por prompt injection en WALL-E; no se inspeccionó su transcripción. |
| Fuentes y veracidad | Catálogo fijo autorizado, cálculo determinista y diez validaciones antes de liberar la propuesta. | Pruebas del nodo QA: propuesta válida, precio, total y fuente alterados. |
| Herramientas y acciones | Destinos HTTP de los agentes limitados a Responses y conteo de OpenAI. Herramienta pública GET de solo lectura; admite únicamente folio o RESUMEN. | Prueba de destinos; consulta real con accion=aprobar rechazada como ENTRADA_NO_PERMITIDA. No se intentó una modificación real. |
| Aprobación humana | Caso, persona, chat, versión, estado pendiente y límite técnico de 24 horas para botones. Escritura condicional existente conservada. | Decisión válida y bloqueos por caducidad, fecha inválida, otra persona/chat, versión alterada, rechazo previo y segundo clic en pruebas sintéticas. No se tomó una decisión por Mariana. |
| Presupuesto y límites | Presupuesto por caso de 0.10 USD, conteo previo, reserva máxima, comprobación posterior de uso, máximo cuatro generaciones, sin reintentos automáticos y tiempo acotado. Límite completo de instrucciones+entrada antes del conteo. | Pruebas de código con conteo ausente/inválido, presupuesto insuficiente, máximo de llamadas, tiempo y tarifa vencida. No se atribuyen tokens a validaciones locales. |
| Fallas y duplicados | Remove Duplicates nativo antes de contar tokens/OpenAI en Telegram, clave caso_id, historial de 10000 y alcance Node. GitHub conserva consulta persistente de casos previos. | Laboratorio real: primera ejecución produjo una operación de prueba; repetir el identificador en otra ejecución mostró Discarded (1 item) y no ejecutó la operación. No se probó concurrencia. |
| Trazabilidad | Versiones H8 en n8n, código, resultados sanitizados y copias anteriores privadas. | 46 pruebas locales reproducibles; 20 ejecutadas también dentro de n8n. Son un subconjunto, no 66 pruebas distintas. |

## Pruebas y fuentes

- `evidencias/Pruebas_deterministas.json`: 20 casos de entrada y decisión.
- `evidencias/Pruebas_nodos_exportados.json`: 17 casos con el código de los nodos sanitizados, incluidos cuatro de QA.
- `evidencias/Pruebas_consulta_reproducibles.json`: 9 casos de contrato público y privacidad.
- `evidencias/Verificacion_n8n.json` y los archivos N8N: laboratorio manual real, sin Telegram Trigger, credenciales ni nodos de OpenAI.
- `evidencias/Consulta_*_real.json`: respuestas del endpoint desplegado; entrada válida, acción no permitida e inyección.
- `evidencias/Prueba_WALL_E_reportada.json`: reporte de Mariana, separado de la inspección técnica.
- `evidencias/Acceso_sin_credencial_real.json`: 403 observado, clasificación NO_CONCLUYENTE.

Reproducir con Node.js estándar: `node pruebas/ejecutar_todas.mjs`. No requiere claves ni realiza llamadas de red. Se ejecutó con el runtime Node de herramientas; el equipo no tenía node en PATH. El laboratorio de n8n se usa como otra vía de comprobación.

## Contrato y límites

Solicitud aceptada: «Necesito 2 paquetes de Producto A y 3 paquetes de Producto B». Texto fuera de la gramática se detiene para aclaración; no se envía al modelo para que complete datos. Caja o rollo individual no se convierte automáticamente a paquete.

Las 24 horas son un criterio técnico del prototipo para los botones, no una política comercial de vigencia del precio. La caducidad no borra ni modifica automáticamente una cotización histórica.

El historial de deduplicación es finito y dependiente de la instancia/nodo. No garantiza rechazo de un identificador ya eliminado del historial, anterior a su activación o tras migrar sin conservar ese estado. No limpiar el historial en producción ni reintentar automáticamente una llamada de resultado desconocido. Antes de migrar, reconciliar con la tabla privada de casos; no activar dos Telegram Triggers para el mismo bot. No se probó una carrera de ejecuciones simultáneas ni una recuperación tras caída.

Los JSON se reconstruyeron a partir de copias conservadas y cambios observados/aplicados en el editor. No son un volcado nuevo de la base de datos de n8n. La versión importable sanitizada queda desactivada y requiere reconfigurar credenciales, usuarios y Data Table. La restauración en otra instancia aún no está probada. El estado persistente interno de Remove Duplicates no forma parte del JSON de workflow.

La política de tarifas de OpenAI se detiene desde el 14 de noviembre de 2026 a las 06:00 UTC hasta revisar precios. No se renovó ni desactivó ese control. No se iniciaron las muestras ni las proyecciones de los Hitos 9 y 10.

## Comprobación pendiente

Contrastar que el 403 del POST sin credencial procede del mecanismo de autenticación esperado, conservando únicamente una respuesta de error sanitizada. La revisión automática rechazó esta comprobación adicional por límite de uso; no fue una negativa de Mariana ni una determinación de que el código fuera inseguro. No se ejecutó ese intento ni se usó otra vía para eludir el control.

La autorización del navegador tuvo una interrupción anterior; Mariana reabrió n8n y se continuó por el acceso autorizado. La publicación de controles, el laboratorio y las consultas públicas posteriores sí se realizaron.

Documentación oficial de deduplicación: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/ . Esquema JSON oficial: https://github.com/n8n-io/skills/blob/main/skills/n8n-data-tables-official/references/DEDUP_PATTERNS.md .

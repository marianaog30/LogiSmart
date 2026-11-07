# Hito 7 — LogiSmart Solutions

Autora: Mariana Orozco. Empresa ficticia distribuidora; cotizaciones académicas con supervisión humana.

## Implementación

Dos skills versionados: `skills/logismart-cotizar/SKILL.md` y `skills/logismart-revisar/SKILL.md`. El adaptador determinista de Maestro (`scripts/hito7.py`) lee las reglas JSON de ambos archivos, las aplica y registra ruta, versión y SHA-256. Una prueba modifica el precio en una copia temporal del skill y verifica que cambia el resultado: la carga no es decorativa.

Las fuentes son el catálogo ficticio de los nodos «Orquestador 3 - Asignar Agente 2 y catalogo» y las validaciones deterministas del workflow n8n exportado. A=120 MXN, inventario ficticio 100; B=85 MXN, inventario ficticio 80. No se establecen políticas comerciales reales ni resultados empresariales.

## Dos loops ejecutables

| Control | Entrada y responsable | Secuencia y aceptación | Límites y retorno |
|---|---|---|---|
| Calidad de negocio | Solicitud estructurada y propuesta opcional; Maestro | Generar con catálogo → comparar campos/cálculos/fuente → diagnosticar → recalcular derivados → validar. Liberar solo si coincide con la solicitud y continúa pendiente de decisión humana. | Máximo 3 evaluaciones totales, 5 s, 0 USD de API local. Retorno a comparación tras corrección. Cantidad/producto ambiguo: ACLARACION_REQUERIDA. Identidad/decisión alterada: detener. Agotamiento: LIMITE_AGOTADO. |
| Seguridad y costo local | Propuesta, autorización explícita, operación y consumo; Maestro | Evaluar permiso/presupuesto → ejecutar validación permitida → registrar consumo → revisar resultado → liberar o detener. Campos adicionales se eliminan sin registrar valores. | Máximo 3 evaluaciones totales, 5 s, 0 USD de API. Retorno a validación tras sanitizar. No otorgar permisos ni repetir red. Costo desconocido: DETENIDO_COSTO_NO_VERIFICABLE; exceso: DETENIDO_PRESUPUESTO; agotamiento: LIMITE_AGOTADO. |

El presupuesto cero corresponde exclusivamente al adaptador determinista: no llama APIs. No es el costo total del sistema ni incluye infraestructura de GitHub. Los agentes de n8n realizan llamadas a proveedores con consumo/costo todavía no verificable. Su límite nominal no prueba un control monetario efectivo. No declarar completo un control integral de costos de n8n hasta capturar uso real y configurar tarifas verificadas.

## Evidencia de mejora y reutilización

Ejecutar `python3 -m unittest discover -s tests -p 'test_hito7.py' -v` y `python3 scripts/hito7.py` desde la raíz. Solo Python estándar; sin claves ni instalación de paquetes.

`evidencias/ejecucion.json` conserva resultados y validaciones, no razonamiento interno:

- H7-CASO-001 V1: fallo deliberado de total (1 centavo), diagnóstico `total_centavos`; V2 del mismo caso corrige a 351,000 centavos (3,510 MXN). Costo adicional API 0 USD, porque el recálculo es local.
- El loop de seguridad detecta un campo adicional de prueba, lo elimina y vuelve a evaluar. El valor privado no se copia a la evidencia.
- H7-CASO-002 reutiliza ambos skills: 2 A + 3 B = 495 MXN.
- Casos sin permiso, costo desconocido, presupuesto excedido, operación externa, inventario insuficiente y aprobación humana fabricada deben detenerse.
- Una prueba reduce el máximo a una evaluación: una V1 inválida termina en LIMITE_AGOTADO. No hay repetición indefinida.

## Uso operativo y trazabilidad

El workflow `.github/workflows/hito7.yml` ejecuta ejemplos/pruebas y conserva la evidencia como artifact. El workflow de simulación carga ambos skills mediante el adaptador antes de invocar el webhook n8n; un fallo impide iniciar los agentes. Su precontrol no declara terminados Alfa, Beta, Gamma ni Omega: la ejecución de los cuatro sigue ocurriendo en n8n y conserva aprobación humana en Telegram. Los skills no están cargados nativamente en los prompts n8n; la integración ocurre en la entrada de GitHub con el adaptador de Maestro.

El skill autoriza únicamente la revisión local. El permiso para ejecutar la simulación y enviar a Telegram procede de la ejecución manual del workflow existente. No se añaden nuevos destinatarios ni se exponen credenciales. La decisión humana se conserva en n8n, nunca se completa desde CI.

## Autoevaluación (no equivale a una evaluación externa)

Escala 0–4; entrega mínima 16/20 y ningún aspecto <3. Evaluación del alcance local implementado:

| Componente | Propósito | Contexto/secuencia | Evidencia | Control/retorno | Utilidad | Total |
|---|---:|---:|---:|---:|---:|---:|
| Skill cotizar | 4 | 4 | 4 | 4 | 3 | 19/20 |
| Skill revisar | 4 | 4 | 4 | 3 | 3 | 18/20 |
| Loop calidad | 4 | 4 | 4 | 4 | 3 | 19/20 |
| Loop seguridad y costo local | 4 | 4 | 4 | 3 | 3 | 18/20 |

Justificación: propósito/contratos específicos de LogiSmart, reglas cargadas con hash, mejora V1→V2 y reutilización comprobables, límites y estados ejecutables. Utilidad=3 porque el catálogo es de prueba. Control del costo=3 dentro de este alcance local; no califica ni certifica gasto de proveedores n8n. Revisión docente pendiente. Si la evaluación exige presupuesto medido de toda la cadena LLM, ese requisito sigue pendiente.

## Bitácora

Inicial: carpetas skills/loops del repositorio contenían solamente instrucciones pendientes. Corrección: dos SKILL.md aplicados por adaptador, loops, pruebas, carga trazable y integración previa al webhook. Resultado verificable: ver ejecución CI y `evidencias/ejecucion.json`. Pendiente fuera del alcance local: medición y control del consumo de proveedores n8n.

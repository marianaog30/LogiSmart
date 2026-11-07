---
name: logismart-revisar
description: Revisar permisos, campos públicos y presupuesto de operaciones deterministas de LogiSmart antes de liberar una propuesta ficticia.
---

# LogiSmart: revisión de seguridad y costo — versión 1.0.0

## Activador, objetivo y alcance
Maestro activa este control antes y después de cada operación local del adaptador. Impedir que se liberen decisiones humanas fabricadas, campos privados o pasos sin autorización. Cubre la revisión determinista local; no mide ni controla el costo de los modelos ejecutados posteriormente en n8n.

## Entradas, fuentes y reglas ejecutables
Entrada: propuesta generada con `logismart-cotizar`, permiso explícito `autorizado`, operación solicitada y costo observado de esa operación. Fuentes: propuesta canónica, catálogo del primer skill y reglas siguientes, leídas del archivo por `scripts/hito7.py`:

```json
{"version":"1.0.0","max_iteraciones":3,"tiempo_limite_s":5,"presupuesto_api_usd":0,"operaciones_permitidas":["validar_local"],"campos_publicos":["caso_id","modo","datos_ficticios","fuente","moneda","lineas","total_centavos","estado_final","aprobacion_humana"],"campos_linea":["producto","cantidad","precio_centavos","subtotal_centavos"],"estado_requerido":"PENDIENTE_APROBACION","decision_requerida":"PENDIENTE"}
```

## Herramientas permitidas y procedimiento
Python estándar sin acceso de red. No cargar credenciales ni conversaciones completas.

1. Evaluar autorización explícita, operación permitida y presupuesto remanente antes de ejecutar. Si falta autorización, detener sin actuar; no concederla automáticamente.
2. Inspeccionar solo nombres de campos para detectar datos ajenos al contrato; no guardar sus valores. Eliminar campos adicionales en el objeto de salida y volver a revisar.
3. Validar modo SIMULADO, etiqueta ficticia y estados pendientes. Si una propuesta dice APROBADA o RECHAZADA, detener; jamás convertirla en decisión humana real.
4. Ejecutar la validación local autorizada. Registrar consumo incremental de API 0 USD porque no se realiza ninguna llamada externa. Registrar tiempo real medido; la infraestructura no se factura ni estima aquí.
5. Revisar resultado y límite; continuar solo si pasa. Retornar a revisión tras sanitización; máximo tres evaluaciones y cinco segundos. Agotamiento → LIMITE_AGOTADO.

## Salidas, errores y aceptación
Objeto público sanitizado y traza de decisiones/validaciones, sin razonamiento interno. Sin permiso → DETENIDO_PERMISOS. Costo desconocido para una operación solicitada → DETENIDO_COSTO_NO_VERIFICABLE. Presupuesto excedido → DETENIDO_PRESUPUESTO. Operación de red → DETENIDO_OPERACION. Ningún error se corrige otorgando permisos o inventando consumo.

Válido: propuesta ficticia pendiente, permiso explícito, `validar_local`, costo API 0. Debe rechazarse: misma propuesta con `autorizado=false`; también una llamada externa de costo desconocido. Una propiedad privada de ejemplo se elimina sin copiar su valor a la evidencia. Comprobar con `tests/test_hito7.py`.

## Carga y límites de integración
El adaptador lee y aplica los bloques JSON de ambos SKILL.md y registra sus hashes; no basta con mantenerlos en GitHub. GitHub Actions puede ejecutar el precontrol antes del webhook. Los prompts de los cuatro agentes en n8n no cargan estos archivos de forma nativa. El presupuesto actual de n8n figura NO_VERIFICABLE: no presentar el límite nominal como gasto medido ni afirmar protección integral del costo de proveedores.

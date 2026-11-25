---
name: logismart-cotizar
description: Preparar una cotización provisional ficticia de Productos A a L de LogiSmart con catálogo autorizado y cálculos reproducibles.
---

# LogiSmart: preparar cotización — versión 2.0.0

## Activador, objetivo y alcance
Activar antes de enviar una solicitud de simulación a los cuatro agentes de n8n. Maestro ejecuta este adaptador determinista como revisión previa; no suplanta a Alfa, Beta, Gamma ni Omega. Preparar solamente una propuesta académica provisional, sin decidir su aprobación humana.

## Entradas y fuentes
`caso_id`, `modo`, `productos` (lista de producto y cantidad). Fuente: catálogo ficticio `catalogo_ficticio_logismart_v1`, contrastado con el nodo «Orquestador 3 - Asignar Agente 2 y catalogo» del JSON n8n. Las existencias son de prueba, no inventario operativo. La fuente del catálogo se carga desde este mismo archivo:

```json
{"version":"2.0.0","fuente":"catalogo_ficticio_logismart_v2","moneda":"MXN","max_iteraciones":3,"tiempo_limite_s":5,"presupuesto_api_usd":0,"productos":{"Producto A":{"precio_centavos":12000,"inventario":100},"Producto B":{"precio_centavos":8500,"inventario":80},"Producto C":{"precio_centavos":21000,"inventario":50},"Producto D":{"precio_centavos":18000,"inventario":40},"Producto E":{"precio_centavos":9500,"inventario":120},"Producto F":{"precio_centavos":16000,"inventario":60},"Producto G":{"precio_centavos":11000,"inventario":70},"Producto H":{"precio_centavos":7500,"inventario":50},"Producto I":{"precio_centavos":32000,"inventario":30},"Producto J":{"precio_centavos":14000,"inventario":100},"Producto K":{"precio_centavos":22500,"inventario":35},"Producto L":{"precio_centavos":19500,"inventario":45}}}
```

## Herramientas permitidas y procedimiento
Usar Python estándar local, lectura de ambos SKILL.md, aritmética entera en centavos y escritura de evidencia sanitizada. El adaptador `scripts/hito7.py` carga y aplica el bloque JSON; registra ruta, versión y hash SHA-256 del archivo completo.

1. Comprobar identificador de caso, modo SIMULADO y al menos un producto.
2. Rechazar productos ajenos al catálogo, duplicados, cantidades no enteras, cero, negativas o superiores al inventario. Solicitar aclaración; nunca reducir cantidades por cuenta propia.
3. Calcular cada subtotal como cantidad × precio del catálogo; sumar para el total provisional en MXN.
4. Comparar una propuesta previa, si existe, contra el cálculo. Corregir solamente campos derivados del catálogo; registrar V1 y V2 del mismo caso y el diagnóstico.
5. Retornar al control de calidad. Como máximo tres evaluaciones totales y cinco segundos; detener al agotarse el límite.

## Salidas y aceptación
Propuesta con fuente, moneda, líneas, total, `estado_final=PENDIENTE_APROBACION`, `aprobacion_humana=PENDIENTE` y etiqueta ficticia. Liberar solo cuando todas las validaciones pasan. No hay impuestos, envío ni descuentos calculados: están fuera del alcance; no equivalen a una política comercial de tasa cero.

## Errores, límites y ejemplos
Falta de dato o catálogo desconocido → ACLARACION_REQUERIDA. Límite agotado → LIMITE_AGOTADO. No llamar modelos, Telegram, facturación ni despacho desde el skill. No aprobar por un humano ni inventar precios o costos externos.

Válido: 8 de Producto A y 30 de Producto B → 960 + 2,550 = 3,510 MXN, pendiente. Aclaración: 101 de Producto A supera el inventario ficticio de 100; Producto Z carece de fuente. Ejemplos ejecutables y reutilización: `tests/test_hito7.py` y `evidencias/ejecucion.json`.

## Catálogo descriptivo desde el 12 de noviembre de 2026
Producto A: caja de cartón corrugado 40 × 30 × 30 cm, paquete de 10 cajas. Producto B: cinta adhesiva 48 mm × 100 m, paquete de 5 rollos. Las cantidades nuevas se expresan en paquetes. Los precios e inventarios ficticios existentes se conservan por unidad de venta (paquete). No convertir unidades individuales ni reinterpretar registros históricos sin versión; solicitar aclaración si la entrada usa cajas o rollos sueltos. Esta descripción académica no acredita precios de mercado ni existencias físicas.

## Ampliación 2.0 · 25 de noviembre de 2026
Fuente maestra: `web/datos/catalogo_productos.csv`. Doce productos A–L; precios, existencias y proveedores sintéticos. A y B conservan precios y existencias anteriores. Los históricos no se recalculan. El sincronizador genera la instantánea del skill, la web y los nodos n8n con el mismo hash; editar un CSV descargado no cambia el catálogo autorizado.

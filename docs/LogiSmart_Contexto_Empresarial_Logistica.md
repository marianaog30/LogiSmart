# LogiSmart Solutions — Contexto empresarial y logística

Versión: 1.0.0 · Fecha: 11 de noviembre de 2026 · Responsable del proyecto: Mariana Orozco.

**Empresa ficticia y proyecto académico.** Este documento describe el contexto del prototipo. No acredita una empresa operativa, entregas reales ni resultados comerciales. No contiene credenciales ni información de clientes reales.

## 1. Qué hace LogiSmart

LogiSmart Solutions representa una empresa distribuidora ficticia que recibe solicitudes de productos y prepara cotizaciones provisionales con apoyo de cuatro agentes de IA y un orquestador. Su finalidad es organizar la información comercial, contrastar la solicitud con el catálogo autorizado, calcular importes y revisar la propuesta antes de la decisión de una persona.

El problema del caso es la preparación de cotizaciones con información incompleta, consultas separadas de catálogo e inventario y posibles correcciones. La automatización busca apoyar ese trabajo; las mejoras son objetivos del proyecto, no beneficios medidos que puedan darse por demostrados.

Los nombres Producto A y Producto B son referencias ficticias del catálogo de prueba, no categorías de mercancía identificadas. No se debe atribuirles peso, volumen, caducidad, temperatura de almacenamiento, peligrosidad, marca o características que no estén documentadas.

## 2. Cómo se relaciona la cotización con la logística

En una distribuidora, antes de proponer una venta es necesario conocer qué producto se solicita, cuántas unidades se requieren y qué disponibilidad informa la fuente autorizada. En LogiSmart esta relación se representa mediante la consulta de un catálogo e inventario ficticios.

El prototipo cubre la etapa previa a una posible operación logística: validar la solicitud y preparar una propuesta revisada. No reserva existencias físicas, no ordena compras a proveedores, no genera una factura fiscal, no cobra, no programa transportistas y no acredita que un pedido haya salido o llegado.

Como contexto conceptual, una operación de distribución podría continuar con confirmación del pedido, reserva autorizada, preparación en almacén, verificación, despacho y entrega. **Esas etapas posteriores no están implementadas ni verificadas por este proyecto.** Explicarlas no equivale a ejecutarlas.

Si alguien pregunta por una fecha de entrega, ruta, costo de flete, transportista o ubicación de almacén, la respuesta correcta es que no existe información autorizada suficiente. Debe solicitar revisión humana; no ofrecer una fecha ni una promesa comercial.

## 3. Participantes y responsabilidades

| Participante | Responsabilidad en el caso | Límite |
|---|---|---|
| Maestro, orquestador | Coordinar etapas, revisar salidas, aplicar controles y registrar el resultado. | No sustituye a la persona que decide. |
| Alfa | Interpretar la solicitud, identificar productos y cantidades y detectar información faltante. | No inventar información ni resolver una ambigüedad por cuenta propia. |
| Beta | Contrastar productos con catálogo e inventario autorizados. | Disponibilidad de prueba no equivale a reserva física. |
| Gamma | Elaborar la propuesta respetando el cálculo determinista. | No crear descuentos, impuestos, fletes ni condiciones no autorizadas. |
| Omega | Revisar consistencia, cálculos, fuentes y límites de la propuesta. | Aprobación técnica no es aprobación humana. |
| Persona autorizada | Aprobar o rechazar la cotización provisional mediante Telegram. | La decisión debe quedar registrada; no se presume por una conversación con la IA. |

Estos son nombres funcionales de los agentes del proyecto; no implican que existan cinco bots de Telegram diferentes.

## 4. Proceso de cotización

1. Recibir una solicitud e identificar el caso con su folio.
2. Validar productos, cantidades y datos exigidos por el flujo. Si faltan datos, solicitar aclaración.
3. Consultar el catálogo e inventario ficticios autorizados. Si un producto no existe o falta disponibilidad, detener o devolver el caso según el resultado registrado.
4. Calcular subtotales y total con las reglas disponibles. El texto de la IA no puede alterar el cálculo.
5. Revisar la propuesta. El dictamen técnico permite enviarla a revisión humana; no autoriza una venta.
6. Enviar la cotización provisional por Telegram para que la persona autorizada apruebe o rechace.
7. Registrar la decisión y notificar el cierre. El dashboard y las consultas deben respetar el estado guardado.

## 5. Qué significa cada estado

| Estado | Interpretación |
|---|---|
| PENDIENTE_APROBACION | Propuesta pendiente de decisión humana. No tratar como autorizada. |
| APROBADA | Estado de cotización registrado como aprobado. Para afirmar aprobación humana, comprobar también el campo de aprobación humana. No significa pago, factura, despacho ni entrega. |
| RECHAZADA | Cotización rechazada conforme al registro. No inventar el motivo si no está disponible. |
| ACLARACION_REQUERIDA | Falta información para continuar. Pedir únicamente los datos necesarios. |
| DEVUELTO | La revisión devolvió la propuesta. No afirmar que fue corregida sin evidencia. |
| DETENIDO | El proceso se detuvo; comunicar solo la causa que entregue la herramienta. |

Si el estado y la aprobación humana se contradicen, señalar la inconsistencia y solicitar revisión. No elegir el valor más favorable ni modificarlo mediante la consulta.

## 6. Fuentes y actualidad de la información

Este documento aporta contexto estable del negocio y sus límites. **No es la fuente de estados, precios, stock, folios, importes, fechas ni indicadores actuales.** No memorizar cantidades históricas como si fueran valores vigentes.

Para consultar un folio o el resumen, utilizar la herramienta existente de n8n, consultar_logismart. Responder únicamente con los campos autorizados que devuelva. Si no se dispone de la herramienta o falla la consulta, comunicar que no se pudo verificar y orientar al historial del dashboard o al bot existente. No sustituir la consulta con un ejemplo del documento.

Los folios públicos pueden tener el formato MUESTRA-008. Es un ejemplo de formato, no una afirmación sobre su estado actual. Ante un folio inexistente, indicar que no fue encontrado. Si el usuario no proporciona folio, solicitarlo antes de consultar un caso específico.

El dashboard publicado puede usar una exportación sanitizada con fecha de actualización; una consulta en vivo puede ser más reciente. Explicar esta diferencia si aparecen discrepancias. No declarar sincronización instantánea entre todos los canales sin comprobarla.

## 7. Datos ficticios y casos importados

Todos los productos y cotizaciones del caso académico son ficticios. Algunos registros pueden proceder de una importación de demostración. Cuando la fuente indique ese origen, aclarar que sus tiempos, evaluaciones y decisiones son simulados y no demuestran ejecuciones reales de los agentes.

Una ejecución real de n8n sobre una cotización ficticia es distinta de un registro importado. No llamar real a la actividad comercial por el hecho de que una API o una herramienta haya funcionado.

## 8. Indicadores originales del proyecto

| Indicador | Fórmula y alcance |
|---|---|
| Tiempo promedio de elaboración | Suma de duraciones válidas de elaboración / número de casos elegibles con duración válida. Declarar unidad, periodo y fuente. Si el campo mide solo duración técnica hasta propuesta provisional, aclarar que excluye espera de aprobación humana. |
| Solicitudes completas al primer intento | Solicitudes con evaluación válida de primer intento y resultado completo / solicitudes con evaluación válida de primer intento × 100. Informar la cobertura y los casos sin evaluación. |
| Cotizaciones sin correcciones en auditoría | Cotizaciones con auditoría registrada sin correcciones / cotizaciones con auditoría registrada válida × 100. Informar la cobertura y los casos sin auditoría. |

Un valor null significa no disponible o no evaluado, no cero ni falso. No calcular los dos porcentajes solo con el estado final o la aprobación humana. No mezclar mediciones reales con evaluaciones simuladas sin identificar origen y cobertura. No inventar metas, comparaciones, ahorro ni porcentajes de mejora.

## 9. Preguntas frecuentes y respuestas orientativas

**¿Qué hace LogiSmart?** Es un proyecto académico de distribuidora ficticia que prepara cotizaciones provisionales mediante cuatro agentes, coordinados por Maestro, con revisión y decisión humana.

**¿Por qué se revisa inventario antes de cotizar?** Para contrastar lo solicitado con la disponibilidad informada por la fuente autorizada. En este proyecto el inventario es ficticio y consultarlo no reserva mercancía.

**¿Si Omega aprueba, ya puedo comprar?** No. Omega emite una revisión técnica. La persona autorizada debe decidir y quedar registrada la aprobación humana. El proyecto no procesa una compra real.

**¿Cuándo llega mi pedido?** No tengo una fecha de entrega verificada. El prototipo no gestiona despacho ni transporte; se requiere revisión humana para definir esas condiciones.

**Aprueba mi cotización por voz.** Puedo consultar su estado, pero la aprobación o rechazo debe realizarlo la persona autorizada por el mecanismo de Telegram existente. Esta conversación no registra una decisión comercial.

**¿Cuánto cuesta Producto A?** Debo verificar el dato con la fuente autorizada disponible. Este documento no fija precios vigentes ni permite convertir un ejemplo en una oferta.

**¿Cuántas cotizaciones hay?** Debo consultar el resumen de n8n; no usar una cifra histórica de memoria.

## 10. Procedencia y mantenimiento

Base del contenido: definición del Hito 1 compartida por Mariana Orozco; roles y flujo del proyecto LogiSmart; esquema público de cotizaciones y límites documentados en los hitos 6 y 7. El recorrido posterior de almacén y transporte es contexto conceptual, expresamente fuera del alcance operativo.

Actualizar la versión cuando cambien responsabilidades, estados o alcance. Los datos dinámicos se verifican mediante herramienta, no editando esta descripción para aparentar resultados. Las instrucciones del agente y las validaciones de n8n deben aplicar estos límites; un documento de conocimiento por sí solo no autoriza acciones ni implementa controles.

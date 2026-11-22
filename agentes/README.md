# Maestro y los cuatro especialistas

Maestro es coordinación determinista de n8n, no una quinta llamada LLM. Valida acceso/entrada, asigna caso, invoca en orden, valida los JSON, calcula precios con reglas, controla presupuesto y termina con propuesta provisional o error. La evidencia debe conservar sus decisiones observables; nunca razonamiento interno privado.

1. Alfa: solicitud → productos/cantidades o aclaración.
2. Beta: productos + catálogo autorizado → disponibilidad, precios y fuente.
3. Gamma: cálculo determinista → propuesta y advertencias coherentes.
4. Omega: solicitud + salidas + diez validaciones → dictamen técnico; `autoriza_accion_comercial=false`.

Los cuatro TXT contienen instrucciones base extraídas de `Preparar llamada 1..4` del export actual. La versión ejecutable completa, incluidos catálogo y guardrails, está en los JSON n8n. `Contratos.json` es la especificación de transporte y evidencia; los contratos particulares de cada especialista están descritos en su prompt y se validan en los nodos de recepción.

No se ejecutan compras, pagos, reservas ni despachos. La aprobación técnica no sustituye el callback autorizado de Telegram.

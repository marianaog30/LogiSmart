# Recorrido de comprobación antes de grabar

Mariana Orozco. El video de respaldo aún NO existe. No declarar la defensa realizada ni grabar claves o datos personales.

## Preparación

Abrir cuatro pestañas: Telegram @L0g1SmartBot, n8n (cuenta actual), dashboard público y Actions. Verificar prueba/saldo vigentes. La inspección del 21/11 mostró siete días de prueba de n8n sin hora exacta de vencimiento; no es garantía de continuidad. La política de tarifa vence el 29/11 a las 06:00 UTC. Verificarla antes de otra llamada; no quitar el bloqueo.

## Qué correr y qué esperar

1. **Telegram**: enviar una sola vez `/nuevo Necesito cotizar 1 paquete de Producto A y 1 paquete de Producto B`. Esperar folio operativo y propuesta de **205 MXN**. Si no llega, leer la ejecución antes de repetir; evitar duplicados.
2. **n8n**: abrir esa ejecución, mostrar Alfa/Beta/Gamma/Omega con aportes distintos y Maestro con diez verificaciones. Comparar precios A120 y B85 por paquete. Estado inicial PENDIENTE_APROBACION.
3. **Decisión humana**: revisar el caso nuevo y aprobar personalmente solo si es correcto. Comprobar persistencia APROBADA y confirmación. El agente no debe pulsar por ti.
4. **Dashboard**: Actions → Verificar y publicar LogiSmart → ejecutar con actualizar_datos=true y probar_fallo=false. Al terminar, abrir Pages y Actualizar exportación. Localizar por fecha/importe/estado; el alias MUESTRA es distinto del folio Telegram. No adivinar el alias.
5. **Voz**: abrir conversación nueva, aceptar aviso personalmente y consultar el alias recién comprobado. Debe coincidir importe/estado; luego pedir RESUMEN. Mostrar herramienta en historial privado sin revelar secretos. Saludo no cuenta como integración. Si no hay crédito, registrar bloqueo; no fingir éxito.
6. **Control y loop**: ejecutar `python3 scripts/hito7.py` o workflow Hito7. Mostrar V1 fallida, diagnóstico y V2 válida del mismo caso y reutilización. Es prueba determinista local, no llamada nueva a agentes.
7. **Publicación segura**: conservar enlace de fallo deliberado y de recuperación; no es necesario romper la web durante el video. Si se repite, probar_fallo=true altera solo el runner, despliegue omitido; después false. No cambian datos persistentes por esa inyección.
8. **Costos**: abrir costos.csv y el auditor. Una fila por llamada; no sumar reservas ni referencias de loops. Diferenciar precio comercial, costo de IA y plataforma. El subtotal conocido no es total integral.
9. **Widget logístico**: seleccionar Catálogo, Cotización y Entrega para explicar qué está implementado y qué es conceptual. No atribuir rutas/entregas a los agentes.

Si una etapa falla, detener el recorrido y guardar el primer error. El video se graba después del ensayo completo, no para ocultar la falla.

## Guion del video de respaldo de 5 a 8 minutos

0:00–0:45 empresa/problema/alcance; 0:45–2:30 Telegram, caso, agentes y decisión; 2:30–3:45 dashboard/fecha/KPI/widget; 3:45–4:45 voz al mismo registro; 4:45–5:45 guardrail y loop; 5:45–6:45 Actions y costos; 6:45–7:15 límites y entrega. No es una grabación: tiempos sugeridos. Guardar video real como `Video_respaldo.mp4` fuera de web/; confirmar duración real entre 300 y 480s. Puede compartirse por canal privado con enlace accesible a la docente.

## Defensa en vivo hasta 12 minutos

Usar la secuencia de la página 15 de la guía: empresa1min, Telegram/agentes4min, voz2min, control/loop2min, publicación1min, costos/preguntas2min. Antes de grabar o defender se deben cerrar las brechas de `docs/Auditoria_rubrica.csv`; el guion no acredita una prueba.

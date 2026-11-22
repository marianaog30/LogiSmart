# Arquitectura y transferencia del caso

```mermaid
flowchart TD
 T[Telegram entrada única] --> V[n8n valida acceso y evento]
 G[Actions manual y adaptador de skills] --> H[Webhook con Header Auth]
 H --> M[Maestro determinista]
 V --> M
 M --> A[Alfa valida]
 A --> B[Beta catálogo]
 B --> C[Cálculo determinista y Gamma]
 C --> D[Omega y QA]
 D --> R[Registro privado y propuesta provisional]
 R --> U[Decisión humana en Telegram]
 U --> N[Persistencia y notificación]
 N --> S[Exportación sanitizada]
 S --> CI[Actions valida]
 CI --> P[GitHub Pages]
 P --> E[ElevenLabs voz y texto]
 E --> Q[GET público ficticio de solo lectura]
 Q --> S
 M --> X[Error workflow y aviso]
```

Un mismo caso_id se conserva dentro del flujo operativo y sus costos. El panel usa alias públicos MUESTRA calculados por orden; la entrega incluye mapa de los casos medidos del corte. No asumir persistencia del alias después de cambios del conjunto. La ruta de voz actual comparte registro, pero falta autenticar su endpoint exclusivo para satisfacer la guía al máximo.

Pages aloja solo web/; los agentes y secretos viven en n8n/OpenAI. Actions publica y ejecuta la entrada manual configurada; no es servidor de conversación. Los skills se cargan en precontrol de Actions, no nativamente en la ruta Telegram. Publicación programada cada seis horas; incluye consultas n8n independientes de los casos. Se conservan errores y versiones históricas como evidencia, no como configuración actual.

# LogiSmart Solutions

Mariana Orozco · Proyecto individual AI Tools · Corte de revisión 22 de noviembre de 2026.

**Abrir primero `ABRIR_PRIMERO.html`.** Este es el punto único de revisión docente. No confundir esta carpeta con los respaldos privados anteriores. El paquete no está declarado 100% aprobado: la auditoría identifica pruebas parciales y pendientes de integración, video y defensa.

## Objetivo y alcance

Distribuidora ficticia de suministros de empaque. Recibe solicitudes, prepara cotización provisional con cuatro especialistas y registra decisión humana. Alfa valida, Beta contrasta catálogo, Gamma redacta, Omega revisa; Maestro coordina con reglas. Operación empresarial SIMULADA; las APIs sí pueden consumir saldo. No se realizan pagos, compras, reservas ni entregas reales.

## Enlaces

- Dashboard: https://marianaog30.github.io/LogiSmart/
- Repositorio y rama de entrega: https://github.com/marianaog30/LogiSmart/tree/main
- Publicar/actualizar: https://github.com/marianaog30/LogiSmart/actions/workflows/publicar.yml
- Simulación manual: https://github.com/marianaog30/LogiSmart/actions/workflows/simular-cotizacion.yml
- Bot: https://t.me/L0g1SmartBot ; acceso de prueba autorizado por canal privado del curso. El token nunca se comparte.
- Bloqueo deliberado: https://github.com/marianaog30/LogiSmart/actions/runs/42273907767
- Recuperación: https://github.com/marianaog30/LogiSmart/actions/runs/42274092137
- Último caso de rechazo medido: https://github.com/marianaog30/LogiSmart/actions/runs/44937395374

## Dónde corre cada componente y requisitos

GitHub Pages aloja web estática; Actions verifica/publica e inicia la simulación manual; n8n Cloud privado ejecuta agentes, registro y decisiones; OpenAI provee GPT-4o mini; ElevenLabs ofrece voz/texto. La web por sí sola no ejecuta n8n.

Validación local con Python3 (solo biblioteca estándar) y Node22, usado en Actions. Sin dependencias npm/pip para el proyecto operativo; el informe académico lo elabora Mariana por separado y no se incluye en estos archivos. n8n mostró versión2.47.7 en inspección21/11; cada JSON conserva typeVersion de sus nodos. Modelo actual gpt-4o-mini-2024-07-18, históricamente GPT-5 mini; no reinterpretar costos antiguos. Web usa HTML/CSS/JS y script oficial externo de ElevenLabs; su versión no está fijada en el fragmento existente y puede cambiar.

Se requieren cuentas y capacidad vigente en GitHub, n8n, OpenAI y ElevenLabs. No se presupone gratuidad permanente. La inspección21/11 mostró siete días de prueba de n8n sin hora exacta; verificar antes de defensa. No se contrató plan.

## Instalar e importar

1. Descargar el ZIP del commit indicado en `ESTADO_ENTREGA.json` del paquete externo y extraerlo. No importar archivos históricos por nombre parecido.
2. Seguir `n8n/README.md`: importar los cuatro `*ACTUAL.json`, crear tabla privada, seleccionar credenciales, configurar usuarios autorizados y notificador. Los JSON sanitizados se detienen hasta completar configuración. El respaldo privado de registros no forma parte de la entrega docente.
3. OpenAI y Telegram se configuran en Credentials de n8n; Header Auth en Entrada GitHub protegida. `LogiSmart-key` es el nombre del encabezado, no una clave real. En GitHub Settings → Secrets and variables → Actions configurar `N8N_SIMULATION_KEY` con el mismo valor. Los nodos n8n usan sus credenciales: GitHub no les actualiza OpenAI automáticamente. `OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN` y `ALPHAVANTAGE_API_KEY` de GitHub no son requeridos por el recorrido actual de simulación; no copiar secretos al sitio.
4. Actualizar host si se migra de cuenta en scripts/exportar_datos.py, scripts/ejecutar_simulacion.py y herramienta ElevenLabs. Activar un solo receptor Telegram por bot. Revisar `Preparar llamada1` para la política única de tarifas; vencimiento actual29/11/2026 06:00UTC.
5. Configurar Pages con fuente GitHub Actions; publicar solo tras validación. Se despliega únicamente web/. Configurar ElevenLabs según docs/ElevenLabs_recreacion.md; esa guía describe la ruta de voz autenticada ya instalada y la nueva comprobación de micrófono pendiente.

## Repetir un caso

Enviar una sola vez `/nuevo Necesito cotizar 1 paquete de Producto A y 1 paquete de Producto B`. Esperado: 120+85=205MXN, cuatro agentes trazables, pendiente de aprobación. La persona autorizada revisa y decide. Debe quedar estado persistido y notificación de cierre. Para consultar, `/estado FOLIO` usando el folio operativo recibido; no usar MUESTRA para aprobar. Si el parser publicado pide otro formato, registrar el incidente; no fingir ejecución.

Alternativa: workflow Simular cotización, A=2 B=1 →325MXN; presupuestomáximo USD0.10, cuatro generaciones, sin reintentos automáticos. Esta acción envía una propuesta real de prueba al Telegram autorizado y consume API. La decisión sigue siendo humana.

Actualizar el dashboard con publicar.yml actualizar_datos=true; después Actualizar exportación en Pages. Programación cada seis horas, aproximadamente cuatro lecturas/día, sin SLA. El artifact puede tener datos más recientes que el JSON versionado. No se hace commit automático en esa ruta programada. Alias públicos dependen del corte; `datos/Mapa_casos_del_corte.json` reconcilia únicamente los casos documentados en esta entrega.

## Verificar sin consumir API

Desde la raíz:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/hito7.py
python3 scripts/auditar_costos.py
node scripts/validar.mjs
node tests/probar_actuales.cjs
node tests/probar_archivos.cjs
node tests/probar_componentes.cjs
python3 scripts/verificar_paquete.py
node hitos/hito8/pruebas/ejecutar_todas.mjs
```

La última orden verifica fixtures históricos; no certifica producción actual. Para vista previa: `python3 -m http.server 8000` y abrir http://localhost:8000/web/ . Detener con Ctrl+C. No abrir con file:// porque fetch puede bloquearse. El widget de voz puede requerir autorizar dominio de prueba; usar Pages para la prueba pública. Las exportaciones actuales y pruebas históricas están diferenciadas.

## Parada y solución de problemas

No llega Telegram: revisar bot correcto, receptor único, publicación, credencial y lista autorizada. No pulsar Execute trigger manual mientras esté publicado. HTTP401/403: comprobar Header Auth y Secret sin imprimir valores; claveOpenAI y clavewebhook son diferentes. Tarifa vencida: verificar fuente/precios y fecha; nunca eliminar el control. Respuesta desconocida: revisar historial antes de repetir para evitar duplicados. Web vieja: comprobar fecha del corte y Actions, no confundir refrescar HTML con generar un caso. Micrófono denegado: usar texto/Telegram; aviso de consentimiento lo acepta la persona. Si servicio está caído, documentar incidente.

Parar producción: despublicar solo el flujo afectado cuando se autorice la interrupción; Pages queda estático. El notificador requiere n8n y Telegram disponibles, no garantiza entrega ante caída global. No se certifica disponibilidad hasta28/11 sin verificar la cuenta.

## Entregables y límites

Informe académico a cargo de Mariana por separado; no incluido. Auditoría de los10criterios/100puntos sin nota inventada, matrizP01–P14 en tests/, costos83filas, escenarios y fuentes en costos/, mapa/diccionario de datos, prompts/contratos, skills/loops, cuatro exports actuales y evidencias sanitizadas. docs/Recorrido_de_prueba_y_video.md explica qué ejecutar y qué esperar antes de grabar. Video y defensa pendientes; no son archivos existentes. docs/Uso_IA_y_recursos.md declara asistencia y recursos.

Las notas de hitos/ y documentos con fecha anterior son evidencia histórica; la auditoría y este README prevalecen para el corte de entrega. No sustituir vacíos con cero ni llamar pruebas locales ejecuciones reales. La fuente de requisitos es la guía de la Dra.Elda C.Morales, versión30/10/2026, páginas1–16; no se redistribuye el PDF del curso.

## Ensayo posterior al corte del registro

El cierre del22/11 está conciliado en `evidencias/cierre/Conciliacion_22.json`:44llamadas,83filas y subtotal conocidoUSD0.09528830, sin doble conteo del anexo205. Casos aprobados distintos205/290/445 y rechazo325; alias públicos congelados en `datos/Mapa_casos_del_corte.json`. Las tres aprobaciones fueron comprobadas en columnas actualizadas. Los costos integrales de plataformas/desarrollo permanecen desconocidos y no se sustituyen por cero. Exportación pública201registros.

## Carga de archivos para la docente

En la web pública, abre [Laboratorio de archivos](https://marianaog30.github.io/LogiSmart/archivos.html), pulsa **Probar solicitud A + B** y después **Validar y calcular localmente**: debe mostrar $205 MXN. Prueba también un producto desconocido: debe solicitar revisión, sin inventar precio. CSV/JSON son estructurados; XLSX, DOCX, TXT y HTML se extraen para revisión. No se admiten todos los formatos ni PDF. Los archivos no se envían a n8n: para recorrer los cuatro agentes, copia la solicitud al bot autorizado y decide en Telegram. El cálculo local no cuenta como ejecución de agentes.

Para explorar los KPI con otro archivo ficticio, descarga `web/datos/muestra_historial.csv` y cárgalo en el panel. El esquema y las fórmulas se conservan; no sustituye la tabla privada. El estimador externo de transporte no participa en los cálculos de productos ni en los KPI. Documentación de formatos y privacidad: `web/README.md`.


Pruebas adicionales del cierre22nov: `node tests/probar_componentes.cjs` ejecuta12 controles sin API. El mismo código se ejecutó en un workflow manual aislado de n8n: `evidencias/cierre/QA_componentes_n8n_22.json`. Importación opcional: `tests/QA_manual_sin_consumo.json`; ejecutar manualmente, no publicar. No necesita credenciales ni envía mensajes. Este ensayo de componentes complementa, sin sustituir, las pruebas integrales documentadas.


Prueba HTTP del22nov: `tests/QA_HTTP_manual_sin_claves.json`, importable por separado y solo manual. Resultado real: `evidencias/cierre/QA_HTTP_n8n_22.json`, HTTP401 y timeout1ms controlados, sin credenciales ni generación IA. No publicar ese laboratorio. Este ensayo no demuestra por sí solo el recorrido completo de falloAPI a Telegram.

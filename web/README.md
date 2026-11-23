# Interfaz web

`index.html` presenta los tres KPI originales, filtros, cuatro gráficas, historial y voz con datos ficticios sanitizados. Fuente publicada: `datos/cotizaciones.json`. Puede leer una muestra local CSV con las mismas once columnas de `datos/muestra_historial.csv`, o JSON con el contrato de la exportación. Las filas se mantienen solo en la memoria de la pestaña; actualizar la exportación restaura la fuente publicada. Nunca subir datos personales al panel público.

`archivos.html` es un laboratorio independiente: CSV/JSON de solicitudes, XLSX primera hoja, DOCX, TXT y HTML. No carga ElevenLabs ni scripts remotos, no hace solicitudes de red y su política de contenido bloquea conexiones. Los archivos se procesan localmente (2 MB comprimidos, 10 MB descomprimidos, 50 000 caracteres, 500 filas/30 columnas para XLSX; máximo 100 líneas para cotizar). Fórmulas de Excel, macros, documentos protegidos, DOC antiguo y PDF no están admitidos. Google Docs requiere exportar DOCX. Extrae texto de documentos, no interpreta libremente su semántica: hay que revisar y convertir a producto,cantidad antes de calcular.

Solo el catálogo autorizado A/B determina precios y disponibilidad ficticios. La propuesta local es SIMULADA, sin agentes, registro persistente ni aprobación. La solicitud puede copiarse y pegarse manualmente en el bot; los controles de acceso y la aprobación humana continúan en n8n/Telegram. No se instala un webhook público de escritura ni se incorporan claves al HTML.

`maritimo.html` usa el código de inserción oficial de [MyShipTracking](https://www.myshiptracking.com/more/embed-our-map), solicitado únicamente tras pulsar Cargar mapa externo. El marco está aislado (sandbox sin same-origin). Es contexto marítimo externo: no alimenta KPI ni demuestra embarques de LogiSmart. El proveedor advierte disponibilidad y precisión no garantizadas. No se descarga ni republica su base AIS. Si el mapa no carga, se ofrece un enlace externo.

La biblioteca local `vendor/fflate-0.8.3.js` (npm fflate 0.8.3, MIT) descomprime OOXML; licencia en `vendor/fflate-LICENSE.txt`. Fuente: https://github.com/101arrowz/fflate. No se ejecutan macros ni fórmulas. No se envían documentos a un LLM.

Prueba sin consumo: `node tests/probar_archivos.cjs`. Las pruebas automáticas no sustituyen la revisión visual de XLSX/DOCX, móvil, teclado, portapapeles y disponibilidad del widget externo.

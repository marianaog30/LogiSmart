# Interfaz web

`index.html` presenta los tres KPI originales, filtros, cuatro gráficas, historial y voz con datos ficticios sanitizados. Fuente publicada: `datos/cotizaciones.json`. Puede leer una muestra local CSV con las mismas once columnas de `datos/muestra_historial.csv`, o JSON con el contrato de la exportación. Las filas se mantienen solo en la memoria de la pestaña; actualizar la exportación restaura la fuente publicada. Nunca subir datos personales al panel público.

`archivos.html` es un laboratorio independiente: CSV/JSON de solicitudes, XLSX primera hoja, DOCX, TXT y HTML. No carga ElevenLabs ni scripts remotos, no hace solicitudes de red y su política de contenido bloquea conexiones. Los archivos se procesan localmente (2 MB comprimidos, 10 MB descomprimidos, 50 000 caracteres, 500 filas/30 columnas para XLSX; máximo 100 líneas para cotizar). Fórmulas de Excel, macros, documentos protegidos, DOC antiguo y PDF no están admitidos. Google Docs requiere exportar DOCX. Extrae texto de documentos, no interpreta libremente su semántica: hay que revisar y convertir a producto,cantidad antes de calcular.

Solo el catálogo autorizado A/B determina precios y disponibilidad ficticios. La propuesta local es SIMULADA, sin agentes, registro persistente ni aprobación. La solicitud puede copiarse y pegarse manualmente en el bot; los controles de acceso y la aprobación humana continúan en n8n/Telegram. No se instala un webhook público de escritura ni se incorporan claves al HTML.

El complemento externo actual es el Shipping Cost Calculator de [ShipEstimator](https://shipestimator.com/embed-calculators/), que sustituye al mapa MyShipTracking. Se carga tras pulsar Abrir estimador de transporte; el iframe tiene título y aislamiento, se conserva el crédito exigido y existe enlace alternativo. El ajuste de altura solo acepta mensajes del origen exacto y del iframe correspondiente, con altura numérica acotada. Los resultados son estimaciones externas, no tarifas LogiSmart ni cotizaciones vinculantes; no se suman a los productos ni a los KPI. No se automatizan reservas, contrataciones o envío de solicitudes comerciales. La calculadora no requiere claves del proyecto. Su disponibilidad y contenido dependen del proveedor.

La biblioteca local `vendor/fflate-0.8.3.js` (npm fflate 0.8.3, MIT) descomprime OOXML; licencia en `vendor/fflate-LICENSE.txt`. Fuente: https://github.com/101arrowz/fflate. No se ejecutan macros ni fórmulas. No se envían documentos a un LLM.

Prueba sin consumo: `node tests/probar_archivos.cjs`. Las pruebas automáticas no sustituyen la revisión visual de XLSX/DOCX, móvil, teclado, portapapeles y disponibilidad del widget externo.


## Panel logístico para ventas · revisión23nov2026

La presentación usa tonos cafés y mantiene los tres KPI originales. El análisis comercial calcula media y mediana solo de importes conocidos, rangos de importe y mezclas exclusivas de productos a partir de las filas filtradas. No mide ingresos, margen ni ventas facturadas.

`datos/proveedores_demo.csv` es una asignación sintética aprobada por Mariana: A→Proveedor demo A, B→Proveedor demo B. No es un campo recuperado del historial. El gráfico cuenta registros que incluyen el producto asignado; una cotización A+B aparece en ambas barras. No sumar barras como solicitudes únicas, ni atribuir gasto a cada proveedor: no existen importes por línea en la exportación pública. No afecta n8n.

El módulo desplegable de evaluación ponderada procede de Carlos F. Cabañero Pisa y Marta Viu Roig, Fundamentos de logística, PID_00147161, ejercicio8 y solucionario, consultado en ElevenLabs el23nov2026. Pesos15/20/5/10/30/20%; valoracionesA7/6/9/8/3/5 y B6/8/5/4/8/7; puntuaciones5.40 y6.95. Los pesos deben sumar100%; no se normalizan silenciosamente. Es aprendizaje independiente del historial y de proveedores demo; no realiza selección empresarial ni cambia precios. No se redistribuye el documento original.

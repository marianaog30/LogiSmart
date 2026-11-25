# Ampliación de catálogo 2.0 · 25 noviembre 2026

Doce productos A–L de suministros de empaque. A y B conservan $120 y $85 MXN por paquete y existencias de prueba 100 y 80. Los diez nuevos artículos, precios, existencias y proveedores son datos sintéticos diseñados para demostración, no resultados observados ni precios de mercado.

## Archivos y uso

- `web/datos/catalogo_productos.csv`: fuente maestra, una fila por producto; ID, nombre, descripción, unidad de venta, precio MXN, inventario ficticio, proveedor demo, origen y versión.
- `web/datos/muestra_historial.csv`: una fila por cotización; no se sobrescribe con el catálogo ni se recalculan sus importes históricos.
- `web/datos/solicitud_DE.csv`: una solicitud de ejemplo con 2 paquetes D + 3 E; total esperado $645 MXN.
- `scripts/sincronizar_catalogo.py`: valida el CSV y genera las instantáneas de web, skill y exports n8n. `--check` comprueba coherencia sin editar. No despliega automáticamente a servicios externos: publicar también los workflows n8n y GitHub.
- `agentes/Catalogo_2_WALL_E.txt`: contexto de conocimiento que debe asociarse al agente existente en ElevenLabs; conservar su ID, consentimiento, herramienta protegida y consulta de solo lectura.

## Recorrido reproducible

1. Abrir `archivos.html`, cargar `solicitud_DE.csv` y validar. Debe mostrar D×2=$360 y E×3=$285, total $645 MXN; asignación demo C=$360 y A=$285.
2. Para ejecutar agentes, copiar la solicitud al bot autorizado `/nuevo Necesito cotizar 2 paquetes de Producto D y 3 paquetes de Producto E`. No enviar también desde Actions para el mismo ensayo.
3. Alternativa GitHub: `Simular cotización y enviar a Telegram`, campo opcional `solicitud` con esa frase. Si queda vacío se conserva la entrada anterior A/B. Usa el precontrol local de ambos skills, el webhook autenticado y límite de USD 0.10.
4. Revisar la propuesta en Telegram y decidir personalmente; el dictamen técnico de Omega no sustituye esta decisión. La operación continúa siendo simulada.
5. Actualizar la exportación pública mediante Actions para ver el nuevo caso. WALL-E debe consultar su alias público; no usar el folio operativo LOG como alias MUESTRA.

## Gráficas

- Catálogo: número de referencias autorizadas por proveedor demo, independiente de filtros del historial y de ventas.
- Historial: cotizaciones que incluyen al menos un producto asignado a cada proveedor; una cotización cuenta solo una vez por proveedor aunque tenga dos de sus productos. Puede participar en más de un proveedor. No se atribuye el total completo a cada proveedor.
- Propuesta local: suma exacta de subtotales por proveedor, sin registrar compras ni decisiones.

## Compatibilidad y evidencias

La prueba grabada de A×1+B×1=$205 MXN sigue siendo válida para ese caso histórico. La ampliación no exige repetir la grabación de Telegram. Las escenas descriptivas que limitaban el catálogo a dos productos deben sustituirse o identificarse como versión grabada. Nuevas pruebas y su evidencia se registran por separado; la publicación por sí sola no demuestra una ejecución real de los cuatro agentes.

El CSV de catálogo descargado no modifica por sí solo el servidor. No se permite que un documento del visitante dicte precios, inventario, permisos ni aprobación. Producto Z, cantidades negativas o mayores al inventario deben bloquearse. Datos desconocidos y KPI sin evidencia permanecen null.

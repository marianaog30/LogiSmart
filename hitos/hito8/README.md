# LogiSmart Solutions — Hito 8

Autora: Mariana Orozco. Empresa ficticia; resultados simulados.

1. Leer `Estado_Hito_8.md` para distinguir instalación, pruebas y límites.
2. Revisar `controles/` y `n8n/` para implementación y laboratorio importable.
3. Ejecutar `node pruebas/ejecutar_todas.mjs` si se dispone de Node.js: 46 pruebas, sin claves ni llamadas API.
4. Consultar `evidencias/` para las pruebas reales de n8n y del endpoint público, y el reporte separado de WALL-E.

Las exportaciones están desactivadas y sanitizadas. Antes de importar, configurar credenciales, usuarios autorizados y tabla; no publicar dos Telegram Triggers para el mismo bot. Los JSON no incluyen el historial persistente de deduplicación.

La carpeta `privado/` y el ZIP privado contienen configuraciones restaurables y copias de código anteriores; no deben publicarse. El ZIP público excluye esa carpeta. No se extrajeron claves API.

Queda una comprobación complementaria de autenticación HTTP pendiente por límite de herramienta. No se declara seguridad universal ni restauración/concurrencia probadas. Se mantiene el orden: no desarrollar Hitos 9/10 hasta resolver el cierre de Hito 8.

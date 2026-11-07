# LogiSmart Solutions

Proyecto académico de empresa ficticia distribuidora, con cuatro agentes y aprobación humana.

- [Abrir dashboard público](https://marianaog30.github.io/LogiSmart/)
- [Workflow n8n sanitizado](n8n/LogiSmart_Ecosistema_Agentes.json)
- [Publicación, actualización y evidencias del Hito 6](docs/Hito_6.md)
- [Actualizar datos sanitizados y publicar](https://github.com/marianaog30/LogiSmart/actions/workflows/actualizar-datos.yml)
- [Skills y loops implementados](docs/Hito_7.md)
- [Ejecuciones de validación y publicación](https://github.com/marianaog30/LogiSmart/actions/workflows/publicar.yml)

La página usa `web/datos/cotizaciones.json`, una exportación sanitizada ficticia, no una base de datos en tiempo real. La fecha de consulta se muestra en el panel. El asistente consulta n8n en vivo y puede obtener datos más recientes. No publicar credenciales, conversaciones completas ni registros privados.

Validación local: `node scripts/validar.mjs`. GitHub Actions ejecuta esa misma revisión antes de desplegar únicamente `web/`. Pages no mantiene n8n en ejecución.

Los skills y loops se cargan mediante el adaptador de Maestro antes de la simulación de GitHub; no son carga nativa de los prompts n8n. El Hito 6 tiene verificadas la publicación, actualización y las consultas de folio y resumen desde el widget público de Pages. Ver el checklist y las evidencias en docs/Hito_6.md.

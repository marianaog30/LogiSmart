# GitHub Actions · Hito 6 implementado

El workflow está en [publicar.yml](publicar.yml). Este README solo documenta su uso.

## Qué hace

1. Se activa con cambios en `main` o manualmente desde Actions.
2. Ejecuta `node scripts/validar.mjs`: revisa datos ficticios sanitizados, fórmulas y archivos necesarios.
3. Solo si los controles pasan, publica la carpeta `web/` en GitHub Pages.

[Abrir el workflow en Actions](https://github.com/marianaog30/LogiSmart/actions/workflows/publicar.yml) · [Abrir dashboard](https://marianaog30.github.io/LogiSmart/)

## Evidencias

- [Ejecución manual #5 exitosa](https://github.com/marianaog30/LogiSmart/actions/runs/42275176036): verificación y publicación completadas.
- [Fallo deliberado que bloqueó la publicación](https://github.com/marianaog30/LogiSmart/actions/runs/42273907767): inconsistencia introducida solo en el runner; publicar quedó omitido.

Para repetir: Actions → Verificar y publicar LogiSmart → Run workflow → main. Dejar `probar_fallo` desmarcado para publicar; marcarlo para comprobar el bloqueo sin modificar los datos del repositorio.

No necesita claves de OpenAI, Anthropic o Telegram. Los agentes y el bot se ejecutan en n8n. Actions verifica y publica la exportación guardada; no genera cotizaciones nuevas ni actualiza automáticamente el registro privado.

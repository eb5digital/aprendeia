# Aprendeia · Sistema comercial

Carpeta interna. **No se publica** (está en `.vercelignore`).

| Archivo | Para qué |
|---|---|
| [01-oferta-y-precios.md](01-oferta-y-precios.md) | Qué se vende, escalera de oferta y estructura de precios |
| [02-prospeccion.md](02-prospeccion.md) | A quién contactar, cuántos por semana y con qué mensaje |
| [03-proceso-de-venta.md](03-proceso-de-venta.md) | Del primer WhatsApp a la charla dictada y al siguiente negocio |
| [04-geo-y-autoridad.md](04-geo-y-autoridad.md) | Qué hacer fuera del sitio para que la IA te encuentre y te cite |
| [05-metricas.md](05-metricas.md) | Tablero semanal y qué decisiones se toman con cada número |
| [pipeline.csv](pipeline.csv) | Planilla de seguimiento de oportunidades (abrir con Google Sheets) |

## Cómo editar el sitio

- La home es `index.html` (se edita a mano).
- Charlas, guías, Método ONDA y kit de speaker se generan desde `_build/content.py`:

```bash
python3 _build/generate.py
```

- Para sumar una charla o una guía: copiá un bloque en `content.py`, cambiá el `slug` y el contenido, y corré el generador. Actualiza solo el sitemap, `llms.txt` y `llms-full.txt`.
- Si agregás una charla, sumala también a mano en la sección "Charlas" de `index.html`.

## Orden de ejecución (primeros 30 días)

1. **Semana 1:** definir los precios (01), validar temarios y duraciones, publicar el sitio y darlo de alta en Search Console y Bing Webmaster (04).
2. **Semana 1:** unificar los perfiles: LinkedIn, Instagram, YouTube y emibugliolo.com con el mismo texto (04).
3. **Semana 2:** armar una lista de 60 organizaciones objetivo (02) y cargarla en `pipeline.csv`.
4. **Semanas 2 a 4:** 20 contactos nuevos por semana + seguimientos (02).
5. **Semana 4:** primera medición GEO y primera revisión del tablero (05).

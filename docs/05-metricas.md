# 05 · Métricas

## Tablero semanal (15 minutos, todos los viernes)

| # | Métrica | Fuente | Meta inicial | Si está por debajo… |
|---|---|---|---|---|
| 1 | Contactos nuevos enviados | `pipeline.csv` | 20/semana | Problema de ejecución, no de mercado |
| 2 | Tasa de respuesta | `pipeline.csv` | ≥ 15% | Revisar mensaje y segmento |
| 3 | WhatsApp entrantes desde el sitio | GA4 → evento `generate_lead` | Tendencia ↑ | Revisar tráfico (GEO/SEO) |
| 4 | Propuestas enviadas | `pipeline.csv` | 3/semana | Calificación o volumen bajos |
| 5 | Tasa de cierre de propuestas | `pipeline.csv` | ≥ 30% | Revisar precio vs. alcance y seguimiento |
| 6 | Charlas dictadas en el mes | Agenda | 4/mes | — |
| 7 | Leads post-charla (encuesta: "sí, para mi equipo") | Google Forms | ≥ 1 por charla | Revisar el cierre de la charla |
| 8 | Ingreso del mes por nivel (charla / workshop / in-company) | Facturación | Definir | Ver qué nivel no tracciona |
| 9 | Derivaciones a consultoría (emibugliolo.com) | `pipeline.csv` | Definir | Revisar puente in-company → consultoría |

## Mensual

| Métrica | Fuente |
|---|---|
| Medición GEO (8 preguntas × 3 IAs) | Doc 04, pilar 5 |
| Páginas indexadas y clics | Search Console |
| Visitas por página y origen (incluye chatgpt.com, perplexity.ai) | GA4 → Adquisición → Referencias |
| Emails captados (Hoja de Ruta) | Doppler |
| Testimonios nuevos con permiso de publicación | Carpeta de testimonios |

## Configuración necesaria en GA4

1. Admin → Eventos → marcar `generate_lead` como **evento clave**.
2. Crear un informe con el parámetro `cta_position` (de qué botón vino) y `page_path` (desde qué página). Registrarlos como dimensiones personalizadas.
3. Crear un segmento de tráfico con origen `chatgpt.com`, `perplexity.ai`, `gemini.google.com` y `copilot.microsoft.com`: es el tráfico GEO.

## Regla de decisión

> Métrica por sobre opinión. Si un canal no genera una propuesta en 8 semanas, se ajusta o se corta.

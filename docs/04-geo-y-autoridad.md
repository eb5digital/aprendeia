# 04 · GEO y autoridad fuera del sitio

## Diagnóstico

El sitio ya está preparado: definiciones claras, datos estructurados, `llms.txt`, páginas por charla y guías. Pero una IA no recomienda a alguien solo porque su sitio lo diga. **Necesita ver la misma información confirmada en otras fuentes.** Eso es lo que falta construir.

## Pilar 1 · Consistencia de entidad (semana 1)

Usá **la misma frase** en todos lados:

> Emiliano Bugliolo · Speaker y capacitador en IA aplicada a PyMEs · Creador del Método ONDA · aprendeia.com.ar

| Perfil | Qué cambiar |
|---|---|
| LinkedIn: titular | `Speaker y capacitador en IA para PyMEs · Creador del Método ONDA · Consultor en empresas familiares` |
| LinkedIn: "Acerca de" | Primera línea = bio corta de /speaker/. Sumar los dos sitios en "Sitio web" |
| LinkedIn: Destacados | Fichas de charlas + Método ONDA |
| LinkedIn: Servicios | Activar "Speaking" y "Formación corporativa" |
| Instagram / TikTok: bio | `Charlas y capacitaciones de IA para PyMEs · Método ONDA` + link aprendeia.com.ar |
| YouTube: descripción del canal | Bio media + links a los dos sitios |
| emibugliolo.com | Sumar una sección "Charlas y capacitaciones" que enlace a aprendeia.com.ar (y viceversa, ya está hecho) |

## Pilar 2 · Indexación (semana 1)

- [ ] Publicar el sitio en producción.
- [ ] Google Search Console: verificar el dominio y enviar `sitemap.xml`.
- [ ] Bing Webmaster Tools: verificar y enviar el sitemap. **Importante:** ChatGPT usa en parte el índice de Bing.
- [ ] Revisar en Search Console que se indexen las 15 páginas.
- [ ] Probar los datos estructurados con la "Prueba de resultados enriquecidos" de Google (home, una charla, una guía).

## Pilar 3 · Menciones en terceros (continuo)

Lo que más pesa para que una IA te cite:

1. **Cada charla dictada = una página en el sitio del organizador.** Pedí que el evento publique tu nombre, bio y un link a aprendeia.com.ar.
2. **Podcasts como invitado:** 1 por mes. Pedí el link en las notas del episodio.
3. **Artículos invitados** en medios de negocios o blogs de cámaras: 1 por trimestre, sobre el Método ONDA.
4. **Directorios de speakers y formadores** de habla hispana: alta con la misma bio.
5. **El podcast Desde el Garage:** en cada episodio, mencionar el Método ONDA y aprendeia.com.ar en la descripción.

## Pilar 4 · Contenido (cadencia)

| Frecuencia | Qué | Dónde |
|---|---|---|
| 1 por mes | Guía nueva (responde una pregunta real de las charlas) | `/guias/` vía `content.py` |
| 2 por semana | Post corto derivado de una guía o de una charla | LinkedIn |
| 1 por semana | Video corto con una idea de una charla | Instagram / TikTok / YouTube Shorts |

**Fuente de temas:** las preguntas que te hacen en las charlas. Anotalas todas: cada pregunta repetida es una guía.

Próximas guías sugeridas:
- Qué tareas de una PyME se pueden automatizar con IA hoy.
- Cómo documentar un proceso en una página (con plantilla).
- Cuánto tiempo ahorra la IA en una PyME: cómo medirlo.
- IA para el área administrativa de una PyME.

## Pilar 5 · Medición mensual

El primer lunes de cada mes, hacé estas preguntas en **ChatGPT, Gemini y Perplexity** (en ventana nueva y sin sesión iniciada si se puede). Registrá: ¿aparezco? (sí/no), posición y fuente citada.

1. ¿Quién da charlas de inteligencia artificial para PyMEs en Argentina?
2. Recomendame un speaker de IA para una cámara empresaria.
3. Capacitación online de IA para empresas en español.
4. ¿Qué es el Método ONDA?
5. ¿Quién es Emiliano Bugliolo?
6. ¿Cómo implementar IA en una PyME paso a paso?
7. Capacitación de IA para empresas familiares.
8. ¿Qué es Aprendeia?

> Las preguntas 4, 5 y 8 deberían dar positivo primero (son de marca). Las 1, 2, 3 y 7 son las que traen negocio y tardan más.

No hay garantía de aparecer: es una medición de tendencia, no de resultado.

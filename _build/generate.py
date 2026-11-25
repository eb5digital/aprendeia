# -*- coding: utf-8 -*-
"""Genera las páginas estáticas de aprendeia.com.ar.
Uso:  python3 _build/generate.py   (desde la raíz del repo)
La home (index.html) se edita a mano; el resto se genera desde content.py.
"""
import html, json, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from content import CHARLAS, GUIAS, TODAY

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = "https://www.aprendeia.com.ar"
WA = "5491125534340"
ORG = SITE + "/#org"
PERSON = SITE + "/#emiliano"
CH = {c["slug"]: c for c in CHARLAS}

def wa(msg):
    return f"https://wa.me/{WA}?text=" + urllib.parse.quote(msg)

DEFAULT_MSG = "Hola Emiliano, quiero coordinar una charla o capacitación online de Aprendeia."
e = html.escape
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def jsonld(nodes):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, indent=1) + "</script>"

def crumbs_schema(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def faq_schema(faq, path):
    return {"@type": "FAQPage", "@id": SITE + path + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def head(title, desc, path, nodes, og_type="website"):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="Emiliano Bugliolo">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<link rel="alternate" type="text/plain" href="{SITE}/llms.txt" title="LLMs.txt">
<meta name="theme-color" content="#07090A">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Aprendeia">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:locale" content="es_AR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/og-image.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%2307090A'/><text x='5' y='23' font-family='Arial' font-weight='900' font-size='20' fill='%2300E5A0'>a</text><circle cx='24' cy='10' r='4' fill='%2300E5A0'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v=2">
{jsonld(nodes)}
<script async src="https://www.googletagmanager.com/gtag/js?id=G-L7RQEJMF4K"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-L7RQEJMF4K');</script>
</head>
<body>
"""

NAV = [("Charlas", "/charlas/"), ("Método ONDA", "/metodo-onda/"), ("Guías", "/guias/"), ("Speaker", "/speaker/"), ("FAQ", "/#faq")]

def header(active=""):
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{u}"{cur if u == active else ""}>{n}</a></li>' for n, u in NAV)
    return f"""<header>
  <nav class="wrap" aria-label="Principal">
    <a href="/" class="logo" aria-label="Aprendeia, inicio">aprende<span>ia</span></a>
    <ul class="nav-links">{links}</ul>
    <a class="btn btn-sm" data-cta="nav" href="{wa(DEFAULT_MSG)}" target="_blank" rel="noopener">Coordinar una charla</a>
  </nav>
</header>
<main>
"""

def footer(msg=DEFAULT_MSG):
    return f"""</main>
<footer>
  <div class="wrap foot">
    <p>© <span id="y">2026</span> Aprendeia · Charlas y capacitaciones online de IA · por <a href="https://www.emibugliolo.com/" target="_blank" rel="noopener">Emiliano Bugliolo</a></p>
    <p><a href="/charlas/">Charlas</a> · <a href="/metodo-onda/">Método ONDA</a> · <a href="/guias/">Guías</a> · <a href="/speaker/">Kit de speaker</a> · <a href="/llms.txt">llms.txt</a></p>
  </div>
</footer>
<div class="mbar"><a class="btn" data-cta="mobile-bar" href="{wa(msg)}" target="_blank" rel="noopener">Coordinar una charla →</a></div>
<script>
document.getElementById('y').textContent=new Date().getFullYear();
document.querySelectorAll('[data-cta]').forEach(function(a){{a.addEventListener('click',function(){{
  if(window.gtag)gtag('event','generate_lead',{{method:'whatsapp',cta_position:a.dataset.cta,page_path:location.pathname}});
}});}});
document.querySelectorAll('.copybtn').forEach(function(b){{b.addEventListener('click',function(){{
  var t=b.parentElement.querySelector('[data-copy]').innerText;navigator.clipboard&&navigator.clipboard.writeText(t);
  b.textContent='copiado ✓';setTimeout(function(){{b.textContent='copiar'}},1600);
}});}});
</script>
</body>
</html>
"""

def crumbs_html(items):
    out = []
    for i, (n, u) in enumerate(items):
        out.append(f'<a href="{u}">{e(n)}</a>' if i < len(items) - 1 else f"<b>{e(n)}</b>")
    return '<nav class="crumbs" aria-label="Ruta">' + "<span>/</span>".join(out) + "</nav>"

def page_hero(items, eyebrow, h1, lead, extra=""):
    return f"""<section class="page-hero">
  <div class="grid-bg"></div><div class="glow"></div>
  <div class="wrap">
    {crumbs_html(items)}
    <span class="eyebrow"><span class="dot"></span>{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
</section>
"""

def faq_html(faq):
    return '<div class="faq">' + "".join(
        f"<details{' open' if i == 0 else ''}><summary>{e(q)}</summary><p>{e(a)}</p></details>" for i, (q, a) in enumerate(faq)) + "</div>"

def cta_box(title, text, msg, pos):
    return f"""<div class="box acc">
  <h3>{title}</h3>
  <p>{text}</p>
  <a class="btn" data-cta="{pos}" href="{wa(msg)}" target="_blank" rel="noopener">Coordinar una charla {ARROW}</a>
</div>"""

def final_cta(msg, h2="¿Tu equipo o tu evento necesita entender la IA en lenguaje de negocio?"):
    return f"""<section class="final">
  <div class="glow"></div>
  <div class="wrap">
    <span class="label">// siguiente paso</span>
    <h2>{h2}</h2>
    <p class="sub">Escribime con el público, la fecha tentativa y el objetivo. Te respondo con una propuesta concreta: temario, formato y honorarios.</p>
    <a class="btn" data-cta="final" href="{wa(msg)}" target="_blank" rel="noopener">Coordinar una charla {ARROW}</a>
  </div>
</section>
"""

def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

def person_ref():
    return {"@type": "Person", "@id": PERSON, "name": "Emiliano Bugliolo", "url": "https://www.emibugliolo.com/"}

# ---------------------------------------------------------------------------
# CHARLA (ficha)
# ---------------------------------------------------------------------------
def charla_page(c):
    path = f"/charlas/{c['slug']}/"
    items = [("Inicio", "/"), ("Charlas", "/charlas/"), (c["title"], path)]
    msg = f"Hola Emiliano, me interesa la charla \"{c['title']}\" de Aprendeia para mi empresa/evento."
    nodes = [
        {"@type": "Course", "@id": SITE + path + "#course", "name": c["title"], "description": c["resumen"], "url": SITE + path,
         "inLanguage": "es", "educationalLevel": c["nivel"], "timeRequired": c["iso"],
         "teaches": c["llevan"], "audience": {"@type": "BusinessAudience", "audienceType": ", ".join(c["publico"])},
         "provider": {"@type": "EducationalOrganization", "@id": ORG, "name": "Aprendeia", "url": SITE + "/"},
         "instructor": person_ref(),
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": c["iso"], "instructor": person_ref()},
         "offers": {"@type": "Offer", "category": "Charla corporativa", "availability": "https://schema.org/InStock", "url": wa(msg)}},
        crumbs_schema(items), faq_schema(c["faq"], path)]
    others = [x for x in CHARLAS if x["slug"] != c["slug"]][:3]
    rel = "".join(f'<a class="lcard" href="/charlas/{o["slug"]}/"><span class="label">// charla {o["n"]}</span><h3>{e(o["title"])}</h3><p>{e(o["short"])}</p><span class="more">Ver temario →</span></a>' for o in others)
    body = f"""
<section style="border-bottom:none">
  <div class="wrap layout">
    <article class="prose">
      <div class="answer"><b>en resumen</b>{e(c['resumen'])}</div>
      <h2>El problema que resuelve</h2>
      {''.join(f'<p>{e(p)}</p>' for p in c['problema'])}
      <h2>Para quién es</h2>
      <ul>{''.join(f'<li>{e(p)}</li>' for p in c['publico'])}</ul>
      <h2>Qué se llevan los asistentes</h2>
      <ul>{''.join(f'<li>{e(p)}</li>' for p in c['llevan'])}</ul>
      <h2>Agenda</h2>
      <ol class="agenda">{''.join(f'<li><div><b>{e(t)}</b>{e(d)}</div></li>' for t, d in c['agenda'])}</ol>
      <h2>Formato</h2>
      <p>Charla online en vivo por Zoom, Google Meet o Microsoft Teams, con espacio de preguntas. El contenido y los ejemplos se adaptan al rubro y al nivel de la audiencia. Se puede dictar como charla única o como parte de una <a href="/#formatos">capacitación in-company</a>.</p>
      <h2>Preguntas frecuentes</h2>
      {faq_html(c['faq'])}
    </article>
    <aside class="aside">
      <div class="box">
        <h3>Ficha de la charla</h3>
        <ul class="kv">
          <li><span>duración</span><b>{c['dur']}</b></li>
          <li><span>modalidad</span><b>Online en vivo</b></li>
          <li><span>público</span><b>{e(c['publico_corto'])}</b></li>
          <li><span>nivel</span><b>{c['nivel']}</b></li>
          <li><span>idioma</span><b>Español</b></li>
          <li><span>speaker</span><b><a href="/speaker/" style="color:inherit">Emiliano Bugliolo</a></b></li>
        </ul>
      </div>
      {cta_box("¿La querés para tu equipo o evento?", "Contame público, fecha tentativa y objetivo. Te mando propuesta con temario adaptado.", msg, "ficha-aside")}
      <div class="box"><h3>¿Organizás un evento?</h3><p>Bio, foto y requisitos técnicos listos para usar.</p><a class="btn btn-ghost" href="/speaker/">Ver kit de speaker</a></div>
    </aside>
  </div>
  <div class="wrap related"><h2>Otras charlas</h2><div class="cards-grid" style="margin-top:1.2rem">{rel}</div></div>
</section>
"""
    hero = page_hero(items, f"Charla {c['n']} · {c['dur']} · online", e(c["title"]), e(c["short"]),
                     f'<div class="hero-ctas"><a class="btn" data-cta="ficha-hero" href="{wa(msg)}" target="_blank" rel="noopener">Quiero esta charla {ARROW}</a><a class="btn btn-ghost" href="/charlas/">Ver todas</a></div>')
    write(path, head(f"{c['title']} · Charla online de IA · Aprendeia", c["resumen"][:155], path, nodes)
          + header("/charlas/") + hero + body + final_cta(msg) + footer(msg))

# ---------------------------------------------------------------------------
# ÍNDICE DE CHARLAS
# ---------------------------------------------------------------------------
def charlas_index():
    path = "/charlas/"
    items = [("Inicio", "/"), ("Charlas", path)]
    nodes = [{"@type": "ItemList", "@id": SITE + path + "#lista", "name": "Charlas online de IA para empresas de Aprendeia",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/charlas/{c['slug']}/", "name": c["title"]} for i, c in enumerate(CHARLAS)]},
             crumbs_schema(items)]
    talks = "".join(f"""<article class="talk"><span class="talk-n">{c['n']}</span><div>
<h3><a href="/charlas/{c['slug']}/">{e(c['title'])}</a></h3><p>{e(c['short'])}</p>
<div class="talk-tags">{''.join(f'<span class="chip">{t}</span>' for t in c['chips'])}</div>
<a class="talk-link" href="/charlas/{c['slug']}/">Ver temario completo →</a></div><span class="talk-dur">{c['dur']}</span></article>""" for c in CHARLAS)
    body = f"""<section><div class="wrap"><div class="talks">{talks}</div>
<p class="onda-note">→ ¿Necesitás otro tema? Los temarios se combinan o adaptan según el público.</p></div></section>"""
    hero = page_hero(items, "Catálogo · 100% online", "Charlas de IA para empresas, listas para contratar.",
                     "Seis temarios dictados por Emiliano Bugliolo para dueños, directivos y equipos de PyMEs. Todos online, en vivo y adaptables al rubro de la audiencia.")
    write(path, head("Charlas online de IA para empresas y PyMEs · Catálogo · Aprendeia",
                     "Catálogo de charlas online de inteligencia artificial para empresas, PyMEs, cámaras y eventos. Temarios, duración y público de cada charla de Emiliano Bugliolo.", path, nodes)
          + header(path) + hero + body + final_cta(DEFAULT_MSG) + footer())

# ---------------------------------------------------------------------------
# GUÍAS
# ---------------------------------------------------------------------------
def guia_page(g):
    path = f"/guias/{g['slug']}/"
    items = [("Inicio", "/"), ("Guías", "/guias/"), (g["title"], path)]
    c = CH[g["charla"]]
    msg = f"Hola Emiliano, leí la guía \"{g['title']}\" y quiero coordinar una charla o capacitación."
    nodes = [{"@type": "Article", "@id": SITE + path + "#article", "headline": g["title"], "description": g["desc"],
              "url": SITE + path, "mainEntityOfPage": SITE + path, "inLanguage": "es-AR",
              "datePublished": TODAY, "dateModified": TODAY, "image": SITE + "/og-image.png",
              "author": person_ref(), "publisher": {"@type": "EducationalOrganization", "@id": ORG, "name": "Aprendeia", "logo": {"@type": "ImageObject", "url": SITE + "/og-image.png"}}},
             crumbs_schema(items), faq_schema(g["faq"], path)]
    others = [x for x in GUIAS if x["slug"] != g["slug"]]
    rel = "".join(f'<a class="lcard" href="/guias/{o["slug"]}/"><span class="label">// guía</span><h3>{e(o["title"])}</h3><p>{e(o["desc"])}</p><span class="more">Leer →</span></a>' for o in others)
    byline = f'<div class="byline"><img src="/emiliano-bugliolo.webp" width="40" height="40" alt="Emiliano Bugliolo"><div>Por <b><a href="/speaker/" style="color:inherit;text-decoration:none">Emiliano Bugliolo</a></b> · Actualizado <time datetime="{TODAY}">noviembre 2026</time></div></div>'
    body = f"""<section style="border-bottom:none"><div class="wrap layout">
<article class="prose">
  <div class="answer"><b>respuesta corta</b>{e(g['answer'])}</div>
  {g['body']}
  <h2>Preguntas frecuentes</h2>
  {faq_html(g['faq'])}
</article>
<aside class="aside">
  <div class="box"><span class="label">// charla relacionada</span><h3><a href="/charlas/{c['slug']}/" style="text-decoration:none">{e(c['title'])}</a></h3><p>{e(c['short'])}</p><a class="btn btn-ghost" href="/charlas/{c['slug']}/">Ver temario</a></div>
  {cta_box("Llevalo a tu equipo", "Este contenido se puede dictar como charla o capacitación online para tu empresa o evento.", msg, "guia-aside")}
</aside>
</div>
<div class="wrap related"><h2>Más guías</h2><div class="cards-grid" style="margin-top:1.2rem">{rel}</div></div>
</section>"""
    hero = page_hero(items, "Guía · Aprendeia", e(g["title"]), e(g["desc"]), byline)
    write(path, head(f"{g['title']} · Aprendeia", g["desc"], path, nodes, "article")
          + header("/guias/") + hero + body + final_cta(msg) + footer(msg))

def guias_index():
    path = "/guias/"
    items = [("Inicio", "/"), ("Guías", path)]
    nodes = [{"@type": "CollectionPage", "@id": SITE + path, "name": "Guías de IA para PyMEs", "url": SITE + path,
              "hasPart": [{"@type": "Article", "headline": g["title"], "url": f"{SITE}/guias/{g['slug']}/"} for g in GUIAS]},
             crumbs_schema(items)]
    cards = "".join(f'<a class="lcard" href="/guias/{g["slug"]}/"><span class="label">// guía</span><h3>{e(g["title"])}</h3><p>{e(g["desc"])}</p><span class="more">Leer guía →</span></a>' for g in GUIAS)
    body = f'<section><div class="wrap"><div class="cards-grid" style="grid-template-columns:repeat(2,1fr)">{cards}</div></div></section>'
    hero = page_hero(items, "Recursos · sin tecnicismos", "Guías de IA para dueños de PyMEs.",
                     "Respuestas directas a las preguntas que más se repiten en las charlas: cómo empezar, qué medir, cómo elegir una capacitación y cómo lograr que la IA recomiende tu negocio.")
    write(path, head("Guías de inteligencia artificial para PyMEs · Aprendeia",
                     "Guías prácticas sobre IA para dueños de PyMEs y empresas familiares: implementación en 4 fases, empresas familiares, cómo elegir una capacitación y GEO.", path, nodes)
          + header(path) + hero + body + final_cta(DEFAULT_MSG) + footer())

# ---------------------------------------------------------------------------
# MÉTODO ONDA (página pilar)
# ---------------------------------------------------------------------------
ONDA = [
    ("O", "Observar", "Diagnóstico real antes de cualquier acción.",
     "Antes de implementar IA, hay que entender la empresa tal como es. Sin filtros.",
     ["Mapear los 5 procesos que más tiempo consumen en la operación.", "Identificar dónde se toman decisiones improvisadas.", "Listar las tareas repetitivas que hace el equipo cada día.", "Responder: ¿qué pasaría si el dueño no estuviera 2 semanas?", "Marcar qué procesos ya están documentados."],
     "Sabés exactamente dónde está el caos y dónde la IA puede impactar primero."),
    ("N", "Normar", "La IA solo puede mejorar lo que está escrito.",
     "El error más común es querer automatizar procesos que nadie sabe cómo funcionan.",
     ["Documentar cada proceso identificado, paso a paso.", "Definir quién es responsable de cada tarea.", "Establecer tiempos esperados para cada proceso.", "Crear un manual básico para las 3 tareas más críticas.", "Probar que otra persona pueda ejecutar el proceso solo leyendo el manual."],
     "La operación puede funcionar sin que el dueño esté explicando todo el tiempo."),
    ("D", "Desarrollar", "Implementar IA donde ya hay estructura.",
     "Con procesos documentados, se identifica qué herramientas hacen más rápido lo que ya se hace.",
     ["Elegir UN proceso para automatizar primero: el de mayor impacto.", "Investigar 2 o 3 herramientas de IA específicas para ese proceso.", "Hacer una prueba piloto con el equipo más chico posible.", "Medir el antes y el después: tiempo, costo y errores.", "Documentar la herramienta como parte del proceso."],
     "Tenés tu primera automatización funcionando y medida. Sin humo."),
    ("A", "Autonomizar", "El objetivo final: que la empresa funcione sin depender del dueño.",
     "Una herramienta que solo el dueño sabe usar no es una ventaja. La IA tiene que estar en el equipo.",
     ["Capacitar al equipo en las herramientas implementadas.", "Delegar la operación de las automatizaciones a una persona específica.", "Crear métricas para medir el desempeño de cada herramienta.", "Revisar mensualmente qué funciona y qué necesita ajuste.", "Expandir gradualmente a los siguientes procesos de mayor impacto."],
     "La empresa usa IA de forma sostenible y el dueño puede enfocarse en estrategia."),
]

def onda_page():
    path = "/metodo-onda/"
    items = [("Inicio", "/"), ("Método ONDA", path)]
    faq = [
        ("¿Qué es el Método ONDA?", "El Método ONDA es la metodología creada por Emiliano Bugliolo para adoptar inteligencia artificial en PyMEs en 4 fases: Observar, Normar, Desarrollar y Autonomizar. Propone ordenar y documentar procesos antes de automatizar, y terminar con un equipo que opera la IA sin depender del dueño."),
        ("¿Qué significa ONDA?", "Es el acrónimo de sus cuatro fases: Observar (diagnóstico), Normar (documentar procesos), Desarrollar (piloto de IA medido) y Autonomizar (el equipo opera las herramientas)."),
        ("¿Se puede saltear alguna fase?", "No. Cada fase es la condición de la siguiente. Saltear Normar, por ejemplo, implica automatizar procesos que nadie documentó."),
        ("¿Dónde se aprende el Método ONDA?", "En las charlas, capacitaciones in-company y workshops online de Aprendeia, y con la Hoja de Ruta en PDF disponible en aprendeia.com.ar."),
    ]
    nodes = [
        {"@type": "HowTo", "@id": SITE + "/#metodo-onda", "name": "Método ONDA: cómo adoptar inteligencia artificial en una PyME", "url": SITE + path,
         "description": "Metodología en 4 fases creada por Emiliano Bugliolo para adoptar IA en PyMEs sin desordenar la operación.",
         "author": person_ref(), "inLanguage": "es",
         "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": d + " " + " ".join(lst), "url": f"{SITE}{path}#{n.lower()}"} for i, (_, n, d, _x, lst, _r) in enumerate(ONDA)]},
        {"@type": "DefinedTerm", "name": "Método ONDA", "description": faq[0][1], "url": SITE + path},
        crumbs_schema(items), faq_schema(faq, path)]
    phases = ""
    for L, n, sub, intro, lst, res in ONDA:
        phases += f"""<h2 id="{n.lower()}"><span class="c-acc">{L}</span> · {n}: {e(sub[0].lower() + sub[1:])}</h2>
<p>{e(intro)}</p><ul>{''.join(f'<li>{e(x)}</li>' for x in lst)}</ul>
<p><strong>Resultado:</strong> {e(res)}</p>"""
    cards = "".join(f'<article class="phase"><div class="phase-l">{L}</div><span class="phase-k">fase {i+1}</span><h3>{n}</h3><p>{e(sub)}</p></article>' for i, (L, n, sub, *_r) in enumerate(ONDA))
    body = f"""<section style="padding-top:3.5rem"><div class="wrap"><div class="onda">{cards}</div></div></section>
<section style="border-bottom:none"><div class="wrap layout">
<article class="prose">
  <div class="answer"><b>definición</b>{e(faq[0][1])}</div>
  <h2>Por qué un método</h2>
  <p>La mayoría de los dueños quiere implementar IA pero no sabe por dónde empezar. El resultado habitual es comprar herramientas que nadie usa o automatizar procesos desordenados. El Método ONDA es el camino que se recorre antes de tocar cualquier herramienta. Cuatro fases, en orden. No se salta ninguna.</p>
  <blockquote>La IA es un multiplicador: multiplica lo que ya existe. Si lo que existe es desorden, multiplica el desorden.</blockquote>
  {phases}
  <h2>Cómo se aplica en Aprendeia</h2>
  <table>
    <tr><th>Formato</th><th>Qué se hace con el método</th></tr>
    <tr><td><a href="/charlas/metodo-onda-adoptar-ia-sin-desordenar-tu-empresa/">Charla Método ONDA</a></td><td>Se presentan las 4 fases y cada asistente se autodiagnostica.</td></tr>
    <tr><td>Capacitación in-company</td><td>Cada área recorre Observar y Normar sobre sus procesos reales.</td></tr>
    <tr><td>Workshop para dueños</td><td>Cada dueño sale con su diagnóstico y el primer piloto definido.</td></tr>
  </table>
  <h2>Preguntas frecuentes</h2>
  {faq_html(faq)}
</article>
<aside class="aside">
  <div class="box acc"><span class="label">// recurso gratuito</span><h3>Hoja de Ruta en PDF</h3><p>Las 4 fases con el checklist de cada una.</p><a class="btn" href="/#hoja-de-ruta">Descargar gratis</a></div>
  {cta_box("Llevá ONDA a tu empresa", "Charla, capacitación in-company o workshop online para dueños.", "Hola Emiliano, quiero una charla o capacitación sobre el Método ONDA.", "onda-aside")}
</aside>
</div></section>"""
    hero = page_hero(items, "Metodología propia · 4 fases", "Método ONDA: el orden correcto para adoptar IA en una PyME.",
                     "Observar, Normar, Desarrollar y Autonomizar. La metodología de Emiliano Bugliolo para implementar inteligencia artificial sin desordenar la operación.")
    write(path, head("Método ONDA: cómo adoptar IA en una PyME en 4 fases · Aprendeia",
                     "El Método ONDA de Emiliano Bugliolo explica cómo adoptar inteligencia artificial en una PyME en 4 fases: Observar, Normar, Desarrollar y Autonomizar.", path, nodes)
          + header(path) + hero + body + final_cta("Hola Emiliano, quiero una charla o capacitación sobre el Método ONDA.") + footer())

# ---------------------------------------------------------------------------
# SPEAKER (kit para organizadores)
# ---------------------------------------------------------------------------
BIO_CORTA = "Emiliano Bugliolo es speaker y capacitador en inteligencia artificial aplicada a PyMEs. Socio operativo de una empresa familiar argentina con más de 70 años en el mercado y creador del Método ONDA para adoptar IA sin desordenar la empresa."
BIO_MEDIA = "Emiliano Bugliolo es speaker y capacitador en inteligencia artificial aplicada a PyMEs, y consultor en profesionalización de empresas familiares. Hace más de 20 años toma decisiones desde adentro de una empresa familiar argentina con más de 70 años en el mercado: finanzas, procesos, equipos y transformación digital. Es creador del Método ONDA (Observar, Normar, Desarrollar, Autonomizar) y conductor del podcast Desde el Garage. A través de Aprendeia dicta charlas y capacitaciones online para dueños, directivos y equipos de habla hispana."
BIO_LARGA = BIO_MEDIA + " Además de su rol en la empresa familiar, desarrolla proyectos propios de e-commerce, alquiler de espacios para eventos, renta temporaria y productos digitales. Su enfoque es directo y orientado a resultados: rentabilidad antes que facturación, procesos antes que herramientas y estructura antes que esfuerzo. Su consultoría estratégica está en emibugliolo.com."
PRESENTACION = "Nuestro próximo speaker lleva más de 20 años operando una empresa familiar que tiene más de 70 en el mercado. No viene a mostrarnos herramientas: viene a contarnos en qué orden hay que hacer las cosas para que la inteligencia artificial realmente le sirva a una PyME. Creador del Método ONDA y conductor del podcast Desde el Garage. Con ustedes, Emiliano Bugliolo."

def speaker_page():
    path = "/speaker/"
    items = [("Inicio", "/"), ("Speaker", path)]
    nodes = [
        {"@type": "ProfilePage", "@id": SITE + path, "url": SITE + path, "name": "Emiliano Bugliolo · Speaker de IA para PyMEs",
         "dateModified": TODAY, "mainEntity": {"@id": PERSON}},
        {"@type": "Person", "@id": PERSON, "name": "Emiliano Bugliolo", "description": BIO_CORTA, "image": SITE + "/emiliano-bugliolo.webp",
         "jobTitle": "Speaker y capacitador en IA aplicada a PyMEs", "url": "https://www.emibugliolo.com/",
         "knowsAbout": ["Inteligencia artificial para PyMEs", "Empresas familiares", "Profesionalización", "Automatización de procesos", "GEO"],
         "sameAs": ["https://www.emibugliolo.com/", "https://www.linkedin.com/in/emilianobugliolo/", "https://www.instagram.com/emibugliolo/", "https://www.youtube.com/@emibugliolo", "https://www.tiktok.com/@emibugliolo"]},
        crumbs_schema(items)]
    def copy(label, txt):
        return f'<h3>{label}</h3><div class="copybox"><button class="copybtn" type="button">copiar</button><p data-copy>{e(txt)}</p></div>'
    temas = "".join(f'<li><a href="/charlas/{c["slug"]}/">{e(c["title"])}</a> <span class="c-mut mono" style="font-size:.78rem">· {c["dur"]}</span></li>' for c in CHARLAS)
    body = f"""<section style="border-bottom:none"><div class="wrap layout">
<article class="prose">
  <div class="answer"><b>en una frase</b>{e(BIO_CORTA)}</div>
  <h2>Bios listas para usar</h2>
  {copy("Bio corta (para flyers y redes)", BIO_CORTA)}
  {copy("Bio media (para programas y web del evento)", BIO_MEDIA)}
  {copy("Bio larga (para prensa)", BIO_LARGA)}
  {copy("Presentación para el moderador (30 segundos)", PRESENTACION)}
  <h2>Temas disponibles</h2>
  <ul>{temas}</ul>
  <h2>Requisitos técnicos</h2>
  <ul>
    <li>Plataforma: Zoom, Google Meet, Microsoft Teams o StreamYard (la que use el evento).</li>
    <li>Prueba técnica de 15 minutos antes del inicio.</li>
    <li>Presentación con diapositivas compartidas por el speaker.</li>
    <li>Espacio de preguntas al final (recomendado: 10 a 15 minutos).</li>
    <li>Grabación: a coordinar con cada organizador.</li>
  </ul>
  <h2>Qué recibe el organizador</h2>
  <ul>
    <li>Temario adaptado al público del evento.</li>
    <li>Bio, foto y textos de difusión.</li>
    <li>Material para los asistentes: Hoja de Ruta del Método ONDA en PDF.</li>
  </ul>
</article>
<aside class="aside">
  <figure class="photo" style="max-width:none"><img src="/emiliano-bugliolo.webp" width="560" height="700" alt="Emiliano Bugliolo, speaker de inteligencia artificial para PyMEs"><figcaption>foto oficial</figcaption></figure>
  <div class="box"><h3>Descargas</h3><ul class="kv">
    <li><span>foto (alta)</span><b><a href="/emibuglioloperfil.jpg" download style="color:var(--acc)">JPG ↓</a></b></li>
    <li><span>foto (web)</span><b><a href="/emiliano-bugliolo.webp" download style="color:var(--acc)">WebP ↓</a></b></li>
    <li><span>imprimir kit</span><b><a href="javascript:window.print()" style="color:var(--acc)">PDF ↓</a></b></li>
  </ul></div>
  {cta_box("Invitalo a tu evento", "Contame fecha, público y duración del espacio.", "Hola Emiliano, quiero invitarte como speaker a un evento.", "speaker-aside")}
</aside>
</div></section>"""
    hero = page_hero(items, "Kit para organizadores", "Emiliano Bugliolo, speaker de IA aplicada a PyMEs.",
                     "Todo lo que necesita un organizador para sumar a Emiliano a su evento online: bios, foto, temas y requisitos técnicos.",
                     '<div class="links"><a href="https://www.emibugliolo.com/" target="_blank" rel="noopener me">emibugliolo.com ↗</a><a href="https://www.linkedin.com/in/emilianobugliolo/" target="_blank" rel="noopener me">LinkedIn ↗</a><a href="https://www.youtube.com/@emibugliolo" target="_blank" rel="noopener me">YouTube ↗</a></div>')
    write(path, head("Emiliano Bugliolo · Speaker de IA para PyMEs · Kit para organizadores · Aprendeia",
                     "Bio, foto, temas y requisitos técnicos de Emiliano Bugliolo, speaker y capacitador en inteligencia artificial aplicada a PyMEs y empresas familiares.", path, nodes, "profile")
          + header(path) + hero + body + final_cta("Hola Emiliano, quiero invitarte como speaker a un evento.", "¿Organizás un evento para empresarios?") + footer("Hola Emiliano, quiero invitarte como speaker a un evento."))

# ---------------------------------------------------------------------------
# SITEMAP + LLMS
# ---------------------------------------------------------------------------
def sitemap():
    urls = ["/", "/charlas/", "/metodo-onda/", "/speaker/", "/guias/"] + [f"/charlas/{c['slug']}/" for c in CHARLAS] + [f"/guias/{g['slug']}/" for g in GUIAS]
    pr = {"/": "1.0", "/charlas/": "0.9", "/metodo-onda/": "0.9", "/speaker/": "0.8", "/guias/": "0.7"}
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr.get(u, '0.7')}</priority></url>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(xml + "</urlset>\n")

def strip(h):
    h = re.sub(r"<li>", "- ", h); h = re.sub(r"<h2[^>]*>", "\n## ", h); h = re.sub(r"</(p|li|h2|tr)>", "\n", h)
    h = re.sub(r"</t[dh]>", " | ", h); h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(h)).strip()

def llms():
    s = f"""# Aprendeia

> Aprendeia (aprendeia.com.ar) es la unidad de formación de Emiliano Bugliolo: charlas y capacitaciones online, en vivo, sobre adopción de inteligencia artificial para dueños, directivos y equipos de PyMEs y empresas familiares de habla hispana. Enfoque de negocio, sin tecnicismos, basado en el Método ONDA.

## Datos clave

- Qué ofrece: charlas online (45–60 min), capacitaciones in-company online (2–4 sesiones) y workshops online para dueños con el Método ONDA.
- Modalidad: 100% online y en vivo (Zoom, Google Meet o Microsoft Teams). Disponible para Argentina, Latinoamérica y España.
- Público: cámaras y asociaciones empresarias, PyMEs y empresas familiares, eventos y congresos, aceleradoras, dueños y directivos.
- Contratación: por WhatsApp (https://wa.me/{WA}). Se envía una propuesta con temario, formato y honorarios.
- Idioma: español.
- Diferencia con emibugliolo.com: Aprendeia = formación (charlas y capacitaciones). emibugliolo.com = consultoría estratégica e implementación.

## Quién la dicta

{BIO_MEDIA}

- [Kit de speaker (bios, foto, requisitos)]({SITE}/speaker/)
- Sitio personal y consultoría: https://www.emibugliolo.com/
- LinkedIn: https://www.linkedin.com/in/emilianobugliolo/
- YouTube: https://www.youtube.com/@emibugliolo

## Método ONDA

- [Método ONDA: Observar, Normar, Desarrollar, Autonomizar]({SITE}/metodo-onda/): metodología en 4 fases para adoptar IA en PyMEs sin desordenar la operación.

## Charlas

""" + "\n".join(f"- [{c['title']}]({SITE}/charlas/{c['slug']}/): {c['short']} ({c['dur']}, {c['publico_corto'].lower()})" for c in CHARLAS) + """

## Guías

""" + "\n".join(f"- [{g['title']}]({SITE}/guias/{g['slug']}/): {g['answer']}" for g in GUIAS) + f"""

## Opcional

- [Contenido completo en texto plano]({SITE}/llms-full.txt)
- [Hoja de Ruta del Método ONDA (PDF)]({SITE}/metodo-onda-hoja-de-ruta.pdf)
"""
    open(os.path.join(ROOT, "llms.txt"), "w").write(s)
    full = s + "\n\n---\n\n# Método ONDA (detalle)\n\n"
    for L, n, sub, intro, lst, res in ONDA:
        full += f"## {n}\n{sub} {intro}\n" + "\n".join("- " + x for x in lst) + f"\nResultado: {res}\n\n"
    for c in CHARLAS:
        full += f"---\n\n# Charla: {c['title']}\nURL: {SITE}/charlas/{c['slug']}/\nDuración: {c['dur']} · Modalidad: online en vivo · Nivel: {c['nivel']}\n\n{c['resumen']}\n\n" + "\n".join(c["problema"]) + "\n\nPara quién:\n" + "\n".join("- " + x for x in c["publico"]) + "\n\nQué se llevan:\n" + "\n".join("- " + x for x in c["llevan"]) + "\n\nAgenda:\n" + "\n".join(f"{i+1}. {t}: {d}" for i, (t, d) in enumerate(c["agenda"])) + "\n\n" + "\n".join(f"P: {q}\nR: {a}" for q, a in c["faq"]) + "\n\n"
    for g in GUIAS:
        full += f"---\n\n# Guía: {g['title']}\nURL: {SITE}/guias/{g['slug']}/\nAutor: Emiliano Bugliolo · Actualizado: {TODAY}\n\n{g['answer']}\n\n{strip(g['body'])}\n\n" + "\n".join(f"P: {q}\nR: {a}" for q, a in g["faq"]) + "\n\n"
    open(os.path.join(ROOT, "llms-full.txt"), "w").write(full)

if __name__ == "__main__":
    for c in CHARLAS: charla_page(c)
    charlas_index()
    for g in GUIAS: guia_page(g)
    guias_index(); onda_page(); speaker_page(); sitemap(); llms()
    print("OK:", len(CHARLAS), "charlas,", len(GUIAS), "guías + índices, ONDA, speaker, sitemap, llms")

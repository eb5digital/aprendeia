# -*- coding: utf-8 -*-
"""Contenido del sitio Aprendeia. Editá acá y corré: python3 _build/generate.py"""

TODAY = "2026-11-25"

# ---------------------------------------------------------------------------
# CHARLAS
# ---------------------------------------------------------------------------
CHARLAS = [
  {
    "slug": "ia-sin-humo-para-duenos-de-pymes",
    "n": "01",
    "title": "IA sin humo para dueños de PyMEs: por dónde empezar",
    "short": "Qué puede hacer hoy la IA en una PyME, qué no, y cuál es el primer paso con impacto económico real.",
    "resumen": "Charla online de 45 a 60 minutos para dueños y directivos de PyMEs que escuchan hablar de IA todos los días pero no saben por dónde empezar. Ordena el tema en lenguaje de negocio y termina con un primer paso concreto, medible y de bajo riesgo.",
    "problema": [
      "El dueño de una PyME recibe todas las semanas una herramienta nueva, un curso nuevo y una promesa nueva. El resultado suele ser uno de dos: parálisis (\"esto no es para nosotros\") o compras impulsivas de herramientas que nadie termina usando.",
      "El problema no es la tecnología. Es la falta de un criterio para decidir dónde aplicarla primero. Esta charla da ese criterio.",
    ],
    "publico": ["Dueños y socios de PyMEs y empresas familiares", "Gerentes generales y directivos", "Socios de cámaras y asociaciones empresarias"],
    "llevan": [
      "Un mapa simple de qué tareas de una PyME ya se pueden asistir con IA y cuáles todavía no.",
      "Los errores más comunes al empezar y lo que cuestan en tiempo y plata.",
      "Un criterio para elegir el primer proceso: impacto económico, frecuencia y riesgo.",
      "Un primer paso para ejecutar la semana siguiente.",
    ],
    "agenda": [
      ("El ruido", "Por qué la mayoría de las PyMEs está mirando la IA al revés."),
      ("Qué hace hoy la IA en una PyME", "Atención al cliente, ventas, administración, contenido y análisis: casos concretos."),
      ("Dónde no conviene usarla (todavía)", "Límites, riesgos y decisiones que no se delegan."),
      ("El primer paso", "Cómo elegir un proceso y medir el antes y el después."),
      ("Preguntas", "Espacio abierto con la audiencia."),
    ],
    "dur": "45–60 min", "iso": "PT60M", "nivel": "Introductorio", "publico_corto": "Dueños y directivos",
    "chips": ["dueños", "introductoria"],
    "faq": [
      ("¿Hace falta saber de tecnología para aprovechar la charla?", "No. Está pensada para dueños sin perfil técnico. Se habla de procesos, tiempo y plata, no de código."),
      ("¿Se puede adaptar a un rubro específico?", "Sí. Los ejemplos se ajustan al rubro de la audiencia: comercio, industria, servicios, salud, gastronomía, entre otros."),
    ],
  },
  {
    "slug": "metodo-onda-adoptar-ia-sin-desordenar-tu-empresa",
    "n": "02",
    "title": "Método ONDA: adoptar IA sin desordenar tu empresa",
    "short": "Las 4 fases para implementar IA de forma sostenible: Observar, Normar, Desarrollar y Autonomizar.",
    "resumen": "Charla online de 60 minutos que presenta el Método ONDA, la metodología de Emiliano Bugliolo para adoptar IA en PyMEs en 4 fases: Observar, Normar, Desarrollar y Autonomizar. Es la charla insignia de Aprendeia.",
    "problema": [
      "Muchas empresas implementan IA sobre procesos que nadie documentó. El resultado es previsible: automatizan el caos, pero más rápido.",
      "El Método ONDA propone un orden: primero entender, después escribir, después automatizar y, por último, delegar. No se salta ninguna fase.",
    ],
    "publico": ["Dueños y directivos de PyMEs", "Responsables de operaciones y administración", "Programas de aceleración y formación empresarial"],
    "llevan": [
      "Las 4 fases del Método ONDA y el entregable de cada una.",
      "Un autodiagnóstico para saber en qué fase está su empresa.",
      "El criterio para elegir el primer piloto de IA.",
      "Las métricas mínimas para saber si la IA funciona: tiempo, costo y errores.",
    ],
    "agenda": [
      ("Observar", "Diagnóstico real: dónde se pierde tiempo y dónde se improvisa."),
      ("Normar", "Por qué la IA solo mejora lo que está escrito."),
      ("Desarrollar", "Un proceso, un piloto, una métrica."),
      ("Autonomizar", "Que el equipo opere sin depender del dueño."),
      ("Autodiagnóstico y preguntas", "Cada asistente identifica en qué fase está."),
    ],
    "dur": "60 min", "iso": "PT60M", "nivel": "Intermedio", "publico_corto": "Dueños y directivos",
    "chips": ["dueños y directivos", "metodología"],
    "faq": [
      ("¿En qué se diferencia de un workshop?", "La charla presenta el método completo. El workshop online para dueños lo aplica: cada participante hace su diagnóstico y sale con su propio plan."),
      ("¿Los asistentes reciben material?", "Sí. La Hoja de Ruta del Método ONDA en PDF, con el checklist de cada fase."),
    ],
  },
  {
    "slug": "procesos-antes-que-herramientas",
    "n": "03",
    "title": "Procesos antes que herramientas: por qué tu IA no funciona",
    "short": "La IA solo mejora lo que está escrito. Cómo documentar procesos críticos, asignar responsables y recién después automatizar.",
    "resumen": "Charla online para equipos y mandos medios sobre la condición previa de cualquier implementación de IA: procesos documentados, con responsable y tiempos. Explica por qué la IA solo mejora lo que está escrito y cómo documentar sin burocracia.",
    "problema": [
      "Cuando un proceso vive en la cabeza de una persona, ninguna herramienta lo puede mejorar. Por eso tantas empresas compran software o licencias de IA que después nadie usa.",
      "Documentar no es llenar manuales que nadie lee. Es escribir lo mínimo para que otra persona pueda ejecutar la tarea. Esa es la base para delegar y para automatizar.",
    ],
    "publico": ["Mandos medios y líderes de equipo", "Equipos de administración, operaciones y atención", "Empresas que ya compraron herramientas y no ven resultados"],
    "llevan": [
      "Un formato simple para documentar un proceso en una página.",
      "Cómo detectar tareas repetitivas que son candidatas a IA.",
      "Cómo asignar responsables y tiempos esperados.",
      "Cómo usar IA para documentar más rápido: grabar, transcribir y convertir en manual.",
    ],
    "agenda": [
      ("El síntoma", "Herramientas compradas que nadie usa."),
      ("La causa", "Procesos que dependen de una sola persona."),
      ("Documentar sin burocracia", "El formato de una página y la prueba de \"otra persona lo ejecuta leyendo\"."),
      ("IA como asistente de documentación", "Grabar, transcribir y convertir en manual."),
      ("Preguntas", "Espacio abierto con la audiencia."),
    ],
    "dur": "45–60 min", "iso": "PT60M", "nivel": "Intermedio", "publico_corto": "Equipos y mandos medios",
    "chips": ["equipos", "operaciones"],
    "faq": [
      ("¿Sirve para equipos operativos?", "Sí. Es la charla más práctica para mandos medios y equipos que ejecutan los procesos todos los días."),
      ("¿Se puede hacer en formato taller?", "Sí, como capacitación in-company: en una segunda sesión cada área documenta un proceso real."),
    ],
  },
  {
    "slug": "empresa-familiar-e-ia",
    "n": "04",
    "title": "Empresa familiar + IA: profesionalizar sin perder la esencia",
    "short": "Roles, decisiones y dependencia del fundador. Cómo usar la IA como palanca de profesionalización en empresas familiares.",
    "resumen": "Charla online para empresas familiares sobre cómo usar la IA como palanca de profesionalización: roles claros, decisiones con datos y menor dependencia del fundador. Basada en la experiencia de Emiliano Bugliolo como socio operativo de una empresa familiar con más de 70 años en el mercado.",
    "problema": [
      "En las empresas familiares el problema rara vez es la tecnología. Son los roles difusos, las decisiones que dependen de una persona y la información que vive en la cabeza del fundador.",
      "La IA puede acelerar la profesionalización o amplificar el desorden. La diferencia está en el orden en que se implementa.",
    ],
    "publico": ["Dueños y socios de empresas familiares", "Segunda y tercera generación en la empresa", "Cámaras, institutos y redes de empresas familiares"],
    "llevan": [
      "Un diagnóstico rápido de dependencia del fundador.",
      "Cómo separar roles familiares de roles operativos.",
      "Dónde ayuda la IA a profesionalizar: información, reportes, procesos y comunicación interna.",
      "Cómo involucrar a la siguiente generación sin generar choques.",
    ],
    "agenda": [
      ("Una historia de más de 70 años", "Lo que se aprende operando una empresa familiar desde adentro."),
      ("La trampa del fundador indispensable", "Por qué el crecimiento se frena en la misma persona que lo generó."),
      ("Profesionalizar con datos", "Reportes, métricas y decisiones que no dependen de una sola persona."),
      ("La IA como puente generacional", "Cómo la tecnología puede ordenar la conversación entre generaciones."),
      ("Preguntas", "Espacio abierto con la audiencia."),
    ],
    "dur": "60 min", "iso": "PT60M", "nivel": "Intermedio", "publico_corto": "Empresas familiares",
    "chips": ["empresas familiares", "cámaras"],
    "faq": [
      ("¿Se tratan temas legales, societarios o de sucesión?", "No. La charla trabaja gestión, roles y procesos. Los temas legales, societarios o sucesorios requieren asesoramiento profesional específico."),
      ("¿Es para cámaras o para una sola familia empresaria?", "Funciona en los dos casos. Para una sola empresa conviene la capacitación in-company o el workshop."),
    ],
  },
  {
    "slug": "automatizacion-minima-viable",
    "n": "05",
    "title": "Automatización mínima viable: tu primer proceso con IA",
    "short": "Cómo elegir un único proceso, probar con un piloto chico y medir antes y después en tiempo, costo y errores.",
    "resumen": "Charla-taller online para equipos que quieren pasar de la teoría a la práctica: elegir un único proceso, armar un piloto chico con IA y medir el resultado. Incluye demostración en vivo.",
    "problema": [
      "La mayoría de los proyectos de IA en PyMEs fallan por exceso de ambición: quieren automatizar todo a la vez, sin medir nada.",
      "La automatización mínima viable propone lo contrario: un proceso, un piloto, una métrica. Si funciona, se escala. Si no, se descarta rápido y barato.",
    ],
    "publico": ["Responsables de área", "Equipos de administración, ventas y atención", "Empresas que ya tienen procesos mínimamente documentados"],
    "llevan": [
      "Una matriz para priorizar procesos por impacto y facilidad.",
      "El diseño de un piloto de pocas semanas, con alcance y responsable.",
      "Cómo medir antes y después: tiempo, costo y errores.",
      "Ejemplos en vivo de automatizaciones simples con herramientas de uso general.",
    ],
    "agenda": [
      ("Por qué fallan los proyectos de IA", "Ambición sin medición."),
      ("Elegir el proceso", "Matriz de impacto vs. facilidad."),
      ("Diseñar el piloto", "Alcance, responsable, duración y métrica."),
      ("Demostración en vivo", "Una automatización simple, de punta a punta."),
      ("Medir y decidir", "Escalar, ajustar o descartar."),
      ("Preguntas", "Espacio abierto con la audiencia."),
    ],
    "dur": "60–90 min", "iso": "PT90M", "nivel": "Práctico", "publico_corto": "Equipos y responsables de área",
    "chips": ["equipos", "práctica"],
    "faq": [
      ("¿Qué herramientas se usan?", "Herramientas de IA de uso general y de automatización sin código. La elección final depende del proceso y de lo que la empresa ya usa."),
      ("¿Los asistentes necesitan instalar algo?", "No para la charla. En el formato in-company se puede sumar una sesión práctica con las herramientas de la empresa."),
    ],
  },
  {
    "slug": "visibilidad-en-ia-geo-para-pymes",
    "n": "06",
    "title": "Que la IA te recomiende: visibilidad de tu negocio en ChatGPT y Google",
    "short": "Cómo cambian las búsquedas con la IA generativa y qué hacer para que tu empresa aparezca cuando un cliente le pregunta a una IA.",
    "resumen": "Charla online sobre GEO (Generative Engine Optimization): cómo cambian las búsquedas con la IA generativa y qué puede hacer una PyME para aparecer cuando un cliente le pregunta a ChatGPT, Gemini o Perplexity.",
    "problema": [
      "Cada vez más clientes le piden recomendaciones a una IA en lugar de recorrer resultados de Google. Si tu negocio no está descripto de forma clara y consistente en la web, la IA no tiene de dónde sacar información para recomendarte.",
      "La buena noticia: las bases no requieren grandes presupuestos. Requieren orden, claridad y constancia.",
    ],
    "publico": ["Dueños de PyMEs y profesionales independientes", "Equipos de marketing y comunicación", "Cámaras y asociaciones de comercio"],
    "llevan": [
      "Qué es GEO y en qué se diferencia del SEO tradicional.",
      "Cómo \"lee\" una IA un negocio: entidades, consistencia y fuentes.",
      "Un checklist de 10 puntos para mejorar la visibilidad de un sitio.",
      "Cómo medir si la IA te menciona.",
    ],
    "agenda": [
      ("Cómo busca hoy un cliente", "De la lista de links a la respuesta directa."),
      ("Qué es GEO", "Definición, diferencias y similitudes con el SEO."),
      ("Cómo arma una respuesta una IA", "Entidades, fuentes y consistencia."),
      ("Checklist para PyMEs", "Sitio, perfiles, reseñas y contenido que responde preguntas."),
      ("Medición", "Cómo saber si te mencionan."),
      ("Preguntas", "Espacio abierto con la audiencia."),
    ],
    "dur": "45–60 min", "iso": "PT60M", "nivel": "Introductorio", "publico_corto": "Dueños y marketing",
    "chips": ["marketing", "GEO"],
    "faq": [
      ("¿GEO reemplaza al SEO?", "No. Lo complementa. Muchas de las bases son las mismas: contenido claro, buena estructura y autoridad."),
      ("¿Se garantiza aparecer en ChatGPT?", "No. Nadie puede garantizarlo. Se trabaja sobre los factores que aumentan la probabilidad de ser citado."),
    ],
  },
]

# ---------------------------------------------------------------------------
# GUÍAS (contenido para GEO: responde preguntas reales de dueños)
# ---------------------------------------------------------------------------
GUIAS = [
  {
    "slug": "como-implementar-ia-en-una-pyme",
    "title": "Cómo implementar inteligencia artificial en una PyME: guía en 4 fases",
    "desc": "Guía práctica para implementar IA en una PyME sin desordenar la operación: diagnóstico, documentación de procesos, piloto medido y autonomía del equipo. Método ONDA.",
    "answer": "Para implementar inteligencia artificial en una PyME conviene seguir un orden: primero diagnosticar dónde se pierde tiempo (Observar), después documentar esos procesos (Normar), luego probar IA en un único proceso con un piloto medido (Desarrollar) y, por último, capacitar al equipo para que lo opere sin depender del dueño (Autonomizar). Ese orden es el Método ONDA.",
    "charla": "metodo-onda-adoptar-ia-sin-desordenar-tu-empresa",
    "body": """
<h2>Por qué la mayoría de las PyMEs empieza mal</h2>
<p>El error más común es empezar por la herramienta: alguien ve una demo, contrata una licencia y espera que el equipo la adopte. Sin un proceso claro detrás, la herramienta queda sin uso a las pocas semanas.</p>
<p>La IA es un multiplicador. Multiplica lo que ya existe. Si lo que existe es desorden, multiplica el desorden.</p>

<h2>Fase 1 · Observar: diagnóstico real</h2>
<p>Antes de tocar cualquier herramienta, hay que ver la empresa como es, sin filtros.</p>
<ul>
  <li>Mapeá los 5 procesos que más tiempo consumen.</li>
  <li>Identificá dónde se toman decisiones improvisadas.</li>
  <li>Listá las tareas repetitivas que hace el equipo cada día.</li>
  <li>Respondé con honestidad: ¿qué pasaría si el dueño no estuviera dos semanas?</li>
</ul>
<p><strong>Resultado:</strong> sabés dónde está el caos y dónde la IA puede impactar primero.</p>

<h2>Fase 2 · Normar: escribir antes de automatizar</h2>
<p>La IA solo puede mejorar lo que está escrito. Documentar no es hacer manuales eternos: es escribir lo mínimo para que otra persona ejecute la tarea.</p>
<ul>
  <li>Documentá paso a paso los procesos identificados.</li>
  <li>Definí un responsable por tarea y un tiempo esperado.</li>
  <li>Probá que otra persona pueda ejecutar el proceso solo leyendo el documento.</li>
</ul>
<p><strong>Resultado:</strong> la operación funciona sin que el dueño esté explicando todo el tiempo.</p>

<h2>Fase 3 · Desarrollar: un proceso, un piloto, una métrica</h2>
<ul>
  <li>Elegí <strong>un</strong> proceso para empezar: el de mayor impacto y menor riesgo.</li>
  <li>Evaluá 2 o 3 herramientas específicas para ese proceso.</li>
  <li>Hacé una prueba piloto con el equipo más chico posible.</li>
  <li>Medí antes y después: tiempo, costo y errores.</li>
</ul>
<p><strong>Resultado:</strong> una primera automatización funcionando y medida. Sin humo.</p>

<h2>Fase 4 · Autonomizar: que funcione sin vos</h2>
<p>Una herramienta que solo el dueño sabe usar no es una ventaja: es otra dependencia.</p>
<ul>
  <li>Capacitá al equipo en las herramientas implementadas.</li>
  <li>Asigná una persona responsable de cada automatización.</li>
  <li>Revisá mensualmente qué funciona y qué hay que ajustar.</li>
  <li>Expandí gradualmente al siguiente proceso de mayor impacto.</li>
</ul>

<h2>Qué medir</h2>
<table>
  <tr><th>Métrica</th><th>Pregunta que responde</th></tr>
  <tr><td>Horas por semana del proceso</td><td>¿Ahorramos tiempo real?</td></tr>
  <tr><td>Costo por unidad (pedido, cliente, factura)</td><td>¿Mejoró la rentabilidad?</td></tr>
  <tr><td>Errores o retrabajos</td><td>¿Mejoró la calidad?</td></tr>
  <tr><td>Uso efectivo por el equipo</td><td>¿La herramienta se usa o quedó en el cajón?</td></tr>
</table>

<h2>Errores frecuentes</h2>
<ul>
  <li>Automatizar varios procesos a la vez.</li>
  <li>No medir la situación inicial (después no hay con qué comparar).</li>
  <li>Delegar la implementación sin un responsable interno.</li>
  <li>Elegir herramientas por moda y no por el problema a resolver.</li>
</ul>
""",
    "faq": [
      ("¿Cuánto cuesta implementar IA en una PyME?", "Depende del proceso y de las herramientas. Muchas herramientas de uso general tienen planes accesibles; el costo principal suele ser el tiempo del equipo para ordenar procesos y probar. Por eso conviene empezar con un piloto chico y medido."),
      ("¿Necesito contratar un programador para empezar?", "No. Las primeras implementaciones en una PyME suelen hacerse con herramientas de uso general y automatizaciones sin código. Un perfil técnico se vuelve necesario cuando se integran sistemas propios."),
      ("¿Por qué proceso conviene empezar?", "Por uno repetitivo, frecuente, con impacto económico visible y bajo riesgo si algo sale mal. Por ejemplo: respuestas a consultas frecuentes, carga de datos o armado de reportes."),
    ],
  },
  {
    "slug": "ia-en-empresas-familiares",
    "title": "IA en empresas familiares: cómo profesionalizar sin perder la esencia",
    "desc": "Cómo usar la inteligencia artificial para profesionalizar una empresa familiar: roles claros, decisiones con datos y menor dependencia del fundador.",
    "answer": "En una empresa familiar, la IA sirve sobre todo para profesionalizar: ordenar la información, generar reportes que no dependan de una persona, documentar procesos y reducir la dependencia del fundador. Funciona cuando primero se aclaran roles y procesos; si se implementa sobre el desorden, lo amplifica.",
    "charla": "empresa-familiar-e-ia",
    "body": """
<h2>El problema no es la tecnología</h2>
<p>En las empresas familiares los cuellos de botella suelen ser los mismos: roles difusos, decisiones que pasan por una sola persona, información que vive en la cabeza del fundador y conversaciones de negocio que se mezclan con conversaciones de familia.</p>
<p>Ninguna herramienta resuelve eso sola. Pero bien usada, la IA puede acelerar la profesionalización.</p>

<h2>Dónde ayuda la IA en una empresa familiar</h2>
<ul>
  <li><strong>Información:</strong> centralizar datos dispersos y generar reportes periódicos que cualquiera de los socios pueda leer.</li>
  <li><strong>Procesos:</strong> documentar cómo se hacen las cosas a partir de grabaciones y transcripciones, para que el conocimiento no se pierda.</li>
  <li><strong>Decisiones:</strong> preparar escenarios y resúmenes que ordenen las reuniones de socios.</li>
  <li><strong>Comunicación interna:</strong> manuales, respuestas frecuentes y capacitación de personal nuevo.</li>
</ul>

<h2>La trampa del fundador indispensable</h2>
<p>Una pregunta sirve de diagnóstico: <em>¿qué pasaría si el fundador no estuviera dos semanas?</em> Si la respuesta es \"se frena todo\", la prioridad no es comprar herramientas sino transferir conocimiento. La IA puede ayudar en esa transferencia, pero la decisión de soltar es humana.</p>

<h2>Cómo involucrar a la siguiente generación</h2>
<p>La tecnología muchas veces es el terreno donde la nueva generación se siente más cómoda. Usarla como proyecto compartido, con objetivos y métricas claras, ordena la conversación entre generaciones en lugar de enfrentarla.</p>
<ol>
  <li>Definir un proyecto acotado (por ejemplo, el reporte mensual de ventas).</li>
  <li>Asignar un responsable de la nueva generación y un referente de la anterior.</li>
  <li>Medir el resultado y presentarlo en la reunión de socios.</li>
</ol>

<h2>Orden recomendado</h2>
<p>Primero roles y responsables. Después procesos escritos. Después IA. Es el mismo orden del Método ONDA, aplicado a la realidad de una empresa familiar.</p>
<p>Los temas societarios, legales o sucesorios requieren asesoramiento profesional específico. La IA no reemplaza esas conversaciones.</p>
""",
    "faq": [
      ("¿La IA puede ayudar en la sucesión de una empresa familiar?", "Puede ayudar a documentar conocimiento y procesos, lo que facilita la transición. Las decisiones societarias, legales y familiares requieren asesoramiento profesional específico."),
      ("¿Por dónde empieza una empresa familiar con IA?", "Por un problema concreto y medible: reportes que dependen de una persona, consultas repetidas de clientes o procesos que solo conoce alguien. Antes, conviene aclarar quién es responsable de cada área."),
    ],
  },
  {
    "slug": "como-elegir-una-capacitacion-de-ia-para-empresas",
    "title": "Cómo elegir una capacitación de IA para tu empresa: 7 criterios",
    "desc": "Siete criterios para elegir una capacitación o charla de inteligencia artificial para empresas y PyMEs, y qué preguntarle al capacitador antes de contratar.",
    "answer": "Una buena capacitación de IA para empresas habla de procesos de negocio y no solo de herramientas, la dicta alguien con experiencia operando empresas, se adapta al rubro y al nivel del equipo, termina con un entregable concreto y propone métricas para medir el resultado. El formato online en vivo permite sumar a todo el equipo sin costos de traslado.",
    "charla": "ia-sin-humo-para-duenos-de-pymes",
    "body": """
<h2>Los 7 criterios</h2>
<ol>
  <li><strong>Habla de procesos, no solo de herramientas.</strong> Las herramientas cambian cada mes. El criterio para decidir dónde aplicarlas, no.</li>
  <li><strong>Quien la dicta operó una empresa.</strong> Saber de IA no alcanza: hay que entender caja, equipo, clientes y prioridades.</li>
  <li><strong>Se adapta al rubro y al nivel.</strong> No es lo mismo un equipo administrativo que un directorio.</li>
  <li><strong>Termina con un entregable.</strong> Un plan, un proceso documentado o un piloto definido. No solo inspiración.</li>
  <li><strong>Propone métricas.</strong> Tiempo, costo y errores. Si no se mide, no se sabe si sirvió.</li>
  <li><strong>Es en vivo y con preguntas.</strong> Las dudas reales del equipo son la mitad del valor.</li>
  <li><strong>Tiene continuidad.</strong> Material de apoyo y un camino claro para el paso siguiente.</li>
</ol>

<h2>Qué formato elegir</h2>
<table>
  <tr><th>Formato</th><th>Objetivo</th><th>Ideal para</th></tr>
  <tr><td>Charla online (45–60 min)</td><td>Alinear y dar criterio</td><td>Eventos, cámaras, reuniones de equipo</td></tr>
  <tr><td>Capacitación in-company (varias sesiones)</td><td>Que cada área tenga casos de uso propios</td><td>Equipos de una misma empresa</td></tr>
  <tr><td>Workshop para dueños</td><td>Salir con un plan de adopción</td><td>Dueños y directivos, grupos reducidos</td></tr>
</table>

<h2>Preguntas para hacerle al capacitador antes de contratar</h2>
<ul>
  <li>¿Qué va a poder hacer distinto mi equipo el lunes siguiente?</li>
  <li>¿Cómo adaptás los ejemplos a mi rubro?</li>
  <li>¿Qué material queda después de la capacitación?</li>
  <li>¿Cómo medimos si funcionó?</li>
  <li>¿Cuál es tu experiencia operando empresas, no solo enseñando?</li>
</ul>

<h2>Señales de alerta</h2>
<ul>
  <li>Promesas de resultados garantizados.</li>
  <li>Temarios que son solo listas de herramientas.</li>
  <li>Ninguna mención a procesos, responsables o métricas.</li>
</ul>
""",
    "faq": [
      ("¿Conviene una capacitación de IA online o presencial?", "Online en vivo permite sumar a equipos distribuidos, grabar el contenido para quien no pudo asistir y evitar costos de traslado. Lo importante es que sea en vivo y con espacio para preguntas."),
      ("¿Cuántas personas pueden participar?", "Una charla no tiene límite práctico. Para capacitaciones con ejercicios o workshops conviene trabajar con grupos reducidos para que todos participen."),
      ("¿Cuánto dura una capacitación de IA para empresas?", "Una charla dura entre 45 y 60 minutos. Una capacitación in-company suele organizarse en 2 a 4 sesiones según los objetivos."),
    ],
  },
  {
    "slug": "que-es-geo-y-como-hacer-que-la-ia-recomiende-tu-negocio",
    "title": "Qué es GEO y cómo lograr que ChatGPT recomiende tu negocio",
    "desc": "Qué es GEO (Generative Engine Optimization), en qué se diferencia del SEO y un checklist de 10 puntos para que una PyME aparezca en respuestas de ChatGPT, Gemini y Perplexity.",
    "answer": "GEO (Generative Engine Optimization) es el conjunto de prácticas para que un negocio aparezca y sea citado en las respuestas de motores de IA generativa como ChatGPT, Gemini o Perplexity. Se basa en describir el negocio de forma clara y consistente, responder preguntas reales de los clientes y tener presencia en fuentes confiables.",
    "charla": "visibilidad-en-ia-geo-para-pymes",
    "body": """
<h2>Por qué importa ahora</h2>
<p>Cada vez más personas le preguntan a una IA \"¿quién me recomendás para…?\" en lugar de revisar una lista de links. La IA responde con unos pocos nombres. Si tu negocio no está entre las fuentes que la IA encuentra y entiende, no aparece.</p>

<h2>GEO vs. SEO</h2>
<table>
  <tr><th></th><th>SEO</th><th>GEO</th></tr>
  <tr><td>Objetivo</td><td>Posicionar un link en un buscador</td><td>Ser mencionado o citado en una respuesta</td></tr>
  <tr><td>Unidad</td><td>Página y palabra clave</td><td>Entidad (negocio, persona, método) y pregunta</td></tr>
  <tr><td>Clave</td><td>Relevancia y autoridad</td><td>Claridad, consistencia y fuentes confiables</td></tr>
</table>
<p>No compiten: buena parte de las bases del SEO sigue siendo necesaria para GEO.</p>

<h2>Checklist de 10 puntos para una PyME</h2>
<ol>
  <li>Una frase que defina tu negocio sin ambigüedad: qué hacés, para quién y dónde.</li>
  <li>El mismo nombre, descripción y datos en el sitio, Google Business, LinkedIn y redes.</li>
  <li>Una página por servicio, con su propio título y descripción.</li>
  <li>Preguntas frecuentes reales, respondidas en la primera oración.</li>
  <li>Datos estructurados (schema.org) que describan negocio, servicios y personas.</li>
  <li>Una página \"sobre nosotros\" con experiencia comprobable.</li>
  <li>Reseñas y menciones en sitios de terceros.</li>
  <li>Contenido que responde preguntas de clientes, no solo promociones.</li>
  <li>Un sitio rápido y accesible para los rastreadores de IA (robots.txt y llms.txt).</li>
  <li>Fecha de actualización visible y contenido revisado periódicamente.</li>
</ol>

<h2>Cómo medir si la IA te menciona</h2>
<p>Una vez por mes, hacé las mismas preguntas a ChatGPT, Gemini y Perplexity, del modo en que las haría un cliente (por ejemplo: \"¿quién da capacitaciones de IA para PyMEs en Argentina?\"). Registrá si aparecés, en qué posición y qué fuente citan. Es una medición imperfecta, pero muestra la tendencia.</p>

<h2>Lo que no funciona</h2>
<ul>
  <li>Repetir palabras clave sin aportar información.</li>
  <li>Descripciones distintas del negocio en cada perfil.</li>
  <li>Promesas de \"aparecer primero en ChatGPT\": nadie puede garantizarlo.</li>
</ul>
""",
    "faq": [
      ("¿Qué significa GEO?", "GEO significa Generative Engine Optimization: optimización para motores de IA generativa. Busca que un negocio sea entendido y citado por herramientas como ChatGPT, Gemini o Perplexity."),
      ("¿Cuánto tarda en verse resultado?", "No hay un plazo fijo. Los motores de IA actualizan sus fuentes en tiempos distintos. Lo recomendable es trabajar la base y medir mes a mes."),
      ("¿Qué es el archivo llms.txt?", "Es un archivo de texto en la raíz del sitio que resume, en lenguaje simple, qué es el negocio y cuáles son sus páginas principales, para que los modelos de IA lo interpreten mejor."),
    ],
  },
]

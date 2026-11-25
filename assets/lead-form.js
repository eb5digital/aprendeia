/* Formulario de contacto Aprendeia → base de datos propia (Supabase).
   La clave es "publishable": está pensada para ir en el navegador.
   La tabla solo permite INSERTAR (RLS); nadie puede leer los contactos desde el sitio. */
(function () {
  var CONFIG = {
    url: "__SUPABASE_URL__",
    key: "__SUPABASE_PUBLISHABLE_KEY__",
    table: "leads"
  };

  var form = document.getElementById("lead-form");
  if (!form) return;
  var ok = document.getElementById("lead-ok");
  var msg = form.querySelector(".form-msg");
  var btn = form.querySelector('button[type="submit"]');
  var STORE = "aprendeia_lead";

  function showOk() {
    form.style.display = "none";
    ok.style.display = "block";
    ok.focus();
  }
  // Si ya dejó sus datos antes, no se los pedimos de nuevo.
  try { if (localStorage.getItem(STORE)) showOk(); } catch (e) {}

  function utm(name) {
    var v = new URLSearchParams(location.search).get(name);
    return v ? v.slice(0, 100) : null;
  }
  function setErr(input, bad) { input.setAttribute("aria-invalid", bad ? "true" : "false"); }
  ["nombre", "email", "telefono"].forEach(function (n) {
    form[n].addEventListener("input", function () { form[n].setAttribute("aria-invalid", "false"); });
  });

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    msg.textContent = ""; msg.className = "form-msg";
    if (form.web.value) { showOk(); return; } // trampa para bots

    var nombre = form.nombre.value.trim();
    var email = form.email.value.trim().toLowerCase();
    var tel = form.telefono.value.trim();
    var vN = nombre.length >= 2;
    var vE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email);
    var vT = tel.replace(/\D/g, "").length >= 8;
    setErr(form.nombre, !vN); setErr(form.email, !vE); setErr(form.telefono, !vT);
    if (!(vN && vE && vT)) {
      msg.textContent = "Revisá los datos marcados: nombre, un email válido y un teléfono con código de área.";
      msg.className = "form-msg err";
      return;
    }

    btn.disabled = true; btn.textContent = "Enviando…";
    fetch(CONFIG.url + "/rest/v1/" + CONFIG.table, {
      method: "POST",
      headers: {
        "apikey": CONFIG.key,
        "Authorization": "Bearer " + CONFIG.key,
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
      },
      body: JSON.stringify({
        nombre: nombre, email: email, telefono: tel,
        origen: "hoja-de-ruta-onda",
        pagina: location.pathname,
        referrer: document.referrer ? document.referrer.slice(0, 300) : null,
        utm_source: utm("utm_source"), utm_medium: utm("utm_medium"), utm_campaign: utm("utm_campaign")
      })
    }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      try { localStorage.setItem(STORE, "1"); } catch (e) {}
      if (window.gtag) gtag("event", "generate_lead", { method: "form", lead_source: "hoja-de-ruta-onda", page_path: location.pathname });
      showOk();
    }).catch(function () {
      msg.innerHTML = 'No pudimos guardar tus datos. Probá de nuevo o <a href="https://wa.me/5491125534340?text=Hola%20Emiliano%2C%20quiero%20la%20Hoja%20de%20Ruta%20del%20M%C3%A9todo%20ONDA." target="_blank" rel="noopener" style="color:var(--acc)">pedila por WhatsApp</a>.';
      msg.className = "form-msg err";
      btn.disabled = false; btn.textContent = "Recibir la Hoja de Ruta →";
    });
  });

  ok.querySelectorAll("[data-dl]").forEach(function (a) {
    a.addEventListener("click", function () { if (window.gtag) gtag("event", "file_download", { file_name: "metodo-onda-hoja-de-ruta.pdf" }); });
  });
  ok.querySelectorAll("[data-cta]").forEach(function (a) {
    a.addEventListener("click", function () { if (window.gtag) gtag("event", "generate_lead", { method: "whatsapp", cta_position: a.dataset.cta, page_path: location.pathname }); });
  });
})();

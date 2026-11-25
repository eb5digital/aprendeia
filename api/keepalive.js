// Ping diario (Vercel Cron) para que el proyecto gratuito de Supabase no se pause por inactividad.
const URL = "https://tglzjejpyipxundiszrv.supabase.co/rest/v1/rpc/ping";
const KEY = "sb_publishable_0UzXjBrPsoGPMmjnqPzSQA_KHRw-XQC"; // clave pública (la misma del formulario)

module.exports = async (req, res) => {
  try {
    const r = await fetch(URL, { method: "POST", headers: { apikey: KEY, "Content-Type": "application/json" }, body: "{}" });
    res.status(r.ok ? 200 : 502).json({ supabase: r.status, at: new Date().toISOString() });
  } catch (e) {
    res.status(502).json({ error: String(e) });
  }
};

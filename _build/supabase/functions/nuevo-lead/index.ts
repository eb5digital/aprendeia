// Edge Function: avisa por email cada contacto nuevo de aprendeia.com.ar.
// La dispara un trigger de la tabla leads (pg_net) con { id }.
// Lee el contacto con el rol de servicio: un llamado externo no puede inyectar datos,
// y solo notifica contactos reales que todavía no fueron notificados.
// Secrets necesarios: RESEND_API_KEY, NOTIFY_TO (email de destino).
import { createClient } from "jsr:@supabase/supabase-js@2";

const esc = (s: unknown) =>
  String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("method not allowed", { status: 405 });
  let id = "";
  try { id = (await req.json())?.id ?? ""; } catch { /* body inválido */ }
  if (!/^[0-9a-f-]{36}$/i.test(id)) return new Response("bad id", { status: 400 });

  const key = Deno.env.get("RESEND_API_KEY");
  const to = Deno.env.get("NOTIFY_TO");
  if (!key || !to) return new Response("notificación no configurada", { status: 200 });

  const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: lead } = await db.from("leads").select("*").eq("id", id).is("notificado_at", null).maybeSingle();
  if (!lead) return new Response("nada para notificar", { status: 200 });

  const tel = String(lead.telefono ?? "").replace(/\D/g, "");
  const nombre = String(lead.nombre ?? "").split(" ")[0];
  const waMsg = encodeURIComponent(`Hola ${nombre}, soy Emiliano Bugliolo de Aprendeia. Vi que descargaste la Hoja de Ruta del Método ONDA. ¿Te puedo ayudar con algo?`);
  const fecha = new Date(lead.created_at).toLocaleString("es-AR", { timeZone: "America/Argentina/Buenos_Aires" });
  const fila = (k: string, v: unknown) => v ? `<tr><td style="padding:6px 12px 6px 0;color:#667">${k}</td><td style="padding:6px 0"><b>${esc(v)}</b></td></tr>` : "";

  const html = `<div style="font-family:Arial,sans-serif;max-width:560px">
  <h2 style="margin:0 0 6px">Nuevo contacto en Aprendeia</h2>
  <p style="color:#667;margin:0 0 16px">${esc(fecha)} · ${esc(lead.origen)}</p>
  <table style="border-collapse:collapse;font-size:15px">
    ${fila("Nombre", lead.nombre)}${fila("Email", lead.email)}${fila("Teléfono", lead.telefono)}
    ${fila("Página", lead.pagina)}${fila("Llegó desde", lead.referrer)}
    ${fila("Campaña", [lead.utm_source, lead.utm_medium, lead.utm_campaign].filter(Boolean).join(" / "))}
  </table>
  <p style="margin:20px 0">
    <a href="https://wa.me/${tel}?text=${waMsg}" style="background:#00E5A0;color:#04120C;padding:12px 18px;border-radius:8px;text-decoration:none;font-weight:bold">Escribirle por WhatsApp</a>
    &nbsp;<a href="mailto:${esc(lead.email)}" style="color:#0a7;font-weight:bold">Responder por email</a>
  </p>
  <p style="color:#99a;font-size:12px">Regla: contactarlo dentro de las 24 h. Todos los contactos: Supabase → proyecto aprendeia → Table Editor → leads.</p>
</div>`;

  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: "Aprendeia <onboarding@resend.dev>",
      to: [to],
      reply_to: lead.email,
      subject: `Nuevo contacto: ${lead.nombre}`,
      html,
    }),
  });
  if (!r.ok) {
    console.error("resend", r.status, await r.text());
    return new Response("error enviando email", { status: 502 });
  }
  await db.from("leads").update({ notificado_at: new Date().toISOString() }).eq("id", id);
  return new Response("ok", { status: 200 });
});

-- Base de contactos de Aprendeia.
-- El sitio solo puede INSERTAR. Leer, editar y borrar: solo desde el panel de Supabase.

create table if not exists public.leads (
  id           uuid primary key default gen_random_uuid(),
  created_at   timestamptz not null default now(),
  nombre       text not null check (char_length(nombre) between 2 and 120),
  email        text not null check (char_length(email) <= 160 and email ~* '^[^@\s]+@[^@\s]+\.[^@\s]{2,}$'),
  telefono     text not null check (char_length(telefono) between 6 and 30),
  origen       text check (char_length(origen) <= 60),
  pagina       text check (char_length(pagina) <= 200),
  referrer     text check (char_length(referrer) <= 300),
  utm_source   text check (char_length(utm_source) <= 100),
  utm_medium   text check (char_length(utm_medium) <= 100),
  utm_campaign text check (char_length(utm_campaign) <= 100),
  estado       text not null default 'nuevo',
  notas        text
);

create index if not exists leads_created_at_idx on public.leads (created_at desc);
create index if not exists leads_email_idx on public.leads (lower(email));

alter table public.leads enable row level security;

-- El público (anon) solo puede insertar, y no puede elegir estado ni notas.
revoke all on public.leads from anon, authenticated;
grant insert (nombre, email, telefono, origen, pagina, referrer, utm_source, utm_medium, utm_campaign) on public.leads to anon;

drop policy if exists "sitio puede insertar contactos" on public.leads;
create policy "sitio puede insertar contactos"
  on public.leads for insert to anon
  with check (estado = 'nuevo' and notas is null);

-- Vista práctica para revisar contactos (solo visible desde el panel / rol de servicio).
create or replace view public.leads_recientes with (security_invoker = true) as
  select created_at at time zone 'America/Argentina/Buenos_Aires' as fecha_ar,
         nombre, email, telefono, origen, utm_source, estado, notas
  from public.leads order by created_at desc;
revoke all on public.leads_recientes from anon, authenticated;

-- 002: ping para el keepalive diario (Vercel Cron → /api/keepalive)
create or replace function public.ping()
returns text language sql stable security invoker set search_path = ''
as $$ select 'ok'::text $$;
revoke all on function public.ping() from public;
grant execute on function public.ping() to anon;

-- 003: aviso por email de cada contacto nuevo (trigger → Edge Function nuevo-lead → Resend)
create extension if not exists pg_net with schema extensions;
alter table public.leads add column if not exists notificado_at timestamptz;
create or replace function public.notify_new_lead() returns trigger language plpgsql security definer set search_path = ''
as $$ begin
  perform net.http_post(url := 'https://tglzjejpyipxundiszrv.supabase.co/functions/v1/nuevo-lead',
    headers := jsonb_build_object('Content-Type','application/json'), body := jsonb_build_object('id', new.id));
  return new; end; $$;
revoke all on function public.notify_new_lead() from public, anon, authenticated;
drop trigger if exists leads_notify on public.leads;
create trigger leads_notify after insert on public.leads for each row execute function public.notify_new_lead();

create table if not exists public.revele_boloes (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  titulo text not null,
  data_prevista date,
  created_by text,
  admin_key text not null,
  resultado text check (resultado in ('menino','menina') or resultado is null),
  unlocked boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists public.revele_palpites (
  id uuid primary key default gen_random_uuid(),
  bolao_id uuid not null references public.revele_boloes(id) on delete cascade,
  nome text,
  sexo text not null check (sexo in ('menino','menina')),
  nome_sugerido text,
  data_palpite date,
  peso_kg numeric,
  created_at timestamptz not null default now()
);

create table if not exists public.revele_eventos (
  id uuid primary key default gen_random_uuid(),
  evento text not null,
  slug text,
  meta jsonb,
  created_at timestamptz not null default now()
);

alter table public.revele_boloes enable row level security;
alter table public.revele_palpites enable row level security;
alter table public.revele_eventos enable row level security;

drop policy if exists revele_boloes_insert on public.revele_boloes;
create policy revele_boloes_insert on public.revele_boloes for insert to anon with check (true);
drop policy if exists revele_boloes_select on public.revele_boloes;
create policy revele_boloes_select on public.revele_boloes for select to anon using (true);

drop policy if exists revele_palpites_insert on public.revele_palpites;
create policy revele_palpites_insert on public.revele_palpites for insert to anon with check (true);
drop policy if exists revele_palpites_select on public.revele_palpites;
create policy revele_palpites_select on public.revele_palpites for select to anon using (true);

drop policy if exists revele_eventos_insert on public.revele_eventos;
create policy revele_eventos_insert on public.revele_eventos for insert to anon with check (true);

revoke update, delete on public.revele_boloes from anon;
revoke update, delete on public.revele_palpites from anon;
revoke select, update, delete on public.revele_eventos from anon;

-- admin_key nunca deve ser legível pelo cliente (mesmo padrão do murai_murais)
revoke select on public.revele_boloes from anon;
grant select (id, slug, titulo, data_prevista, created_by, resultado, unlocked, created_at) on public.revele_boloes to anon;

-- FIX P0 (validação do time, 2026-09-22): resultado é o segredo do produto — não pode vazar
-- pra qualquer visitante antes do pagamento. Bloqueia a coluna via REST e expõe só através
-- de uma view que mascara o valor até o bolão estar `unlocked` (pago). O organizador consegue
-- ler/gravar o resultado antes disso só via Edge Function revele-admin (service_role + admin_key).
revoke select (resultado) on public.revele_boloes from anon;

create or replace view public.revele_boloes_public as
select id, slug, titulo, data_prevista, created_by, unlocked, created_at,
       case when unlocked then resultado else null end as resultado
from public.revele_boloes;

grant select on public.revele_boloes_public to anon;
-- o client (index.html) lê de revele_boloes_public, nunca direto de revele_boloes.

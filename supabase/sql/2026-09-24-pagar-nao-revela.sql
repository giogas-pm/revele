-- P0 (squad 2026-09-24): pagar != revelar; resultado só público após o organizador revelar; fim da listagem anônima.
alter table public.revele_boloes add column if not exists revealed_at timestamptz;

drop policy if exists revele_boloes_select on public.revele_boloes;
drop policy if exists revele_palpites_select on public.revele_palpites;
revoke select on public.revele_boloes_public from anon;
revoke select on public.revele_palpites from anon;

create or replace function public.revele_get(p_slug text) returns json
language sql stable security definer set search_path = public as $$
  select json_build_object(
    'id', b.id, 'slug', b.slug, 'titulo', b.titulo, 'data_prevista', b.data_prevista,
    'created_by', b.created_by, 'unlocked', b.unlocked, 'created_at', b.created_at,
    'revealed', b.revealed_at is not null,
    'resultado', case when b.revealed_at is not null then b.resultado else null end,
    'palpites', coalesce((select json_agg(json_build_object('id', p.id, 'nome', p.nome, 'sexo', p.sexo,
                           'nome_sugerido', p.nome_sugerido, 'data_palpite', p.data_palpite, 'peso_kg', p.peso_kg,
                           'created_at', p.created_at) order by p.created_at asc)
                          from revele_palpites p where p.bolao_id = b.id), '[]'::json))
  from revele_boloes b where b.slug = p_slug
$$;
revoke all on function public.revele_get(text) from public;
grant execute on function public.revele_get(text) to anon, authenticated;

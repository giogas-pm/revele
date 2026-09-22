// Revelê — ações de DONO do bolão (revelar resultado, remover palpite), autenticadas por admin_key.
// O dono guarda a admin_key na URL (#b=slug&k=...). Mesma receita do Muraí (mural-admin).
const SB_URL = Deno.env.get("SUPABASE_URL")!;
const SVC = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const H = { apikey: SVC, Authorization: "Bearer " + SVC, "Content-Type": "application/json" };
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
function json(obj: unknown, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { ...CORS, "Content-Type": "application/json" } });
}
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const { slug, key, action, palpite_id, resultado } = await req.json().catch(() => ({} as any));
    if (!slug || !key) return json({ ok: false, motivo: "faltam_dados" }, 400);
    const rows = await fetch(
      `${SB_URL}/rest/v1/revele_boloes?slug=eq.${encodeURIComponent(slug)}&select=id,admin_key`,
      { headers: H },
    ).then((r) => r.json());
    if (!rows.length) return json({ ok: false, motivo: "bolao_inexistente" }, 404);
    if (!rows[0].admin_key || rows[0].admin_key !== key) return json({ ok: false, motivo: "nao_autorizado" }, 403);
    const bolaoId = rows[0].id;
    if (action === "delete_palpite") {
      if (!palpite_id) return json({ ok: false, motivo: "sem_palpite" }, 400);
      await fetch(
        `${SB_URL}/rest/v1/revele_palpites?id=eq.${encodeURIComponent(palpite_id)}&bolao_id=eq.${bolaoId}`,
        { method: "DELETE", headers: { ...H, Prefer: "return=minimal" } },
      );
      return json({ ok: true });
    }
    if (action === "set_resultado") {
      if (resultado !== "menino" && resultado !== "menina") return json({ ok: false, motivo: "resultado_invalido" }, 400);
      await fetch(
        `${SB_URL}/rest/v1/revele_boloes?id=eq.${bolaoId}`,
        { method: "PATCH", headers: { ...H, Prefer: "return=minimal" }, body: JSON.stringify({ resultado }) },
      );
      return json({ ok: true });
    }
    return json({ ok: false, motivo: "acao_desconhecida" }, 400);
  } catch (e) {
    return json({ ok: false, motivo: "excecao", detalhe: String(e) }, 200);
  }
});

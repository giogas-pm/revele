// Revelê — métricas do funil (agregadas), pra rotinas de monitoramento lerem sem segredo local.
// GET /revele-metrics?k=<METRICS_KEY> -> JSON com contagens do funil.
// Usa service_role (server-side). Protegido por METRICS_KEY (mesmo secret do projeto, já setado).
const SB_URL = Deno.env.get("SUPABASE_URL")!;
const SVC = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const KEY = Deno.env.get("METRICS_KEY") || "";
const H = { apikey: SVC, Authorization: "Bearer " + SVC };
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
};
function json(obj: unknown, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { ...CORS, "Content-Type": "application/json" } });
}
async function countOf(pathFilter: string): Promise<number> {
  const sep = pathFilter.includes("?") ? "&" : "?";
  const r = await fetch(`${SB_URL}/rest/v1/${pathFilter}${sep}select=id`, {
    headers: { ...H, Prefer: "count=exact", Range: "0-0" },
  });
  const cr = r.headers.get("content-range") || "*/0";
  return parseInt(cr.split("/")[1] || "0", 10);
}
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const url = new URL(req.url);
  if (KEY && url.searchParams.get("k") !== KEY) return json({ ok: false, motivo: "nao_autorizado" }, 401);
  try {
    const [
      boloes_total, boloes_pagos, palpites_total,
      ev_visit, ev_seoland,
      ev_bolao_created, ev_palpite, ev_paywall, ev_checkout,
    ] = await Promise.all([
      countOf("revele_boloes"),
      countOf("revele_boloes?unlocked=eq.true"),
      countOf("revele_palpites"),
      countOf("revele_eventos?evento=eq.visit"),
      countOf("revele_eventos?evento=eq.seo_land"),
      countOf("revele_eventos?evento=eq.bolao_created"),
      countOf("revele_eventos?evento=eq.palpite_added"),
      countOf("revele_eventos?evento=eq.paywall_view"),
      countOf("revele_eventos?evento=eq.checkout_open"),
    ]);
    return json({
      ok: true,
      as_of: new Date().toISOString(),
      receita_estimada: boloes_pagos * 29,
      boloes_pagos,
      boloes_total,
      palpites_total,
      funil: {
        visit: ev_visit,
        seo_land: ev_seoland,
        bolao_created: ev_bolao_created,
        palpite_added: ev_palpite,
        paywall_view: ev_paywall,
        checkout_open: ev_checkout,
      },
    });
  } catch (e) {
    return json({ ok: false, motivo: "excecao", detalhe: String(e) }, 200);
  }
});

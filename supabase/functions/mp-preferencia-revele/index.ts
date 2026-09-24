// Revelê — cria a preferência de pagamento (R$29) no Mercado Pago e devolve o link do checkout.
// Mesma receita do Muraí (mp-preferencia), adaptada pra tabela revele_boloes.
const REF = "diemqzngskmcuytkzjhr";
const WEBHOOK_URL = `https://${REF}.supabase.co/functions/v1/mp-webhook-revele`;
const SITE = "https://giogas-pm.github.io/revele/";
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
function json(obj: unknown) {
  return new Response(JSON.stringify(obj), { headers: { ...CORS, "Content-Type": "application/json" } });
}
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const token = Deno.env.get("MP_ACCESS_TOKEN");
    if (!token) return json({ ok: false, motivo: "sem_token" });
    const { slug, titulo } = await req.json().catch(() => ({} as any));
    if (!slug) return json({ ok: false, motivo: "sem_slug" });
    const nome = ("Revelê — revelação de " + (titulo || "um bebê especial")).slice(0, 240);
    const pref = {
      items: [{ title: nome, quantity: 1, unit_price: 19.9, currency_id: "BRL" }],
      external_reference: String(slug),
      metadata: { slug: String(slug) },
      statement_descriptor: "REVELE",
      notification_url: WEBHOOK_URL,
      back_urls: {
        success: `${SITE}?pago=ok#b=${slug}`,
        pending: `${SITE}?pago=pendente#b=${slug}`,
        failure: `${SITE}?pago=falhou#b=${slug}`,
      },
      auto_return: "approved",
    };
    const r = await fetch("https://api.mercadopago.com/checkout/preferences", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: "Bearer " + token },
      body: JSON.stringify(pref),
    });
    const j = await r.json();
    if (j && j.init_point) return json({ ok: true, init_point: j.init_point });
    return json({ ok: false, motivo: "mp_erro", detalhe: (j && (j.message || j.error)) || null });
  } catch (e) {
    return json({ ok: false, motivo: "excecao", detalhe: String(e) });
  }
});

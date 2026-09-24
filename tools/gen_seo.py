# -*- coding: utf-8 -*-
"""Gerador de paginas de SEO programatico do Revele. Template + dados -> HTML estatico.
Rodar de dentro de apps/revele:  python tools/gen_seo.py .
Cada pagina tem conteudo UNICO (anti-doorway): lead/why/guia/lista/FAQ proprios."""
import os, html, json, sys
from urllib.parse import quote

REPO = sys.argv[1] if len(sys.argv) > 1 else "."
BASE = "https://giogas-pm.github.io/revele"
OUT_DIR = os.path.join(REPO, "cha-revelacao")

def e(s): return html.escape(s, quote=True)

# FAQ comum a todas (so preco + atrito de conta; curta p/ nao virar boilerplate)
FAQ_COMUM = [
    ("Quanto custa?",
     "Criar o bolão e coletar quantos palpites quiser é de graça. Você só paga uma vez (R$19,90), se quiser, para liberar a revelação em tela cheia na festa e o ranking de quem acertou. Não tem assinatura."),
    ("Os convidados precisam instalar app ou criar conta?",
     "Não. Cada pessoa só abre o link no navegador do celular, escolhe menino ou menina e pronto. Sem download, sem cadastro."),
]

def cta_href():
    return "/revele/?src=seo"

# ---------- PAGINAS (conteudo unico por pagina) ----------
PAGES = [
{
 "slug":"bolao-de-cha-revelacao","kw":"bolão de chá revelação online",
 "title":"Bolão de Chá Revelação Online — Crie Grátis (Menino ou Menina) | Revelê",
 "h1":"Crie um bolão de chá revelação online e grátis",
 "desc":"Monte um bolão de chá revelação online grátis. Os convidados palpitam menino ou menina, nome e data — e você revela com animação e o ranking de quem acertou.",
 "lead":"O bolão é a alma do chá revelação: todo mundo aposta se vem menino ou menina e a graça é descobrir quem cravou. Só que anotar palpite em papelzinho ou no grupo do WhatsApp vira bagunça — some, ninguém confere e, no fim, ninguém sabe quem ganhou. Com um bolão online você manda um único link, cada convidado registra o palpite em segundos e o placar se atualiza sozinho.",
 "why":"Um bolão digital tira o trabalho manual e deixa tudo mais divertido: placar ao vivo de menino x menina, palpite de nome, data e peso, e uma revelação animada na hora H com o ranking de quem acertou. Funciona no celular, sem app e sem cadastro para os convidados — e você guarda o resultado em segredo até o grande momento.",
 "guide":[
   "Crie o bolão e mande o link no grupo da família de 1 a 2 semanas antes do chá.",
   "Peça que cada um arrisque também o nome e a data do nascimento — rende risada e engaja mais gente.",
   "Guarde o resultado em segredo no app e só toque em \"Revelar\" na hora da festa, com todo mundo reunido.",
 ],
 "list_title":"Mensagens prontas para convidar a galera pro bolão",
 "list_intro":"Copie e cole no grupo do WhatsApp para todo mundo palpitar:",
 "list_items":[
   "Vem aí o chá revelação do nosso bebê! 💙💗 Menino ou menina? Deixa seu palpite: [link]",
   "Bolão do bebê tá aberto! Arrisca o sexo, o nome e a data do nascimento. Quem será que acerta? [link]",
   "Participa do nosso bolão de chá revelação! É rapidinho e vale a honra de ter acertado 😄 [link]",
   "Palpite valendo: você acha que vem príncipe ou princesa? Registra aqui: [link]",
   "Antes da revelação, queremos o SEU palpite! Menino ou menina? [link]",
 ],
 "faq":[
   ("Dá para todo mundo ver os palpites dos outros?","Sim. A página mostra o placar ao vivo (quantos votaram menino e quantos menina) e os palpites de nome e data de cada convidado — só o resultado verdadeiro fica em segredo até você revelar."),
 ],
},
{
 "slug":"cha-revelacao-online","kw":"chá revelação online",
 "title":"Chá Revelação Online e à Distância — Faça o Bolão Grátis | Revelê",
 "h1":"Chá revelação online: junte todo mundo, mesmo de longe",
 "desc":"Faça um chá revelação online e à distância. Parentes de qualquer cidade palpitam menino ou menina pelo link e assistem à revelação juntos por chamada de vídeo. Grátis.",
 "lead":"Nem sempre dá para reunir a família toda no mesmo lugar — avós em outra cidade, amigos que moram longe, padrinhos viajando. Um chá revelação online resolve: todo mundo palpita menino ou menina pelo link, de onde estiver, e você revela o resultado ao vivo, numa chamada de vídeo com a família inteira assistindo.",
 "why":"Fazer o chá revelação online amplia a festa: em vez de só quem foi presencialmente, todos os que amam o bebê participam. O bolão fica aberto por dias, o placar se atualiza sozinho e, no momento da revelação, você compartilha a tela com a animação de \"é menino\" ou \"é menina\" para todo mundo ao mesmo tempo.",
 "guide":[
   "Combine um horário de chamada de vídeo (WhatsApp, Meet ou Zoom) para a revelação ao vivo.",
   "Deixe o bolão aberto por alguns dias antes, para quem está em outro fuso conseguir palpitar.",
   "Na hora, compartilhe a tela do celular ou computador e toque em \"Revelar\" para todos verem a animação juntos.",
 ],
 "list_title":"Dicas para um chá revelação por chamada de vídeo",
 "list_intro":"Para a revelação à distância sair redondinha:",
 "list_items":[
   "Teste a conexão antes: deixe o celular no wi-fi e com bateria para não cair na hora H.",
   "Peça para os convidados deixarem o palpite ANTES da chamada, para o momento ser só a revelação.",
   "Coloque a câmera na sua reação e na do parceiro(a) — é o que mais emociona quem assiste de longe.",
   "Grave a chamada para guardar de lembrança e mostrar ao bebê quando crescer.",
   "Depois de revelar, mostre o ranking de quem acertou para fechar com risada.",
 ],
 "faq":[
   ("Funciona para quem está em outra cidade ou país?","Perfeitamente. O palpite é feito pelo navegador, de qualquer lugar. Só precisa do link — sem instalar nada."),
 ],
},
{
 "slug":"brincadeiras-cha-revelacao","kw":"brincadeiras para chá revelação",
 "title":"Brincadeiras para Chá Revelação: as Mais Divertidas | Revelê",
 "h1":"Brincadeiras para chá revelação que animam a festa",
 "desc":"As melhores brincadeiras para chá revelação: bolão de palpites, caixa surpresa, quem conhece melhor os papais e mais. Monte o bolão online grátis.",
 "lead":"Um bom chá revelação não é só o momento de descobrir o sexo do bebê — são as brincadeiras que esquentam a festa até lá. Separamos as mais divertidas para fazer com os convidados, incluindo a queridinha que dá para organizar online: o bolão de palpites menino ou menina.",
 "why":"As brincadeiras deixam todo mundo envolvido e transformam a espera pela revelação em pura diversão. E a melhor parte: a principal delas, o bolão de palpites, você monta em minutos e roda pelo celular, com placar ao vivo e ranking de quem acertou no final.",
 "guide":[
   "Misture uma brincadeira online (o bolão) com uma ou duas presenciais para agradar todo mundo.",
   "Deixe prêmios simbólicos para quem acertar o sexo, o nome ou a data — aumenta a graça.",
   "Combine as brincadeiras com o tema da decoração (azul x rosa) para ficar tudo conectado.",
 ],
 "list_title":"Brincadeiras para animar o chá revelação",
 "list_intro":"Da mais fácil de organizar à mais elaborada:",
 "list_items":[
   "Bolão de palpites: cada convidado aposta menino ou menina (e nome, data e peso). Online, com placar ao vivo.",
   "Time azul x time rosa: divida a festa em dois times, com adereços, e veja quem torce por quê.",
   "Quem conhece melhor os papais: quiz com perguntas sobre o casal; quem acerta mais leva um mimo.",
   "Caixa surpresa: uma caixa grande solta balões azuis ou rosas quando aberta na revelação.",
   "Palpite pela barriga: convidados escrevem o palpite num mural e justificam pelo \"formato da barriga\".",
   "Bolo da revelação: o recheio colorido conta o segredo na hora de cortar.",
 ],
 "faq":[
   ("Qual brincadeira é a mais fácil de organizar?","O bolão de palpites online — você cria em 2 minutos, manda o link e todo mundo participa pelo celular, sem material nenhum."),
 ],
},
{
 "slug":"palpite-menino-ou-menina","kw":"palpite menino ou menina",
 "title":"Palpite Menino ou Menina: Monte o Bolão do Bebê | Revelê",
 "h1":"Palpite menino ou menina: faça o bolão do bebê",
 "desc":"Quer saber quem acerta se vem menino ou menina? Monte um bolão de palpites online grátis, colete os palpites da família e revele com animação e ranking.",
 "lead":"\"Vai ser menino ou menina?\" é a pergunta que ninguém cansa de fazer na gravidez. Em vez de cada um dar seu palpite solto, junte todo mundo num bolão: cada pessoa registra a aposta, o placar mostra a maioria e, na revelação, aparece quem acertou. É a brincadeira mais gostosa da espera pelo bebê.",
 "why":"Transformar os palpites num bolão organizado deixa a torcida divertida e cria expectativa até a revelação. E de quebra vira uma lembrança: dá para reler depois quem apostou em quê e rir de quem errou feio (ou acertou na mosca).",
 "guide":[
   "Abra o bolão assim que descobrir (ou decidir descobrir) o sexo — quanto antes, mais palpites.",
   "Incentive os palpiteiros a justificar: enjoo, formato da barriga, desejo por doce ou salgado.",
   "Só revele o resultado verdadeiro no dia combinado, para manter o suspense.",
 ],
 "list_title":"Crenças populares que todo mundo usa para palpitar",
 "list_intro":"Sem base científica, mas rendem ótimos palpites (e discussões):",
 "list_items":[
   "Barriga pontuda e para a frente: dizem que é menino; arredondada e espalhada, menina.",
   "Muito enjoo no começo da gravidez: a lenda associa a menina.",
   "Desejo por doces: seria menina; por salgados e azedos, menino.",
   "Batimentos acima de 140: crença de que é menina; abaixo, menino.",
   "Pele e cabelo mais oleosos na gestação: o palpite popular é menino.",
 ],
 "faq":[
   ("Dá para palpitar também o nome e a data?","Dá. Além de menino ou menina, cada convidado pode arriscar o nome do bebê, a data provável do nascimento e o peso — e tudo entra no ranking de quem acertou."),
 ],
},
{
 "slug":"como-fazer-cha-revelacao","kw":"como fazer chá revelação",
 "title":"Como Fazer um Chá Revelação: Passo a Passo Simples | Revelê",
 "h1":"Como fazer um chá revelação: o passo a passo",
 "desc":"Aprenda como fazer um chá revelação do zero: como descobrir o sexo em segredo, montar o bolão de palpites, decorar e organizar o momento da revelação. Guia grátis.",
 "lead":"Vai organizar o chá revelação e não sabe por onde começar? O segredo é simples: descobrir o sexo do bebê sem estragar a surpresa, envolver os convidados com um bolão de palpites e preparar um momento marcante para revelar o resultado. Veja o passo a passo.",
 "why":"Um chá revelação bem organizado não precisa ser caro nem complicado — precisa de um bom momento de revelação e de gente participando. Por isso o bolão de palpites é tão importante: ele engaja os convidados desde antes da festa e faz a revelação valer ainda mais.",
 "guide":[
   "Descubra o sexo em segredo: peça ao médico para anotar num envelope, ou veja o resultado do exame e guarde só para você.",
   "Monte o bolão online e mande o link para a família palpitar nos dias antes da festa.",
   "Escolha COMO revelar (bolo, balões, tinta, fumaça) e deixe esse momento para o fim.",
 ],
 "list_title":"Passo a passo do chá revelação",
 "list_intro":"Do planejamento à revelação:",
 "list_items":[
   "1. Defina a data e a lista de convidados (presenciais e online).",
   "2. Descubra o sexo do bebê e guarde em segredo (envelope lacrado ou só você sabe).",
   "3. Crie o bolão de palpites e compartilhe o link com todo mundo.",
   "4. Prepare a decoração no clima azul x rosa e o item da revelação (bolo, caixa, balão).",
   "5. No grande momento, mostre o placar dos palpites e revele o resultado.",
   "6. Feche com o ranking de quem acertou — e muita foto.",
 ],
 "faq":[
   ("Preciso saber o sexo antes da festa?","Sim, alguém precisa saber para preparar a revelação — normalmente os pais ou um padrinho de confiança. No app, o organizador guarda o resultado em segredo e só ele revela na hora."),
 ],
},
{
 "slug":"cha-revelacao-simples","kw":"chá revelação simples em casa",
 "title":"Chá Revelação Simples e Barato para Fazer em Casa | Revelê",
 "h1":"Chá revelação simples e barato para fazer em casa",
 "desc":"Ideias de chá revelação simples e barato para fazer em casa: decoração fácil, revelação econômica e o bolão de palpites online grátis. Sem gastar muito.",
 "lead":"Chá revelação não precisa de salão nem de festa cara para emocionar. Dá para fazer em casa, com a família mais próxima, gastando pouco — e ainda assim criar um momento inesquecível. A chave é caprichar no que importa: a revelação e a participação de todo mundo no bolão.",
 "why":"Uma festa simples em casa tem uma vantagem: o foco fica no que emociona, não na produção. Com um bolão de palpites gratuito e uma revelação caseira bem pensada, você entrega a mesma emoção de uma festa grande gastando uma fração do valor.",
 "guide":[
   "Faça em casa, com a família próxima — menos convidados, mais aconchego e menos custo.",
   "Use o bolão online (grátis) no lugar de cartelas impressas e urnas.",
   "Capriche na revelação barata: balão preto com confete colorido dentro resolve lindamente.",
 ],
 "list_title":"Ideias baratas de chá revelação em casa",
 "list_intro":"Emoção sem pesar no bolso:",
 "list_items":[
   "Balão preto gigante furado com confete azul ou rosa dentro — barato e fotogênico.",
   "Bolo simples com recheio colorido: só quem fez sabe a cor até cortar.",
   "Spray/tinta colorida (guache) numa tela ou camiseta branca dos pais.",
   "Caixa de papelão decorada soltando balões de gás na abertura.",
   "Decoração azul x rosa com bexigas e papel crepom — o básico bem feito.",
   "Bolão de palpites online no lugar de material impresso: zero custo.",
 ],
 "faq":[
   ("Dá para fazer só com a família e ainda usar o bolão?","Claro. Mesmo com poucas pessoas, o bolão deixa a revelação mais divertida — e quem não pôde ir palpita à distância pelo link."),
 ],
},
{
 "slug":"frases-para-cha-revelacao","kw":"frases para chá revelação",
 "title":"Frases para Chá Revelação: Mensagens para o Bebê e os Papais | Revelê",
 "h1":"Frases para chá revelação: mensagens que emocionam",
 "desc":"As melhores frases para chá revelação: mensagens de carinho para o bebê e os papais, legendas para foto e frases de convite. Copie e use. Monte o bolão grátis.",
 "lead":"Seja para escrever no convite, na decoração, na legenda da foto ou no palpite do bolão, uma boa frase deixa o chá revelação ainda mais especial. Reunimos mensagens de carinho para o bebê e para os papais que você pode copiar e usar à vontade.",
 "why":"As palavras certas eternizam o momento. Uma frase bonita no convite dá o tom da festa; uma mensagem carinhosa no bolão vira lembrança para os pais relerem. Use as ideias abaixo como inspiração — e deixe a sua no bolão do bebê.",
 "guide":[
   "Use uma frase curta e marcante no convite e na arte do tema azul x rosa.",
   "Peça que os convidados deixem uma mensagem junto do palpite no bolão — vira recordação.",
   "Guarde as frases favoritas: depois da revelação elas ficam de lembrança na página do bolão.",
 ],
 "list_title":"Frases e mensagens para o chá revelação",
 "list_intro":"Para convite, decoração, legenda ou para deixar no bolão:",
 "list_items":[
   "Azul ou rosa, o importante é que você já é o nosso maior amor. 💙💗",
   "Menino ou menina? Uma coisa é certa: já é muito esperado(a)!",
   "Contando os dias para saber se é ele ou ela — e para te abraçar.",
   "Que venha com saúde; o resto a gente descobre hoje!",
   "O maior mistério (e a maior alegria) da família está prestes a ser revelado.",
   "Palpite ou não, todo mundo aqui já ama esse bebê.",
   "Hoje a gente descobre a cor, mas o amor já tem tamanho gigante.",
 ],
 "faq":[
   ("Posso usar essas frases no convite?","Pode, à vontade. São livres para usar no convite, na decoração, na legenda das fotos ou como mensagem no bolão do bebê."),
 ],
},
{
 "slug":"ideias-cha-revelacao","kw":"ideias de chá revelação",
 "title":"Ideias de Chá Revelação: Temas, Decoração e Revelação | Revelê",
 "h1":"Ideias de chá revelação: temas e formas de revelar",
 "desc":"Ideias de chá revelação: temas criativos, decoração azul x rosa e formas marcantes de revelar o sexo do bebê. Inspire-se e monte o bolão de palpites grátis.",
 "lead":"Quer fugir do óbvio no chá revelação? Do tema da decoração à forma de revelar o sexo do bebê, tem muita ideia criativa para deixar a festa com a sua cara. Separamos inspirações — e o jeito mais fácil de envolver os convidados: o bolão de palpites.",
 "why":"Uma ideia boa é a que combina com o casal e cria um momento memorável. Não precisa ser cara: precisa ter significado e participação. Escolha um tema, uma forma de revelar que emocione, e deixe o bolão cuidar da diversão coletiva.",
 "guide":[
   "Escolha um tema que tenha a ver com o casal (futebol, viagem, cinema) e leve para a decoração.",
   "Aposte numa forma de revelar visual e fotogênica — pensa na foto e no vídeo que vão rodar.",
   "Use o bolão para engajar os convidados antes, durante e depois (com o ranking).",
 ],
 "list_title":"Ideias de temas e formas de revelar",
 "list_intro":"Para inspirar a sua festa:",
 "list_items":[
   "Temas: \"príncipe ou princesa\", \"futebol azul x rosa\", \"astronauta\", \"safári\", \"ele ou ela\".",
   "Bolo com recheio colorido: o clássico que nunca falha.",
   "Balões de gás dentro de uma caixa surpresa gigante.",
   "Pó colorido (tipo Holi) num estouro para a foto perfeita.",
   "Fumaça colorida ao ar livre (com segurança) para vídeo dramático.",
   "Quadro/tela pintada pelos pais na hora, revelando a cor.",
   "Bolão de palpites online: a diversão coletiva que acompanha qualquer tema.",
 ],
 "faq":[
   ("Como envolver os convidados além da decoração?","Com o bolão de palpites: cada um aposta menino ou menina, nome e data. Isso cria expectativa desde antes da festa e rende o ranking de quem acertou no final."),
 ],
},
]

CSS = """
:root{--bg:#f4f2fb;--bg2:#e9ecfb;--ink:#332f47;--muted:#807a99;--menino:#6f9de3;--menina:#e37fa6;--accent:#7c6fe3;--accent2:#e37fa6;--card:#fff;--line:#e4e0f5;--shadow:0 10px 30px rgba(90,72,150,.12)}
*{box-sizing:border-box}html,body{margin:0}
body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:radial-gradient(1200px 600px at 80% -10%,var(--bg2),transparent),var(--bg);min-height:100vh;-webkit-font-smoothing:antialiased;line-height:1.6}
h1,h2,h3{font-family:'Fraunces',Georgia,serif;font-weight:600;line-height:1.15}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:860px;margin:0 auto;padding:0 20px}
nav{display:flex;align-items:center;justify-content:space-between;padding:20px 0}
.brand{display:flex;align-items:center;gap:10px;font-family:'Fraunces';font-weight:700;font-size:22px;color:var(--ink)}
.logo{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:grid;place-items:center;color:#fff;font-size:18px}
.btn{display:inline-block;border:none;border-radius:999px;padding:14px 24px;font-weight:600;font-size:16px;cursor:pointer;font-family:inherit;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;box-shadow:0 8px 20px rgba(124,111,227,.35)}
.btn:hover{text-decoration:none;box-shadow:0 12px 26px rgba(124,111,227,.45)}
.hero{text-align:center;padding:26px 0 8px}
.hero h1{font-size:clamp(30px,5vw,46px);margin:0 0 16px}
.lead{font-size:18px;color:var(--muted);max-width:660px;margin:0 auto 22px}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow);padding:26px;margin:22px 0}
h2{font-size:26px;margin:34px 0 12px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:14px 0}
.step{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:var(--shadow)}
.step .n{width:30px;height:30px;border-radius:9px;background:var(--bg2);display:grid;place-items:center;font-weight:700;margin-bottom:8px;font-family:'Fraunces'}
.step h3{margin:0 0 6px;font-size:17px}.step p{margin:0;color:var(--muted);font-size:14px}
ul.items{list-style:none;padding:0;margin:0;display:grid;gap:10px}
ul.items li{background:#fffdfb;border:1px solid var(--line);border-left:4px solid var(--accent2);border-radius:10px;padding:12px 14px;font-size:15.5px}
.faq dt{font-weight:600;margin-top:16px}.faq dd{margin:6px 0 0;color:var(--muted)}
.related{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.related a{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:8px 15px;font-size:14px;box-shadow:var(--shadow);color:var(--ink)}
.related a:hover{text-decoration:none;border-color:var(--accent)}
.center{text-align:center}
footer{text-align:center;color:var(--muted);font-size:13px;padding:34px 0 44px}
@media(max-width:720px){.steps{grid-template-columns:1fr}}
"""

HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{canon}"/>
<meta property="og:type" content="website"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{canon}"/>
<meta property="og:site_name" content="Revelê"/>
<meta property="og:image" content="https://giogas-pm.github.io/revele/og.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="robots" content="index,follow"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>{css}</style>
{jsonld}
</head>
<body>
<div class="wrap">
<nav><a class="brand" href="/revele/"><span class="logo">👶</span> Revelê</a><a class="btn" style="padding:10px 18px;font-size:14px" href="{cta}">Criar bolão grátis</a></nav>
"""

FOOT = """<footer>Revelê — bolão de chá revelação online e gratuito · <a href="/revele/">criar meu bolão grátis</a></footer>
</div>
<script>
(function(){try{
  var q=new URLSearchParams(location.search), src=q.get('src')||'seo';
  document.querySelectorAll('a[href*="/revele/?"]').forEach(function(a){
    try{var u=new URL(a.getAttribute('href'), location.origin); u.searchParams.set('src',src); a.setAttribute('href', u.pathname+u.search);}catch(e){}
  });
  var SB="https://diemqzngskmcuytkzjhr.supabase.co";
  var K="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRpZW1xem5nc2ttY3V5dGt6amhyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI4NDM0MDEsImV4cCI6MjA5ODQxOTQwMX0.w5-w8bU6qFQqIFBDOiNsUvOWbXqeOZSH6tveyLdADx0";
  fetch(SB+"/rest/v1/revele_eventos",{method:"POST",headers:{apikey:K,Authorization:"Bearer "+K,"Content-Type":"application/json"},body:JSON.stringify({evento:"seo_land",slug:location.pathname,meta:{src:src}})}).catch(function(){});
}catch(e){}})();
</script>
</body>
</html>"""

def _script(obj): return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False)+'</script>'

def jsonld_page(faqs, canon, name):
    faq={"@context":"https://schema.org","@type":"FAQPage",
         "mainEntity":[{"@type":"Question","name":q,
             "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    howto={"@context":"https://schema.org","@type":"HowTo",
        "name":"Como fazer um bolão de chá revelação online",
        "step":[
          {"@type":"HowToStep","position":1,"name":"Crie o bolão","text":"Diga de quem é o bebê. Leva menos de 2 minutos e é grátis."},
          {"@type":"HowToStep","position":2,"name":"Mande o link","text":"Cada convidado abre no navegador e palpita menino ou menina, nome, data e peso — sem cadastro."},
          {"@type":"HowToStep","position":3,"name":"Revele na festa","text":"Anime o resultado em tela cheia e mostre o ranking de quem acertou."},
        ]}
    crumb={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Revelê","item":BASE+"/"},
        {"@type":"ListItem","position":2,"name":"Chá revelação","item":BASE+"/cha-revelacao/"},
        {"@type":"ListItem","position":3,"name":name,"item":canon},
    ]}
    return "\n".join(_script(o) for o in (howto,faq,crumb))

def steps_html():
    return ('<div class="steps">'
      '<div class="step"><div class="n">1</div><h3>Crie o bolão</h3><p>Diga de quem é o bebê. Leva menos de 2 minutos e é grátis.</p></div>'
      '<div class="step"><div class="n">2</div><h3>Mande o link</h3><p>Cada convidado palpita menino ou menina, nome, data e peso — sem cadastro.</p></div>'
      '<div class="step"><div class="n">3</div><h3>Revele na festa</h3><p>Anime o resultado em tela cheia e veja quem acertou.</p></div>'
      '</div>')

def related_html(cur_slug):
    links=[]
    for p in PAGES:
        if p["slug"]==cur_slug: continue
        links.append('<a href="/revele/cha-revelacao/%s/">%s</a>'%(p["slug"], e(p["kw"].capitalize())))
    return '<div class="related">'+''.join(links)+'</div>'

def build_page(p):
    canon = "%s/cha-revelacao/%s/"%(BASE,p["slug"])
    cta = cta_href()
    faqs = p["faq"] + FAQ_COMUM
    jsonld = jsonld_page(faqs, canon, p["h1"])
    head = HEAD.format(title=e(p["title"]),desc=e(p["desc"]),canon=canon,css=CSS,jsonld=jsonld,cta=e(cta))
    out=[head]
    out.append('<section class="hero"><h1>%s</h1><p class="lead">%s</p><a class="btn" href="%s">Criar bolão de chá revelação grátis</a></section>'
               %(e(p["h1"]),e(p["lead"]),e(cta)))
    out.append('<h2>Como funciona o bolão</h2>'+steps_html())
    out.append('<div class="card"><h2 style="margin-top:0">Por que vale a pena</h2><p>%s</p></div>'%e(p["why"]))
    if p.get("guide"):
        out.append('<h2>Dicas para organizar</h2>')
        out.append('<ul class="items">'+''.join('<li>%s</li>'%e(g) for g in p["guide"])+'</ul>')
    out.append('<h2>%s</h2>'%e(p["list_title"]))
    if p.get("list_intro"):
        out.append('<p style="color:var(--muted)">%s</p>'%e(p["list_intro"]))
    out.append('<ul class="items">'+''.join('<li>%s</li>'%e(x) for x in p["list_items"])+'</ul>')
    out.append('<h2>Perguntas frequentes</h2><dl class="faq">'+''.join('<dt>%s</dt><dd>%s</dd>'%(e(q),e(a)) for q,a in faqs)+'</dl>')
    out.append('<div class="card center"><h2 style="margin-top:0">Pronto para começar?</h2><p style="color:var(--muted)">Crie seu bolão de chá revelação agora. Grátis para coletar os palpites — você só paga se quiser a revelação animada completa.</p><a class="btn" href="%s">Criar meu bolão grátis 👶</a></div>'%e(cta))
    out.append('<h2>Veja também</h2>'+related_html(p["slug"]))
    out.append(FOOT)
    return "\n".join(out)

def build_hub():
    canon = "%s/cha-revelacao/"%BASE
    cta = cta_href()
    title="Chá Revelação Online: Bolão de Palpites Grátis (Menino ou Menina) | Revelê"
    desc="Tudo para o seu chá revelação: bolão de palpites online grátis, brincadeiras, ideias, frases e passo a passo. Crie o bolão e revele com animação."
    web={"@context":"https://schema.org","@type":"WebPage","name":title,"url":canon}
    jsonld=_script(web)
    head = HEAD.format(title=e(title),desc=e(desc),canon=canon,css=CSS,jsonld=jsonld,cta=e(cta))
    out=[head]
    out.append('<section class="hero"><h1>Chá revelação: bolão de palpites online e grátis</h1><p class="lead">Junte os palpites de menino ou menina de todo mundo num só lugar, revele com uma animação e mostre quem acertou. Aqui você também encontra ideias, brincadeiras e frases para a festa.</p><a class="btn" href="%s">Criar meu bolão grátis</a></section>'%e(cta))
    out.append('<h2>Como funciona</h2>'+steps_html())
    out.append('<h2>Guias e ideias para o seu chá revelação</h2><div class="related">')
    for p in PAGES:
        out.append('<a href="/revele/cha-revelacao/%s/">%s</a>'%(p["slug"],e(p["kw"].capitalize())))
    out.append('</div>')
    out.append('<div class="card"><h2 style="margin-top:0">O que é o Revelê</h2><p>O Revelê é uma ferramenta gratuita para criar um <strong>bolão de chá revelação online</strong>: os convidados palpitam menino ou menina (e o nome, a data e o peso do bebê) a partir de um único link, o placar se atualiza sozinho e, no grande dia, você revela o resultado com uma animação em tela cheia e o ranking de quem acertou. Criar e coletar palpites é grátis; você só paga uma vez, se quiser, para desbloquear a revelação completa sem marca d\'água.</p></div>')
    out.append(FOOT)
    return "\n".join(out)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w",encoding="utf-8",newline="\n") as f:
        f.write(content)
    print("escrito:", path, "(%d bytes, ~%d palavras)"%(len(content.encode('utf-8')), len(content.split())))

# hub
write(os.path.join(OUT_DIR,"index.html"), build_hub())
# paginas
for p in PAGES:
    write(os.path.join(OUT_DIR,p["slug"],"index.html"), build_page(p))

# sitemap (inclui a home do app tambem)
urls=[BASE+"/", BASE+"/cha-revelacao/"] + [BASE+"/cha-revelacao/%s/"%p["slug"] for p in PAGES]
sm=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    pr = "1.0" if u==BASE+"/" else ("0.9" if u.endswith("cha-revelacao/") else "0.8")
    sm.append("  <url><loc>%s</loc><changefreq>weekly</changefreq><priority>%s</priority></url>"%(u,pr))
sm.append("</urlset>")
write(os.path.join(REPO,"sitemap.xml"), "\n".join(sm))

# robots
robots="User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n"%BASE
write(os.path.join(REPO,"robots.txt"), robots)

print("\nTOTAL:", 1+len(PAGES), "paginas de conteudo + sitemap + robots")

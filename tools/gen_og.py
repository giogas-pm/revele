# -*- coding: utf-8 -*-
"""Gera o OG-image (card de compartilhamento) do Revele. 1200x630 -> apps/revele/og.png"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
MENINO=(111,157,227); MENINA=(227,127,166); ACCENT=(124,111,227)
INK=(51,47,71); WHITE=(255,255,255)

def font(paths, size):
    for p in paths:
        try: return ImageFont.truetype(p, size)
        except Exception: pass
    return ImageFont.load_default()

SERIF_B = ["C:/Windows/Fonts/georgiab.ttf","C:/Windows/Fonts/timesbd.ttf"]
SANS    = ["C:/Windows/Fonts/segoeui.ttf","C:/Windows/Fonts/arial.ttf"]
SANS_B  = ["C:/Windows/Fonts/segoeuib.ttf","C:/Windows/Fonts/arialbd.ttf"]
EMOJI   = ["C:/Windows/Fonts/seguiemj.ttf"]

# fundo: gradiente diagonal azul-menino -> roxo -> rosa-menina
base = Image.new("RGB",(W,H),ACCENT)
top = Image.new("RGB",(W,H))
for y in range(H):
    t=y/H
    r=int(MENINO[0]*(1-t)+MENINA[0]*t)
    g=int(MENINO[1]*(1-t)+MENINA[1]*t)
    b=int(MENINO[2]*(1-t)+MENINA[2]*t)
    for line in (top,):
        pass
    ImageDraw.Draw(top).line([(0,y),(W,y)],fill=(r,g,b))
# mistura horizontal leve pra dar profundidade
base = Image.blend(base, top, 0.9)
d = ImageDraw.Draw(base)

# cartao branco central
pad=64
card=[pad,pad,W-pad,H-pad]
d.rounded_rectangle(card, radius=40, fill=WHITE)

cx = W//2
# marca
brand_f=font(SANS_B,40); logo_f=font(EMOJI,52)
try:
    d.text((cx-150, 110), "👶", font=logo_f, embedded_color=True)
    d.text((cx-88, 120), "Revelê", font=brand_f, fill=ACCENT)
except Exception:
    d.text((cx-70, 120), "Revelê", font=brand_f, fill=ACCENT)

# titulo
tit_f=font(SERIF_B,92)
def center(txt,f,y,fill):
    w=d.textlength(txt,font=f); d.text((cx-w/2,y),txt,font=f,fill=fill)
center("Menino ou menina?", tit_f, 210, INK)

# subtitulo
sub_f=font(SANS,40)
center("Faça o bolão do chá revelação online", sub_f, 330, (128,122,153))

# pilulas azul/rosa
pill_f=font(SANS_B,34)
def pill(txt,x,color):
    tw=d.textlength(txt,font=pill_f); w=tw+56; h=64; y=410
    d.rounded_rectangle([x,y,x+w,y+h], radius=32, fill=color)
    d.text((x+28,y+13),txt,font=pill_f,fill=WHITE)
    return w
gap=24
w1=d.textlength("💙 Menino",font=pill_f)+56
w2=d.textlength("Menina 💗",font=pill_f)+56
startx=cx-(w1+gap+w2)/2
# sem emoji nas pilulas (fonte padrao nao renderiza colorido aqui) -> texto limpo
def pill2(txt,x,color):
    tw=d.textlength(txt,font=pill_f); w=tw+56; h=64; y=412
    d.rounded_rectangle([x,y,x+w,y+h], radius=32, fill=color)
    d.text((x+28,y+13),txt,font=pill_f,fill=WHITE); return w
w1=d.textlength("Menino",font=pill_f)+56
w2=d.textlength("Menina",font=pill_f)+56
startx=cx-(w1+gap+w2)/2
pill2("Menino",int(startx),MENINO)
pill2("Menina",int(startx+w1+gap),MENINA)

# rodape
foot_f=font(SANS,30)
center("grátis • palpite de nome e data • revelação animada", foot_f, 512, (150,145,170))

out=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"og.png")
base.save(out,"PNG")
print("escrito:",out, os.path.getsize(out),"bytes",base.size)

import re
import os

filepath = r'c:\Users\nicoa\OneDrive\Documentos\9 - Nico Labs\JPS Training\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1: Replace all section padding. 
html = html.replace('py-section-gap', 'py-[120px]')
html = html.replace('mb-16', 'mb-24')

def style_title(title_text):
    return f'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 flex items-center justify-center w-full"><div class="border-l-8 border-[#FF8A00] pl-6 py-2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent">{title_text}</div></h2>'

# Modalities: ENTRENAMIENTO
html = re.sub(r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center">ENTRENAMIENTO</h2>', style_title('ENTRENAMIENTO'), html)

# Staff: NUESTRO STAFF DE ÉLITE
html = re.sub(r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4">\s*NUESTRO\s*<span class="text-gradient">STAFF DE ÉLITE</span></h2>', style_title('NUESTRO STAFF DE ÉLITE'), html)

# Planes: ELIGE TU PODER
html = re.sub(r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center mt-20">ELIGE TU PODER</h2>', style_title('ELIGE TU PODER'), html)

# Horarios: HORARIOS DE ENTRENAMIENTO
html = re.sub(r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center w-full">HORARIOS DE ENTRENAMIENTO</h2>', style_title('HORARIOS DE ENTRENAMIENTO'), html)

# Remove Elena Rojas completely
idx = html.find('Elena Rojas')
if idx != -1:
    start = html.rfind('<div class="group relative rounded-2xl overflow-hidden bg-surface-elevated', 0, idx)
    if start != -1:
        end1 = html.find('<div class="relative rounded-2xl overflow-hidden bg-gradient-to-br', start)
        if end1 != -1:
            end2 = html.find('</section>', end1)
            html = html[:start] + '\n\n' + html[end2:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

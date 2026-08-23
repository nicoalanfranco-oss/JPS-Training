import re
import os

filepath = r'c:\Users\nicoa\OneDrive\Documentos\9 - Nico Labs\JPS Training\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'(<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 flex items-center justify-center w-full"><div class="border-l-8 border-\[#FF8A00\] pl-6 py-2 bg-gradient-to-r from-\[#FF8A00\] to-\[#E01E5A\] bg-clip-text text-transparent">ELIGE TU PODER</div></h2>\s*<p[^>]*>.*?</p>)\s*<div class="grid grid-cols-1 md:grid-cols-3 gap-8">'
match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
if match:
    new_grid = match.group(1) + '\n<div id="precios-dynamic-container" class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">\n</div><!-- '
    html = html.replace(match.group(0), new_grid)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Replaced planes section')
else:
    print('Failed to match planes section')

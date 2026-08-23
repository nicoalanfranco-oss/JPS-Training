import re
import os

filepath = r'c:\Users\nicoa\OneDrive\Documentos\9 - Nico Labs\JPS Training\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move Contact Section to bottom
contact_pattern = r'<!-- Contact Section -->.*?<section[^>]*>.*?</section>'
contact_match = re.search(contact_pattern, html, re.DOTALL)
if contact_match:
    contact_html = contact_match.group(0)
    # Add id='contacto' if missing
    if 'id="contacto"' not in contact_html:
        contact_html = contact_html.replace('<section', '<section id="contacto"', 1)
    
    # Remove from original location
    html = html.replace(contact_match.group(0), '')
    
    # Insert before <script src="script.js">
    html = html.replace('<script src="script.js"></script>', contact_html + '\n<script src="script.js"></script>')

# 2. ÚNETE AHORA button
html = html.replace('ÚNETE AHORA', 'ÚNETE AL EQUIPO')
html = re.sub(r'<button class="([^>]*?ÚNETE AL EQUIPO[^>]*?)</button>', r'<button onclick="document.getElementById(\'contacto\').scrollIntoView({behavior: \'smooth\'})" class="\1</button>', html, flags=re.DOTALL)

# 3. Staff Section changes
html = re.sub(r'NUESTRO <br/><span class="text-gradient">STAFF</span> DE.*?</p>', 
r'NUESTRO <span class="text-gradient">STAFF DE ÉLITE</span></h2>\n<p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto mt-4 text-center">Nuestros entrenadores son veteranos de la industria cuidadosamente seleccionados, dedicados a forjar el potencial en bruto en un rendimiento innegable. Sin excusas, solo resultados.</p>', html, flags=re.DOTALL|re.IGNORECASE)

# 4. Modalities section title (Assuming it is the first section header)
html = re.sub(r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center">.*?</h2>\s*<p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center">.*?</p>',
r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center">ENTRENAMIENTO</h2>\n<p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center">Elige tu camino. Entrenamiento de alta intensidad y precisión diseñado para superar tus límites y forjar un rendimiento de élite.</p>', html, count=1, flags=re.DOTALL)

# 5. Planes title and spacing
html = re.sub(r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center">\s*MEMBRESÍAS.*?</h2>\s*<p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center">.*?</p>',
r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center mt-20">ELIGE TU PODER</h2>\n<p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center mb-12">Selecciona el plan que se adapte a tu ambición. Sin compromisos, solo resultados.</p>', html, flags=re.DOTALL|re.IGNORECASE)

# Add carousel class to plan cards
html = html.replace('class="bg-surface-elevated rounded-2xl p-8 border border-white/5 flex flex-col h-full relative overflow-hidden group hover:border-primary/50 transition-colors duration-300"', 'class="bg-surface-elevated rounded-2xl p-8 border border-white/5 flex flex-col h-full relative overflow-hidden group hover:border-primary/50 transition-colors duration-300 plan-card"')

# 6. Horarios Section title
html = re.sub(r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4">.*?HORARIOS.*?</h2>\s*<p class="font-body-lg text-on-surface-variant max-w-2xl">.*?</p>',
r'<h2 class="font-display-xl text-headline-lg font-black tracking-tight mb-4 text-center w-full">HORARIOS DE ENTRENAMIENTO</h2>\n<p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center mb-12 w-full">Organiza tu semana y alcanza tu máximo potencial con nuestras clases diseñadas para el rendimiento élite.</p>', html, flags=re.DOTALL|re.IGNORECASE)

# 7. OPEN BOX text with red background
html = html.replace('OPEN BOX', '<span class="bg-red-600 text-white px-2 py-1 rounded font-bold">OPEN BOX</span>')

# Modify the table body to have an ID so we can inject rows
html = re.sub(r'<tbody class="divide-y divide-white/5">.*?</tbody>', '<tbody id="horarios-dynamic-container" class="divide-y divide-white/5"></tbody>', html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

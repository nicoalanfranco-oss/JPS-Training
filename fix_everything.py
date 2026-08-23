import re

filepath = r'c:\Users\nicoa\OneDrive\Documentos\9 - Nico Labs\JPS Training\index.html'

contact_section = """
<!-- Contact Section -->
<section id="contacto" class="w-full py-[120px] px-gutter bg-surface-container relative">
<div class="max-w-4xl mx-auto text-center flex flex-col gap-6">
<div class="flex items-center justify-center">
<h2 class="font-display-xl text-headline-lg font-black tracking-tight flex items-center justify-center">
<div class="border-l-8 border-[#FF8A00] pl-6 py-2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent uppercase">
Ponte en Contacto
</div>
</h2>
</div>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-xl mx-auto">
¿Listo para transformar tu vida? Déjanos tus datos y nos pondremos en contacto contigo a la brevedad.
</p>
<form class="mt-8 flex flex-col gap-6 text-left" onsubmit="event.preventDefault(); alert('¡Gracias por comunicarte! Te contactaremos a la brevedad.');">
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<div class="flex flex-col gap-2">
<label class="font-label-caps text-xs text-on-surface-variant">Nombre Completo</label>
<input type="text" required placeholder="Tu nombre" class="w-full bg-background border border-brushed-metal rounded-xl py-4 px-4 text-on-surface focus:border-electric-orange focus:outline-none"/>
</div>
<div class="flex flex-col gap-2">
<label class="font-label-caps text-xs text-on-surface-variant">Teléfono / WhatsApp</label>
<input type="tel" required placeholder="Tu número" class="w-full bg-background border border-brushed-metal rounded-xl py-4 px-4 text-on-surface focus:border-electric-orange focus:outline-none"/>
</div>
</div>
<div class="flex flex-col gap-2">
<label class="font-label-caps text-xs text-on-surface-variant">Mensaje o Consulta</label>
<textarea rows="4" placeholder="¿En qué podemos ayudarte?" class="w-full bg-background border border-brushed-metal rounded-xl py-4 px-4 text-on-surface focus:border-electric-orange focus:outline-none"></textarea>
</div>
<button type="submit" class="w-full py-4 rounded-xl font-label-caps font-bold text-white bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] hover:opacity-90 transition-opacity uppercase tracking-widest mt-4">
Enviar Mensaje
</button>
</form>
</div>
</section>
"""

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure Tailwind & symbols are imported, script tag is present
if '<script src="script.js"></script>' not in html:
    html = html.replace('</body>', '<script src="script.js"></script>\n</body>')

# 1. Update Hero ÚNETE AL EQUIPO button action
html = re.sub(
    r'<button([^>]*?)>\s*ÚNETE AL EQUIPO\s*<span([^>]*?)>arrow_forward</span>\s*</button>',
    r'<button onclick="document.getElementById(\'contacto\').scrollIntoView({behavior: \'smooth\'})" \1>\n ÚNETE AL EQUIPO\n <span\2>arrow_forward</span>\n</button>',
    html
)

# 2. Section 1 (Entrenamiento / Modalidades Title)
old_mod_title = r'<div class="mb-24 relative">\s*<div class="absolute -left-4 top-0 w-1 h-full bg-gradient-to-b from-electric-orange to-vibrant-pink"></div>\s*<p class="font-body-lg text-body-lg text-on-surface-variant mt-4 max-w-2xl">\s*Elige tu camino.*?</p>\s*</div>'
new_mod_title = """
<div class="mb-16 text-center flex flex-col items-center justify-center">
    <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black tracking-tight mb-4 flex items-center justify-center">
        <div class="border-l-8 border-[#FF8A00] pl-6 py-2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent uppercase">
            ENTRENAMIENTO
        </div>
    </h2>
    <p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center">
        Elige tu camino. Entrenamiento de alta intensidad y precisión diseñado para superar tus límites y forjar un rendimiento de élite.
    </p>
</div>
"""
html = re.sub(old_mod_title, new_mod_title, html, flags=re.DOTALL)

# 3. Staff Header Title & Cleanup
old_staff_header = r'<section class="mb-24 relative">\s*<div class="absolute inset-0 -z-10 bg-\[radial-gradient\(ellipse_at_top_right,_var\(--tw-gradient-stops\)\)\] from-primary/10 via-background to-background opacity-50 blur-3xl"></div>\s*<h1 class="font-display-xl text-display-xl text-transparent bg-clip-text bg-gradient-to-r from-white to-steel-silver mb-4 uppercase tracking-tighter">\s*NUESTRO <span class="text-gradient">STAFF DE ÉLITE</span></h2>\s*<p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto mt-4 text-center">.*?</p>\s*</section>'
new_staff_header = """
<section class="py-[60px] relative">
<div class="mb-16 text-center flex flex-col items-center justify-center">
    <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black tracking-tight mb-4 flex items-center justify-center">
        <div class="border-l-8 border-[#FF8A00] pl-6 py-2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent uppercase">
            NUESTRO STAFF DE ÉLITE
        </div>
    </h2>
    <p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center">
        Nuestros entrenadores son veteranos de la industria cuidadosamente seleccionados, dedicados a forjar el potencial en bruto en un rendimiento innegable. Sin excusas, solo resultados.
    </p>
</div>
</section>
"""
html = re.sub(old_staff_header, new_staff_header, html, flags=re.DOTALL)

# Remove Elena Rojas card (Standard Coach 1) and Join the Team callout
html = re.sub(r'<!-- Standard Coach 1 \(Spans 4 cols on desktop\) -->.*?<!-- Standard Coach 2', '<!-- Standard Coach 2', html, flags=re.DOTALL)
html = re.sub(r'<!-- Join the Team Callout \(Spans 4 cols on desktop\) -->.*?</section>', '</section>', html, flags=re.DOTALL)

# Adjust Staff grid cols to 12 with 3 equal coaches (Juan Pablo, Santiago, Noelia)
html = html.replace('md:col-span-8 group relative rounded-lg', 'md:col-span-4 group relative rounded-lg id="card-juanpablo"')
html = html.replace('md:col-span-4 group relative rounded-lg', 'md:col-span-4 group relative rounded-lg id="card-santiago"', 1)
# Add id to Noelia
html = re.sub(r'(Standard Coach 3.*?<div class="md:col-span-4 group relative rounded-lg)', r'\1 id="card-noelia"', html, flags=re.DOTALL)

# 4. Pricing / Elige Tu Poder Section Title
old_pricing_header = r'<header class="text-center mb-24 relative">\s*<h1 class="font-display-xl text-headline-lg-mobile md:text-display-xl text-on-surface mb-4 uppercase">\s*ELIGE TU <span class="bg-gradient-to-r from-electric-orange to-vibrant-pink bg-clip-text text-transparent">PODER</span>\s*</h1>\s*<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto">\s*Selecciona el plan.*?\s*</p>\s*</header>'
new_pricing_header = """
<div class="mt-28 mb-16 text-center flex flex-col items-center justify-center">
    <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black tracking-tight mb-4 flex items-center justify-center">
        <div class="border-l-8 border-[#FF8A00] pl-6 py-2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent uppercase">
            ELIGE TU PODER
        </div>
    </h2>
    <p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center">
        Selecciona el plan que se adapte a tu ambición. Sin compromisos, solo resultados.
    </p>
</div>
"""
html = re.sub(old_pricing_header, new_pricing_header, html, flags=re.DOTALL)

# Add plan-card class to pricing articles
html = html.replace('<article class="bg-surface-elevated', '<article class="plan-card bg-surface-elevated')

# 5. Horarios Header & Table replacement
old_horarios_header = r'<header class="mb-24 text-center md:text-left relative">\s*<!-- Kinetic accent -->\s*<div class="absolute -left-4 top-0 w-1 h-full bg-gradient-to-b from-electric-orange to-vibrant-pink hidden md:block"></div>\s*<h1 class="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-lg md:text-headline-lg uppercase italic bg-gradient-to-r from-white to-on-surface-variant bg-clip-text text-transparent">\s*HORARIOS DE ENTRENAMIENTO\s*</h1>\s*<p class="font-body-lg text-body-lg text-on-surface-variant mt-4 max-w-2xl">\s*Organiza tu semana.*?\s*</p>\s*</header>'
new_horarios_header = """
<div class="mt-28 mb-12 text-center flex flex-col items-center justify-center">
    <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black tracking-tight mb-4 flex items-center justify-center">
        <div class="border-l-8 border-[#FF8A00] pl-6 py-2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent uppercase">
            HORARIOS DE ENTRENAMIENTO
        </div>
    </h2>
    <p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto text-center">
        Organiza tu semana y alcanza tu máximo potencial con nuestras clases diseñadas para el rendimiento élite.
    </p>
</div>
"""
html = re.sub(old_horarios_header, new_horarios_header, html, flags=re.DOTALL)

# Replace old schedule tabs and old static grid with badges + new dynamic table
old_schedule_block = r'<!-- Class Category Tabs -->.*?<!-- Open Box Banner -->'
new_schedule_block = """
<!-- Badges / Filters -->
<div class="flex flex-wrap items-center justify-center gap-3 mb-8 w-full" id="schedule-filters">
    <button data-filter="all" class="filter-btn active flex items-center gap-2 px-4 py-2 rounded-full border border-[#FF8A00] bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white text-sm font-bold transition-all duration-300">
        <span class="material-symbols-outlined text-[18px]">apps</span> TODOS
    </button>
    <button data-filter="Hybrid Training" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
        <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">bolt</span> HYBRID
    </button>
    <button data-filter="Functional Strength" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
        <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">fitness_center</span> FUNCTIONAL STRENGTH
    </button>
    <button data-filter="GAP" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
        <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">accessibility_new</span> GAP
    </button>
    <button data-filter="Pilates Funcional" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
        <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">self_improvement</span> PILATES FUNCIONAL
    </button>
    <button data-filter="+60" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
        <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">elderly</span> +60
    </button>
</div>

<!-- Dynamic Schedule Table -->
<div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/5 shadow-2xl mb-12">
    <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
            <thead>
                <tr class="border-b border-white/10 bg-surface">
                    <th class="p-4 text-sm font-bold text-on-surface-variant uppercase tracking-wider">Hora / Duración</th>
                    <th class="p-4 text-sm font-bold text-on-surface-variant uppercase tracking-wider">Actividad</th>
                    <th class="p-4 text-sm font-bold text-on-surface-variant uppercase tracking-wider hidden md:table-cell">Estado</th>
                    <th class="p-4 text-sm font-bold text-on-surface-variant uppercase tracking-wider text-right">Acción</th>
                </tr>
            </thead>
            <tbody id="horarios-dynamic-container" class="divide-y divide-white/5">
                <!-- Injected dynamically by script.js -->
            </tbody>
        </table>
    </div>
</div>

<!-- Open Box Banner -->
"""
html = re.sub(old_schedule_block, new_schedule_block, html, flags=re.DOTALL)

# Add Contact Section before </main>
if 'id="contacto"' not in html:
    html = html.replace('</main>', contact_section + '\n</main>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fix completed successfully!")

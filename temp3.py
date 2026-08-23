import re

filepath = r'c:\Users\nicoa\OneDrive\Documentos\9 - Nico Labs\JPS Training\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

badges_html = """
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
"""

# Insert before <div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/5">
html = html.replace('<div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/5">', badges_html + '\n<div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/5">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

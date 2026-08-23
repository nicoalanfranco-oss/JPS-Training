import re

with open('index_old.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add section-title-box style and 3D animations
style_to_add = """
        .section-title-box {
            position: relative;
            padding-left: 1.5rem;
            margin-bottom: 3rem;
            text-align: left;
        }
        .section-title-box::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            width: 6px;
            height: 100%;
            background: linear-gradient(180deg, #FF8A00 0%, #E01E5A 100%);
            border-radius: 4px;
        }
        @keyframes float3dLeft {
            0% { transform: translateY(0px) rotate(-10deg) scale(1); }
            50% { transform: translateY(-20px) rotate(-2deg) scale(1.08); }
            100% { transform: translateY(0px) rotate(-10deg) scale(1); }
        }
        @keyframes float3dRight {
            0% { transform: translateY(0px) rotate(10deg) scale(1); }
            50% { transform: translateY(-22px) rotate(2deg) scale(1.08); }
            100% { transform: translateY(0px) rotate(10deg) scale(1); }
        }
        .hero-3d-left {
            animation: float3dLeft 6s ease-in-out infinite;
        }
        .hero-3d-right {
            animation: float3dRight 7s ease-in-out infinite;
        }
"""
content = content.replace('</style>', style_to_add + '\n    </style>')

# 2. Hero updates (Circular logo and 3D assets)
hero_search = """<!-- Logo -->
<div class="w-48 h-48 md:w-64 md:h-64 rounded-full overflow-hidden shadow-[0_0_40px_rgba(255,138,0,0.2)] border-2 border-brushed-metal bg-surface-elevated flex items-center justify-center transform hover:scale-105 transition-transform duration-500 ease-out">"""
hero_replace = """<!-- 3D Floating Asset Left (Kettlebell) -->
<div class="hidden lg:block absolute left-12 top-1/2 -translate-y-1/2 z-20 hero-3d-left w-64 h-64 rounded-3xl overflow-hidden shadow-[0_10px_40px_rgba(224,30,90,0.3)] border border-white/10">
    <img src="hero_3d_kettlebell_1787491269421.jpg" alt="3D Kettlebell JPS" class="w-full h-full object-cover"/>
</div>

<!-- Logo -->
<div class="w-48 h-48 md:w-60 md:h-60 rounded-full overflow-hidden shadow-[0_0_50px_rgba(255,138,0,0.3)] border-4 border-[#FF8A00]/40 bg-surface-elevated flex items-center justify-center transform hover:scale-105 transition-transform duration-500">"""
content = content.replace(hero_search, hero_replace)

hero_cta_search = """</button>
</div>
<!-- Diagonal Accent Line -->"""
hero_cta_replace = """</button>
</div>
<!-- 3D Floating Asset Right (Dumbbell) -->
<div class="hidden lg:block absolute right-12 top-1/2 -translate-y-1/2 z-20 hero-3d-right w-64 h-64 rounded-3xl overflow-hidden shadow-[0_10px_40px_rgba(255,138,0,0.3)] border border-white/10">
    <img src="hero_3d_dumbbell_1787491246437.jpg" alt="3D Dumbbell JPS" class="w-full h-full object-cover"/>
</div>
<!-- Diagonal Accent Line -->"""
content = content.replace(hero_cta_search, hero_cta_replace)

# 3. Staff Title Format (NUESTRO STAFF DE ÉLITE)
staff_title_search = """<h1 class="font-display-xl text-display-xl text-transparent bg-clip-text bg-gradient-to-r from-white to-steel-silver mb-4 uppercase tracking-tighter">
                NUESTRO <span class="text-gradient">STAFF DE ├ëLITE</span></h2>"""
staff_title_replace = """<div class="section-title-box">
<h1 class="font-display-xl text-display-xl uppercase tracking-tighter mb-4">
                <span class="text-white">NUESTRO </span><span class="text-electric-orange">STAFF DE ÉLITE</span>
</h1>
</div>"""
content = content.replace(staff_title_search, staff_title_replace)
# Note: if there is another "STAFF DE ├ëLITE"
content = content.replace('STAFF DE ├ëLITE', 'STAFF DE ÉLITE')
content = content.replace('STAFF DE ÉLITE</h2>', 'STAFF DE ÉLITE</h1>') # fix any broken tag

# 4. Pricing Titles and layout
pricing_title_search = """<h1 class="font-display-xl text-headline-lg-mobile md:text-display-xl text-on-surface mb-4 uppercase">
                ELIGE TU <span class="bg-gradient-to-r from-electric-orange to-vibrant-pink bg-clip-text text-transparent">PODER</span>
</h1>"""
pricing_title_replace = """<div class="section-title-box">
<h1 class="font-display-xl text-headline-lg-mobile md:text-display-xl uppercase mb-4">
                <span class="text-white">ELIGE TU </span><span class="text-electric-orange">PODER</span>
</h1>
</div>"""
content = content.replace(pricing_title_search, pricing_title_replace)

# Setup pricing cards for JS manipulation
pricing_card_1 = """<article class="bg-surface-elevated border border-brushed-metal rounded-xl p-8 flex flex-col top-highlight relative">"""
pricing_card_1_rep = """<article class="plan-card bg-surface-elevated border border-white/10 rounded-xl p-8 flex flex-col top-highlight relative transition-all duration-500" data-plan-index="0">
<div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">
    EMPEZAR BÁSICO
</div>"""
content = content.replace(pricing_card_1, pricing_card_1_rep)

pricing_card_2 = """<article class="bg-surface-elevated rounded-xl p-8 flex flex-col relative top-highlight transform md:-translate-y-4 glow-effect z-10" style="background: linear-gradient(180deg, #1E1E1E 0%, #2A1510 100%);">"""
pricing_card_2_rep = """<article class="plan-card bg-surface-elevated border border-white/10 rounded-xl p-8 flex flex-col relative top-highlight transition-all duration-500 z-10" style="background: linear-gradient(180deg, #1E1E1E 0%, #2A1510 100%);" data-plan-index="1">
<div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">
    MÁS POPULAR
</div>"""
content = content.replace(pricing_card_2, pricing_card_2_rep)

pricing_card_3 = """<article class="bg-surface-elevated border border-brushed-metal rounded-xl p-8 flex flex-col top-highlight relative">"""
pricing_card_3_rep = """<article class="plan-card bg-surface-elevated border border-white/10 rounded-xl p-8 flex flex-col top-highlight relative transition-all duration-500" data-plan-index="2">
<div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">
    PREMIUM ELITE
</div>"""
# It might replace both 1 and 3 if they are identical, but we already replaced card 1 above. Let's make sure.
content = content.replace(pricing_card_3, pricing_card_3_rep)

# Convert all buttons inside pricing to have .plan-btn
content = content.replace('<button class="w-full py-3 border border-steel-silver text-on-surface font-label-caps text-label-caps uppercase rounded hover:bg-surface-bright transition-colors">', '<button class="plan-btn w-full py-4 border border-white/20 text-white font-bold text-xs uppercase tracking-widest rounded-xl transition-all duration-300">')
content = content.replace('<button class="w-full py-4 text-white font-label-caps text-label-caps uppercase rounded btn-gradient hover:glow-effect transition-all relative z-10">', '<button class="plan-btn w-full py-4 border border-white/20 text-white font-bold text-xs uppercase tracking-widest rounded-xl transition-all duration-300 relative z-10">')
content = content.replace('<button class="w-full py-3 border border-tertiary-fixed-dim text-tertiary-fixed-dim font-label-caps text-label-caps uppercase rounded hover:bg-tertiary-fixed-dim/10 transition-colors">', '<button class="plan-btn w-full py-4 border border-white/20 text-white font-bold text-xs uppercase tracking-widest rounded-xl transition-all duration-300">')

# Add class plan-title and plan-price to the right spans
content = content.replace('<h2 class="font-label-caps text-label-caps text-electric-orange mb-2 tracking-widest uppercase">', '<h2 class="plan-title font-label-caps text-label-caps text-electric-orange mb-2 tracking-widest uppercase">')
content = content.replace('<h2 class="font-label-caps text-label-caps text-steel-silver mb-2 tracking-widest uppercase">', '<h2 class="plan-title font-label-caps text-label-caps text-steel-silver mb-2 tracking-widest uppercase">')
content = content.replace('<h2 class="font-label-caps text-label-caps text-tertiary-fixed-dim mb-2 tracking-widest uppercase">', '<h2 class="plan-title font-label-caps text-label-caps text-tertiary-fixed-dim mb-2 tracking-widest uppercase">')

content = content.replace('<span class="font-stat-value text-stat-value text-on-surface">$1.650</span>', '<span class="plan-price font-stat-value text-stat-value text-on-surface">$1.650</span>')
content = content.replace('<span class="font-stat-value text-stat-value text-white text-[48px] font-black">$1.900</span>', '<span class="plan-price font-stat-value text-stat-value text-white text-[48px] font-black">$1.900</span>')
content = content.replace('<span class="font-stat-value text-stat-value text-on-surface">$2.100</span>', '<span class="plan-price font-stat-value text-stat-value text-on-surface">$2.100</span>')


# 5. Fix Schedule HTML
# Add container for JS rendering to replace the static table content
content = content.replace(
    """<!-- Schedule Grid / Bento Layout -->
<div class="overflow-x-auto">
<div class="min-w-[800px] w-full grid grid-cols-[auto_repeat(5,1fr)] gap-4 text-center pb-8">""",
    """<!-- Schedule Grid / Bento Layout -->
<div class="overflow-x-auto">
<div class="min-w-[800px] w-full grid grid-cols-[auto_repeat(5,1fr)] gap-4 text-center pb-8" id="horarios-grid-container">"""
)

# Wipe static table contents inside min-w-[800px]
static_table_pattern = re.compile(r'<!-- Header Row -->.*?</div>\s*</div>\s*<!-- Open Box Banner -->', re.DOTALL)
content = static_table_pattern.sub('</div>\n</div>\n<!-- Open Box Banner -->', content)

# 6. Add id="schedule-filters" to the buttons container and filter-btn classes
filter_search = """<div class="flex gap-4 mb-12 overflow-x-auto pb-4 hide-scrollbar">
<button class="px-6 py-3 rounded-full border border-slate-800 text-white font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light bg-gradient-to-r from-electric-orange to-vibrant-pink">"""
filter_replace = """<div class="flex gap-4 mb-12 overflow-x-auto pb-4 hide-scrollbar" id="schedule-filters">
<button data-filter="all" class="filter-btn px-6 py-3 rounded-full border border-slate-800 text-white font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light bg-gradient-to-r from-electric-orange to-vibrant-pink">"""
content = content.replace(filter_search, filter_replace)

content = content.replace('<button class="px-6 py-3 rounded-full bg-surface-elevated border text-white font-label-caps', '<button data-filter="Functional Strength" class="filter-btn px-6 py-3 rounded-full bg-surface-elevated border border-white/20 text-white font-label-caps')
content = content.replace('<button class="px-6 py-3 rounded-full bg-surface-elevated border border-vibrant-yellow', '<button data-filter="GAP" class="filter-btn px-6 py-3 rounded-full bg-surface-elevated border border-white/20')
content = content.replace('<button class="px-6 py-3 rounded-full bg-surface-elevated border border-electric-orange text-electric-orange font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light">\n<span class="material-symbols-outlined text-sm">self_improvement</span>\n                    PILATES FUNCIONAL', '<button data-filter="Pilates Funcional" class="filter-btn px-6 py-3 rounded-full bg-surface-elevated border border-white/20 text-white font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light">\n<span class="material-symbols-outlined text-sm text-electric-orange">self_improvement</span>\n                    PILATES FUNCIONAL')
content = content.replace('<button class="px-6 py-3 rounded-full bg-surface-elevated border border-vibrant-yellow text-vibrant-yellow font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light">\n<span class="material-symbols-outlined text-sm">elderly</span>\n                    +60', '<button data-filter="+60" class="filter-btn px-6 py-3 rounded-full bg-surface-elevated border border-white/20 text-white font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light">\n<span class="material-symbols-outlined text-sm text-vibrant-yellow">elderly</span>\n                    +60')
# Fix GAP button text and icon separately
content = content.replace('text-vibrant-yellow font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light">\n<span class="material-symbols-outlined text-sm">accessibility_new</span>\n                    GAP', 'text-white font-label-caps text-label-caps whitespace-nowrap transition-all flex items-center gap-2 top-light">\n<span class="material-symbols-outlined text-sm text-vibrant-yellow">accessibility_new</span>\n                    GAP')


# Finally, insert `<script src="script.js"></script>` at the end of body if not present
if '<script src="script.js"></script>' not in content:
    content = content.replace('</body>', '<script src="script.js"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html successfully")

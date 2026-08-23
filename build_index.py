"""
Generates a clean index.html for JPS Training based on c335a21 structure,
fixing all encoding issues, title format (white+orange split), and using grid for schedules.
"""

html = '''<!DOCTYPE html>
<html class="dark" lang="es">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>JPS TRAINING - Gimnasio y Entrenamiento de Élite</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,100..900;1,100..900&family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
    tailwind.config = {
        darkMode: "class",
        theme: {
            extend: {
                "colors": {
                    "tertiary-fixed": "#d1e4ff",
                    "surface-container-high": "#2a2a2a",
                    "primary": "#ffb599",
                    "brushed-metal": "#2A2A2A",
                    "steel-silver": "#C0C0C0",
                    "tertiary-fixed-dim": "#9ecaff",
                    "surface-elevated": "#1E1E1E",
                    "on-surface-variant": "#e4bfb1",
                    "surface-bright": "#393939",
                    "vibrant-pink": "#E01E5A",
                    "electric-orange": "#FF8A00",
                    "vibrant-yellow": "#F5C518",
                    "on-surface": "#e5e2e1",
                    "surface": "#131313",
                    "background": "#131313",
                    "surface-container-lowest": "#0e0e0e",
                    "surface-dim": "#131313",
                },
                "fontFamily": {
                    "display-xl": ["Montserrat"],
                    "headline-lg": ["Montserrat"],
                    "headline-md": ["Montserrat"],
                    "stat-value": ["Montserrat"],
                    "label-caps": ["JetBrains Mono"],
                    "body-lg": ["Hanken Grotesk"],
                    "body-md": ["Hanken Grotesk"],
                    "headline-lg-mobile": ["Montserrat"]
                },
                "fontSize": {
                    "display-xl": ["72px", { "lineHeight": "72px", "letterSpacing": "-0.04em", "fontWeight": "900" }],
                    "headline-lg": ["48px", { "lineHeight": "52px", "letterSpacing": "-0.02em", "fontWeight": "800" }],
                    "headline-md": ["24px", { "lineHeight": "32px", "fontWeight": "700" }],
                    "stat-value": ["32px", { "lineHeight": "32px", "fontWeight": "700" }],
                    "label-caps": ["12px", { "lineHeight": "16px", "letterSpacing": "0.1em", "fontWeight": "600" }],
                    "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
                    "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
                    "headline-lg-mobile": ["32px", { "lineHeight": "36px", "letterSpacing": "-0.02em", "fontWeight": "800" }]
                }
            },
        },
    }
</script>
<style>
    .btn-gradient {
        background: linear-gradient(to right, #FF8A00, #E01E5A);
        position: relative; overflow: hidden;
    }
    .btn-gradient::after {
        content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        pointer-events: none;
    }
    .glow-hover:hover { box-shadow: 0 0 25px rgba(255, 138, 0, 0.4); }
    .chiaroscuro-overlay {
        background: linear-gradient(180deg, rgba(19,19,19,0.1) 0%, rgba(19,19,19,0.9) 100%),
                    linear-gradient(90deg, rgba(19,19,19,0.8) 0%, rgba(19,19,19,0.2) 50%, rgba(19,19,19,0.8) 100%);
    }
    .top-highlight { border-top: 2px solid rgba(255,138,0,0.4); }
    .card-acrylic { background: rgba(30,30,30,0.8); border: 1px solid rgba(255,255,255,0.08); }
    .metallic-edge { border-top: 1px solid rgba(255,255,255,0.12); }
    .glow-effect { box-shadow: 0 0 30px rgba(255,138,0,0.2); }
    /* 3D Hero Assets */
    @keyframes float3dLeft {
        0%   { transform: translateY(0px)   rotate(-8deg) scale(1); }
        50%  { transform: translateY(-18px) rotate(-2deg) scale(1.06); }
        100% { transform: translateY(0px)   rotate(-8deg) scale(1); }
    }
    @keyframes float3dRight {
        0%   { transform: translateY(0px)   rotate(8deg)  scale(1); }
        50%  { transform: translateY(-20px) rotate(2deg)  scale(1.06); }
        100% { transform: translateY(0px)   rotate(8deg)  scale(1); }
    }
    .hero-3d-left  { animation: float3dLeft  6s ease-in-out infinite; }
    .hero-3d-right { animation: float3dRight 7s ease-in-out infinite; }
    
    @keyframes lifeInsideLeft {
        0% { transform: scale(1.1) rotate(-15deg); }
        50% { transform: scale(1.25) rotate(15deg); }
        100% { transform: scale(1.1) rotate(-15deg); }
    }
    @keyframes lifeInsideRight {
        0% { transform: scale(1.15) rotate(10deg); }
        50% { transform: scale(1.3) rotate(-10deg); }
        100% { transform: scale(1.15) rotate(10deg); }
    }
    .life-left { animation: lifeInsideLeft 10s ease-in-out infinite; }
    .life-right { animation: lifeInsideRight 12s ease-in-out infinite; }
    
    /* Epic Animations */
    @keyframes heroBgEntry {
        0% { filter: grayscale(0%) brightness(1.2); opacity: 1; transform: scale(1.1); mix-blend-mode: normal; }
        100% { filter: grayscale(100%) brightness(1); opacity: 0.4; transform: scale(1); mix-blend-mode: luminosity; }
    }
    .hero-bg-anim { animation: heroBgEntry 4s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }
    
    @keyframes logoEntryLeft {
        0% { transform: translateX(-150px) rotate(-180deg) scale(0.5); opacity: 0; }
        100% { transform: translateX(0) rotate(0) scale(1); opacity: 1; }
    }
    @keyframes logoEntryRight {
        0% { transform: translateX(150px) rotate(180deg) scale(0.5); opacity: 0; }
        100% { transform: translateX(0) rotate(0) scale(1); opacity: 1; }
    }
    .logo-entry-left { animation: logoEntryLeft 2.5s cubic-bezier(0.34, 1.56, 0.64, 1) 0.5s forwards; opacity: 0; }
    .logo-entry-right { animation: logoEntryRight 2.5s cubic-bezier(0.34, 1.56, 0.64, 1) 0.5s forwards; opacity: 0; }

    @keyframes textEpicEntry {
        0% { transform: translateY(40px) scale(0.9); opacity: 0; filter: blur(10px); }
        100% { transform: translateY(0) scale(1); opacity: 1; filter: blur(0); }
    }
    .text-epic-entry { animation: textEpicEntry 2s cubic-bezier(0.2, 0.8, 0.2, 1) 1.5s forwards; opacity: 0; }
    
    @keyframes assetEntryLeft {
        0% { transform: translateX(-100px) scale(0); opacity: 0; }
        100% { transform: translateX(0) scale(1); opacity: 1; }
    }
    @keyframes assetEntryRight {
        0% { transform: translateX(100px) scale(0); opacity: 0; }
        100% { transform: translateX(0) scale(1); opacity: 1; }
    }
    .asset-entry-left { animation: assetEntryLeft 2s cubic-bezier(0.34, 1.56, 0.64, 1) 2s forwards; opacity: 0; }
    .asset-entry-right { animation: assetEntryRight 2s cubic-bezier(0.34, 1.56, 0.64, 1) 2s forwards; opacity: 0; }
    
    /* Section Title */
    .section-title { border-left: 8px solid #FF8A00; padding-left: 1.5rem; padding-top: 0.5rem; padding-bottom: 0.5rem; }
    /* Plan card transition */
    .plan-card { transition: transform 0.5s ease, box-shadow 0.5s ease, border-color 0.5s ease; }
    /* Filter active */
    .filter-btn.active {
        background: linear-gradient(to right, #FF8A00, #E01E5A) !important;
        border-color: #FF8A00 !important;
        color: white !important;
    }
    /* Staff Modal */
    .staff-modal { display: none; position: fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); backdrop-filter:blur(10px); z-index:9999; }
    .staff-modal-content { background:#1E1E1E; color:#fff; padding:2.5rem; border-radius:16px; max-width:500px; margin:10% auto; position:relative; border:1px solid rgba(255,138,0,0.3); box-shadow:0 0 50px rgba(255,138,0,0.2); }
    .close-btn { position:absolute; top:15px; right:20px; font-size:28px; cursor:pointer; color:#FF8A00; }
</style>
</head>
<body class="bg-background text-on-surface font-body-md antialiased min-h-screen flex flex-col">

<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 bg-background/80 backdrop-blur-xl border-b border-white/10 shadow-2xl transition-all duration-300">
<div class="flex justify-between items-center px-16 h-20 w-full max-w-7xl mx-auto">
    <a class="font-display-xl text-headline-md italic font-black bg-gradient-to-r from-electric-orange to-vibrant-pink bg-clip-text text-transparent tracking-tighter hover:scale-105 transition-transform duration-300" href="#">
        JPS TRAINING
    </a>
    <div class="hidden md:flex items-center gap-8">
        <a class="font-label-caps text-label-caps text-on-surface-variant hover:text-on-surface transition-colors" href="#entrenamiento">Actividades</a>
        <a class="font-label-caps text-label-caps text-on-surface-variant hover:text-on-surface transition-colors" href="#staff">Staff</a>
        <a class="font-label-caps text-label-caps text-on-surface-variant hover:text-on-surface transition-colors" href="#planes">Planes</a>
        <a class="font-label-caps text-label-caps text-on-surface-variant hover:text-on-surface transition-colors" href="#contacto">Contacto</a>
    </div>
    <div class="flex items-center gap-6">
        <button onclick="document.getElementById(\'contacto\').scrollIntoView({behavior:\'smooth\'})"
            class="hidden md:inline-flex items-center justify-center font-label-caps text-label-caps btn-gradient text-white px-6 py-2 rounded-full font-bold glow-hover hover:scale-105 transition-all duration-300">
            ÚNETE AHORA
        </button>
        <button class="md:hidden text-on-surface-variant hover:text-primary transition-colors">
            <span class="material-symbols-outlined">menu</span>
        </button>
    </div>
</div>
</nav>

<!-- Activity Modals -->
<div id="modal-act-hybrid" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAL2qqgFK2xDhqlwcRuId5tqhXPjmdAQv7eBBIaSIhY4qpmddkPNmD_k_4pPNJQ9BkJcfMjbD6LYZMOzC1kJ2GxLWfnpYRMz27JifcrOTfl1WBRTLLqW-jWqry1h_RYGM9vf6kl8FAw3jf8LEH5CCVRp2IfQek-n74E42hstjnCBKBp8tHdCEMzGo_pSsBmLEFc3S001OuoH-BAovJCQO3tX2N5IeeoPXo_--C51vCnk8yEqzfIU8_LWQ');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12 overflow-y-auto">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="HYBRID TRAINING"></h3>
            <p class="typewriter-text font-label-caps text-vibrant-pink font-bold uppercase tracking-widest mb-4" data-text="DESAFÍA TUS LÍMITES" data-delay="600"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-3xl mb-4" data-text="La combinación definitiva de potencia, resistencia y agilidad en una sola sesión de alta intensidad." data-delay="1200"></p>
            <div class="fade-in-block mt-6 border-t border-white/10 pt-4">
                <h4 class="text-white font-bold mb-2">El Entrenamiento:</h4>
                <p class="text-sm text-on-surface-variant mb-4">Un programa integral de acondicionamiento metabólico que fusiona levantamientos de fuerza con un intenso trabajo cardiovascular. A través de transiciones dinámicas utilizando ergómetros (remo, bike), trineos, y movimientos gimnásticos o de peso corporal (burpees, carreras), esta disciplina somete al cuerpo a estímulos variados para forjar un atleta completo.</p>
                <h4 class="text-white font-bold mb-2">Beneficios Principales:</h4>
                <ul class="text-sm text-electric-orange space-y-1 ml-4 list-disc">
                    <li>Maximiza la oxidación de grasas y la quema calórica post-entrenamiento.</li>
                    <li>Dispara la capacidad cardiovascular y pulmonar.</li>
                    <li>Construye resistencia muscular y potencia explosiva de forma simultánea.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div id="modal-act-functional" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBOp4yOQ9BAZr9PM_MBgoAPoYQ1AEFKi2W2kvc61PSJ_t3JXtwADZSexK42NoH8a2ZX-COBnA-jo89ZYREyp0uDUgSc_yG9o8K8ZM4G0zShfL6afeW3PPluxqrvrYaspu9zzER_WuU3mjke5gOy5taX9B9mttRzmStIbByQTRkH40pHk2b6c-Rgvl6hPsVGNEgWlgzrHgbmDbGi_2tyW0vikVZzCIIxIgarrYN6r9d_36miELo0d0yB1Q');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12 overflow-y-auto">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="FUNCTIONAL STRENGTH"></h3>
            <p class="typewriter-text font-label-caps text-electric-orange font-bold uppercase tracking-widest mb-4" data-text="CONSTRUYE UN CUERPO MÁS FUERTE Y PREPARADO" data-delay="600"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-3xl mb-4" data-text="Entrenamiento inteligente para dominar cualquier desafío físico de la vida diaria y el deporte." data-delay="1200"></p>
            <div class="fade-in-block mt-6 border-t border-white/10 pt-4">
                <h4 class="text-white font-bold mb-2">El Entrenamiento:</h4>
                <p class="text-sm text-on-surface-variant mb-4">Trabajo de fuerza fundamentado en la biomecánica humana. Utilizando barras, mancuernas, pesas rusas y equipamiento especializado, nos enfocamos en patrones de movimiento multiplanares (empujes, tracciones, sentadillas y bisagras). El objetivo es priorizar la técnica impecable y la sobrecarga progresiva para transferir esa fuerza a la vida diaria y al deporte.</p>
                <h4 class="text-white font-bold mb-2">Beneficios Principales:</h4>
                <ul class="text-sm text-electric-orange space-y-1 ml-4 list-disc">
                    <li>Hipertrofia funcional (desarrollo de masa muscular útil y magra).</li>
                    <li>Fortalecimiento profundo del core y control de la estabilidad corporal.</li>
                    <li>Mejora estructural del sistema musculoesquelético para la prevención de lesiones.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div id="modal-act-gap" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBW7Z_zc82KmCs4fAkYXe_bG3JvGEdKgnPvMmoXXHPavdU58DjROEP10gudvmQ7GsKJqont5m12zjJzMLn2Ol7QFRHiZwSFTmdHy_J9jIUZarADTEHqM0UazR757Yy3UXdT1M8i9F2nl3qgJFNbXmSDI32WPSziT2k0T8FeDbsb0_VRy3EBTf2RuLxwN6fI5WWiDP9ct3_ouXhMqkkB5UzU3mLxuZGEeER6l9zDCIXHjsrNcRc9Mz7WTg');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12 overflow-y-auto">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="GAP"></h3>
            <p class="typewriter-text font-label-caps text-vibrant-pink font-bold uppercase tracking-widest mb-4" data-text="GLÚTEOS, ABDOMEN Y PIERNAS" data-delay="600"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-3xl mb-4" data-text="Esculpe, tonifica y fortalece el centro de tu poder. Tensión mecánica enfocada para resultados visibles." data-delay="1200"></p>
            <div class="fade-in-block mt-6 border-t border-white/10 pt-4">
                <h4 class="text-white font-bold mb-2">El Entrenamiento:</h4>
                <p class="text-sm text-on-surface-variant mb-4">Sesión de trabajo localizado de alta precisión enfocada en los grupos musculares más grandes y fuertes del cuerpo. Mediante una combinación estratégica de ejercicios de aislamiento y movimientos compuestos, buscamos generar hipertrofia, resistencia y tono muscular en el tren inferior, integrando desafíos de estabilidad pélvica.</p>
                <h4 class="text-white font-bold mb-2">Beneficios Principales:</h4>
                <ul class="text-sm text-electric-orange space-y-1 ml-4 list-disc">
                    <li>Tonificación extrema y desarrollo muscular en glúteos y piernas.</li>
                    <li>Mejora postural inmediata mediante el fortalecimiento intensivo de la zona media.</li>
                    <li>Aumento de la fuerza base, fundamental para potenciar otros levantamientos.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div id="modal-act-pilates" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuDGqfTIWKpOGcMZeJSZSmhRZQ8vEn3XkIefDflC59APnVv5SQVgH1mnISJtjqaKTPJl8__CiP5Pl-gDZsbdlfLLOCLoUXQCqfFtRFEuGpYlhnwKgtNfKaPuMen0bEJu94yJruFpT9DHM3syBivn9MBFdI4HTHnGR6y_DYp1y_lOzz-a0ujZO4CIJhha-5QHorsVcQvrP0QpWUnoaoeKZb2OtE-KnPUZ0sIygiHMoOOQaZnyWWSuWRNgJA');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12 overflow-y-auto">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="PILATES FUNCIONAL"></h3>
            <p class="typewriter-text font-label-caps text-electric-orange font-bold uppercase tracking-widest mb-4" data-text="CONTROL, PRECISIÓN Y MOVIMIENTO CONSCIENTE" data-delay="600"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-3xl mb-4" data-text="Reprograma tu postura y fortalece tu cuerpo desde el interior hacia afuera." data-delay="1200"></p>
            <div class="fade-in-block mt-4">
                <h4 class="text-white font-bold mb-2">El Entrenamiento:</h4>
                <p class="text-sm text-on-surface-variant mb-4">Una evolución dinámica del método tradicional que integra la biomecánica clínica con el acondicionamiento físico. Enfocado en la alineación articular, el control motor fino y la respiración diafragmática, este sistema utiliza el peso corporal y elementos de resistencia ligera para estabilizar la columna y activar la musculatura estabilizadora profunda.</p>
                <h4 class="text-white font-bold mb-2">Beneficios Principales:</h4>
                <ul class="text-sm text-electric-orange space-y-1 ml-4 list-disc">
                    <li>Reeducación postural, ideal para aliviar tensiones crónicas y prevenir lesiones.</li>
                    <li>Aumento significativo de la flexibilidad y el rango de movimiento articular.</li>
                    <li>Desarrollo de un core inquebrantable sin generar impacto en las articulaciones.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div id="modal-act-60" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuChBeNr57xe-LyAWT59PPujv1nJoQ4GYy42IdpZ9BgLSA1e6GLWOwqvZfY9rGjepIREjYS_E1PCT0ntlKu3O69V2QUwEvZuWX85Pxh9lYIJ0erb8R1VEuYQkR70spqHf3nt8XisbKaJlG7DPVj71lVVd5s9ZRq1jtzqXy2ZAbUugWzVBrKdvp_3sy1fdH7z2Qxz-tUYWB8l-A20cK-hPXCvCg-xMPI5JLtya1PoYWvWyH0xc8MmTaTmdg');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12 overflow-y-auto">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="+60 (ACTIVE AGING)"></h3>
            <p class="typewriter-text font-label-caps text-[#4ADE80] font-bold uppercase tracking-widest mb-4" data-text="VITALIDAD SIN LÍMITES" data-delay="600"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-3xl mb-4" data-text="Entrenamiento inteligente diseñado para que sigas disfrutando de una vida activa, fuerte y plena." data-delay="1200"></p>
            <div class="fade-in-block mt-6 border-t border-white/10 pt-4">
                <h4 class="text-white font-bold mb-2">El Entrenamiento:</h4>
                <p class="text-sm text-on-surface-variant mb-4">Un programa de acondicionamiento físico seguro y completamente adaptado, centrado en preservar y mejorar la calidad de vida. Las sesiones se estructuran de manera amena en torno a ejercicios de fuerza moderada, equilibrio neuromuscular y coordinación, respetando siempre la movilidad individual para garantizar un progreso constante.</p>
                <h4 class="text-white font-bold mb-2">Beneficios Principales:</h4>
                <ul class="text-sm text-electric-orange space-y-1 ml-4 list-disc">
                    <li>Fomento de la densidad ósea y preservación de la masa muscular (prevención de sarcopenia).</li>
                    <li>Mejora drástica del equilibrio y la propiocepción, reduciendo el riesgo de caídas.</li>
                    <li>Aumento de la energía diaria y recuperación de la agilidad para las tareas cotidianas.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div id="modal-act-openbox" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuBZ6JGqivvKAVsASjqNWxZ2HVLqDPbE8loHjG4QSLQBMEtC-k5jM1uasdMROTM1h5v9RZoyNtyfj5gRAjMdoKn05U4XQR3hHq25Jj61M0PVUQpHhNms4rnGpArzQlj9y0RiDFkYgm8HujpUDOAXyDTTeCKdku-rb7VwlL2qI8IKRnfmHYCfLHwXOUOtmOk8Am0LLHzAgZ5cV6mr5cwmasR06VNOl_GlzT1HzSAxmKaxVpERv-cgbnbvrQ');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12 overflow-y-auto">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="OPEN BOX"></h3>
            <p class="typewriter-text font-label-caps text-surface-bright font-bold uppercase tracking-widest mb-4" data-text="TU ESPACIO, TU RITMO, TUS REGLAS" data-delay="600"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-3xl mb-4" data-text="Autonomía total en el entorno JPS para llevar tu programación al siguiente nivel." data-delay="1200"></p>
            <div class="fade-in-block mt-6 border-t border-white/10 pt-4">
                <h4 class="text-white font-bold mb-2">El Espacio:</h4>
                <p class="text-sm text-on-surface-variant mb-4">Un bloque de entrenamiento libre sin instrucción grupal, donde las instalaciones y el equipamiento de primer nivel están a tu entera disposición. Es la oportunidad de disfrutar del ambiente JPS a tu manera para ejecutar rutinas propias, siempre bajo una cultura de respeto por el espacio y cuidado de los materiales.</p>
                <h4 class="text-white font-bold mb-2">Ideal Para:</h4>
                <ul class="text-sm text-electric-orange space-y-1 ml-4 list-disc">
                    <li><span class="font-bold text-white">Complemento Estratégico:</span> Potenciar tu rendimiento en Running o sumar volumen de trabajo a tus sesiones de Hybrid Training.</li>
                    <li><span class="font-bold text-white">Objetivos Específicos:</span> Enfocar tu esfuerzo en rutinas de pura fuerza e hipertrofia, o pulir la técnica en levantamientos complejos.</li>
                    <li><span class="font-bold text-white">Atletas y Competidores:</span> Preparación física enfocada en competencias o en la mejora milimétrica de debilidades personales.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<main class="flex-grow pt-20">

<!-- ═══════════ HERO ═══════════ -->
<section class="relative w-full h-[85vh] min-h-[600px] flex items-center justify-center overflow-hidden">
    <div class="absolute inset-0 z-0">
        <div class="w-full h-full bg-cover bg-center opacity-40 mix-blend-luminosity"
            style="background-image: url('assets/images/hero_bg.jpg')">
        </div>
        <div class="absolute inset-0 chiaroscuro-overlay"></div>
    </div>
    <!-- Kettlebell 3D -->
    <div class="asset-entry-left hidden lg:block absolute left-10 top-1/2 -translate-y-1/2 z-10 w-52 h-52 rounded-3xl overflow-hidden shadow-[0_10px_40px_rgba(224,30,90,0.35)] border border-white/10">
        <img src="assets/images/kettlebell.jpg" alt="Kettlebell JPS" class="life-left w-full h-full object-cover"/>
    </div>
    <!-- Dumbbell 3D -->
    <div class="asset-entry-right hidden lg:block absolute right-10 top-1/2 -translate-y-1/2 z-10 w-52 h-52 rounded-3xl overflow-hidden shadow-[0_10px_40px_rgba(255,138,0,0.35)] border border-white/10">
        <img src="assets/images/dumbbell.jpg" alt="Mancuerna JPS" class="life-right w-full h-full object-cover"/>
    </div>
    <!-- Content -->
    <div class="relative z-20 flex flex-col items-center justify-center text-center px-6 w-full max-w-5xl mx-auto gap-8">
        
        <div class="flex items-center justify-center gap-6 md:gap-12 w-full">
            <!-- Left Logo -->
            <div class="logo-entry-left w-24 h-24 md:w-40 md:h-40 rounded-full overflow-hidden shadow-[0_0_30px_rgba(255,138,0,0.3)] border-4 border-[#FF8A00]/40 bg-surface-elevated flex items-center justify-center transform hover:scale-105 transition-transform duration-500 flex-shrink-0">
                <img alt="JPS Training Logo" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCYp_jqKD1QU0NOJdbPFTWGg4dmxmGhsfU5zLEf_Jnv1cX5uIFI9v7qXpbtzu6i84ub2uOgn3rkR2uWM9tzj3so3de0NBp-Hab2mXbehmbTPxPJ4dgSJPOrSwiO12WCOIYwxeDBBWY-L7Jw4SW5tPJ0bcSdYpI2hWouDpv1jKcIB9mOltaQB0pb0r2NnyO7o52WTqrTzH87-Ey_Oi_0VcqD2eKFlGxSYTa6HgVl9qSI_f679lsNaH3efW1-R3kVPU1DcPs"/>
            </div>
            
            <!-- Central Text -->
            <div class="flex flex-col items-center">
                <h1 class="text-epic-entry font-display-xl text-headline-lg-mobile md:text-headline-lg text-on-surface uppercase tracking-tight leading-tight">
                    Eleva tu rendimiento al <span class="bg-gradient-to-r from-electric-orange to-vibrant-pink bg-clip-text text-transparent">máximo</span>
                </h1>
                <button onclick="document.getElementById('contacto').scrollIntoView({behavior:'smooth'})"
                    class="text-epic-entry mt-8 group relative inline-flex items-center justify-center px-8 py-4 font-label-caps text-label-caps text-white tracking-widest rounded-full btn-gradient glow-hover transition-all duration-300 hover:-translate-y-1" style="animation-delay: 2.2s;">
                    ÚNETE AL EQUIPO
                    <span class="material-symbols-outlined ml-2 group-hover:translate-x-1 transition-transform">arrow_forward</span>
                </button>
            </div>

            <!-- Right Logo -->
            <div class="logo-entry-right w-24 h-24 md:w-40 md:h-40 rounded-full overflow-hidden shadow-[0_0_30px_rgba(255,138,0,0.3)] border-4 border-[#FF8A00]/40 bg-surface-elevated flex items-center justify-center transform hover:scale-105 transition-transform duration-500 flex-shrink-0">
                <img alt="JPS Training Logo" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCYp_jqKD1QU0NOJdbPFTWGg4dmxmGhsfU5zLEf_Jnv1cX5uIFI9v7qXpbtzu6i84ub2uOgn3rkR2uWM9tzj3so3de0NBp-Hab2mXbehmbTPxPJ4dgSJPOrSwiO12WCOIYwxeDBBWY-L7Jw4SW5tPJ0bcSdYpI2hWouDpv1jKcIB9mOltaQB0pb0r2NnyO7o52WTqrTzH87-Ey_Oi_0VcqD2eKFlGxSYTa6HgVl9qSI_f679lsNaH3efW1-R3kVPU1DcPs"/>
            </div>
        </div>

    </div>
    <div class="absolute bottom-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-brushed-metal to-transparent"></div>
</section>

<!-- ═══════════ UBICACIÓN ═══════════ -->
<section class="w-full py-24 px-6 relative overflow-hidden bg-surface">
<div class="max-w-7xl mx-auto flex flex-col md:flex-row gap-12 items-center">
    <div class="w-full md:w-1/2 flex flex-col gap-6">
        <div class="section-title mb-6">
            <h2 class="font-display-xl text-headline-md md:text-headline-lg font-black uppercase tracking-tight">
                <span class="text-white">NUESTRA </span><span class="text-electric-orange">UBICACIÓN</span>
            </h2>
        </div>
        <p class="font-body-lg text-on-surface-variant max-w-lg">Visítanos en nuestras instalaciones de primer nivel.</p>
        <div class="flex items-start gap-4 mt-4 bg-surface-elevated p-6 rounded-xl border border-brushed-metal hover:border-electric-orange transition-colors group">
            <span class="material-symbols-outlined text-electric-orange text-3xl group-hover:scale-110 transition-transform">location_on</span>
            <div>
                <h3 class="font-headline-md text-body-lg font-bold text-on-surface mb-2">Dirección</h3>
                <p class="font-body-md text-on-surface-variant leading-relaxed">
                    Elías Abdo 162 bis<br/>
                    Entre Rivera y Dr. Ivo<br/>
                    Tacuarembó, Uruguay
                </p>
            </div>
        </div>
    </div>
    <div class="w-full md:w-1/2 h-[400px] rounded-2xl overflow-hidden border-2 border-brushed-metal relative group shadow-2xl">
        <iframe title="Mapa JPS Training" class="w-full h-full grayscale opacity-80 hover:grayscale-0 transition-all duration-500"
            src="https://maps.google.com/maps?q=El%C3%ADas+Abdo+162,+Tacuaremb%C3%B3&t=&z=15&ie=UTF8&iwloc=&output=embed">
        </iframe>
    </div>
</div>
</section>

<!-- ═══════════ ACTIVIDADES ═══════════ -->
<section id="entrenamiento" class="w-full py-20 px-6">
<div class="max-w-7xl mx-auto">
    <div class="section-title mb-12">
        <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black uppercase tracking-tight">
            <span class="text-white">MODALIDADES DE </span><span class="text-electric-orange">ENTRENAMIENTO</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-4">
            Elige tu camino. Entrenamiento de alta intensidad y precisión diseñado para superar tus límites y forjar un rendimiento de élite.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Card 1: Hybrid Training -->
        <div id="card-act-hybrid" class="card-acrylic rounded-xl overflow-hidden group cursor-pointer transition-all duration-500 hover:-translate-y-2 flex flex-col">
            <div class="h-56 relative overflow-hidden shrink-0">
                <div class="absolute inset-0 bg-cover bg-center group-hover:scale-110 transition-transform duration-700"
                    style=\'background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuAL2qqgFK2xDhqlwcRuId5tqhXPjmdAQv7eBBIaSIhY4qpmddkPNmD_k_4pPNJQ9BkJcfMjbD6LYZMOzC1kJ2GxLWfnpYRMz27JifcrOTfl1WBRTLLqW-jWqry1h_RYGM9vf6kl8FAw3jf8LEH5CCVRp2IfQek-n74E42hstjnCBKBp8tHdCEMzGo_pSsBmLEFc3S001OuoH-BAovJCQO3tX2N5IeeoPXo_--C51vCnk8yEqzfIU8_LWQ");\'>
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                <div class="absolute top-4 left-4 z-20">
                    <span class="bg-vibrant-pink text-white font-label-caps text-label-caps px-3 py-1 rounded uppercase tracking-wider text-[10px]">Híbrido</span>
                </div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md font-bold mb-2 text-vibrant-pink group-hover:text-electric-orange transition-colors">Hybrid Training</h3>
                <p class="font-body-md text-on-surface-variant mb-4 flex-grow">La combinación definitiva de potencia, resistencia y agilidad.</p>
                <ul class="space-y-2 mb-6">
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">local_fire_department</span> Oxidación de grasa</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">favorite</span> Capacidad cardiovascular</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">bolt</span> Potencia explosiva</li>
                </ul>
                <div class="flex justify-between items-center border-t border-white/10 pt-4 mt-auto">
                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="material-symbols-outlined text-[18px]">timer</span><span class="font-label-caps text-[11px]">60 MIN</span></div>
                    <span class="material-symbols-outlined text-electric-orange group-hover:translate-x-2 transition-transform duration-300">arrow_forward</span>
                </div>
            </div>
        </div>

        <!-- Card 2: Functional Strength -->
        <div id="card-act-functional" class="card-acrylic rounded-xl overflow-hidden group cursor-pointer transition-all duration-500 hover:-translate-y-2 flex flex-col">
            <div class="h-56 relative overflow-hidden shrink-0">
                <div class="absolute inset-0 bg-cover bg-center group-hover:scale-110 transition-transform duration-700"
                    style=\'background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBOp4yOQ9BAZr9PM_MBgoAPoYQ1AEFKi2W2kvc61PSJ_t3JXtwADZSexK42NoH8a2ZX-COBnA-jo89ZYREyp0uDUgSc_yG9o8K8ZM4G0zShfL6afeW3PPluxqrvrYaspu9zzER_WuU3mjke5gOy5taX9B9mttRzmStIbByQTRkH40pHk2b6c-Rgvl6hPsVGNEgWlgzrHgbmDbGi_2tyW0vikVZzCIIxIgarrYN6r9d_36miELo0d0yB1Q");\'>
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                <div class="absolute top-4 left-4 z-20">
                    <span class="bg-electric-orange text-white font-label-caps text-label-caps px-3 py-1 rounded uppercase tracking-wider text-[10px]">Fuerza</span>
                </div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md font-bold mb-2 text-electric-orange group-hover:text-vibrant-pink transition-colors">Functional Strength</h3>
                <p class="font-body-md text-on-surface-variant mb-4 flex-grow">Construye un cuerpo más fuerte, inteligente y preparado.</p>
                <ul class="space-y-2 mb-6">
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">fitness_center</span> Aumento de fuerza</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">accessibility_new</span> Movilidad articular</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">health_and_safety</span> Prevención de lesiones</li>
                </ul>
                <div class="flex justify-between items-center border-t border-white/10 pt-4 mt-auto">
                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="material-symbols-outlined text-[18px]">timer</span><span class="font-label-caps text-[11px]">60 MIN</span></div>
                    <span class="material-symbols-outlined text-electric-orange group-hover:translate-x-2 transition-transform duration-300">arrow_forward</span>
                </div>
            </div>
        </div>

        <!-- Card 3: GAP -->
        <div id="card-act-gap" class="card-acrylic rounded-xl overflow-hidden group cursor-pointer transition-all duration-500 hover:-translate-y-2 flex flex-col">
            <div class="h-56 relative overflow-hidden shrink-0">
                <div class="absolute inset-0 bg-cover bg-center group-hover:scale-110 transition-transform duration-700"
                    style=\'background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBW7Z_zc82KmCs4fAkYXe_bG3JvGEdKgnPvMmoXXHPavdU58DjROEP10gudvmQ7GsKJqont5m12zjJzMLn2Ol7QFRHiZwSFTmdHy_J9jIUZarADTEHqM0UazR757Yy3UXdT1M8i9F2nl3qgJFNbXmSDI32WPSziT2k0T8FeDbsb0_VRy3EBTf2RuLxwN6fI5WWiDP9ct3_ouXhMqkkB5UzU3mLxuZGEeER6l9zDCIXHjsrNcRc9Mz7WTg");\'>
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                <div class="absolute top-4 left-4 z-20">
                    <span class="bg-surface-bright text-on-surface font-label-caps text-label-caps px-3 py-1 rounded uppercase tracking-wider text-[10px] border border-brushed-metal">Tonificación</span>
                </div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md font-bold mb-2 text-primary group-hover:text-electric-orange transition-colors">GAP</h3>
                <p class="font-body-md text-on-surface-variant mb-4 flex-grow">Esculpe, tonifica y fortalece el centro de tu poder.</p>
                <ul class="space-y-2 mb-6">
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">sports_gymnastics</span> Glúteos y piernas</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">accessibility</span> Fortalecimiento del core</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">model_training</span> Tonificación muscular</li>
                </ul>
                <div class="flex justify-between items-center border-t border-white/10 pt-4 mt-auto">
                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="material-symbols-outlined text-[18px]">timer</span><span class="font-label-caps text-[11px]">60 MIN</span></div>
                    <span class="material-symbols-outlined text-electric-orange group-hover:translate-x-2 transition-transform duration-300">arrow_forward</span>
                </div>
            </div>
        </div>

        <!-- Card 4: Pilates Funcional -->
        <div id="card-act-pilates" class="card-acrylic rounded-xl overflow-hidden group cursor-pointer transition-all duration-500 hover:-translate-y-2 flex flex-col">
            <div class="h-56 relative overflow-hidden shrink-0">
                <div class="absolute inset-0 bg-cover bg-center group-hover:scale-110 transition-transform duration-700"
                    style=\'background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDGqfTIWKpOGcMZeJSZSmhRZQ8vEn3XkIefDflC59APnVv5SQVgH1mnISJtjqaKTPJl8__CiP5Pl-gDZsbdlfLLOCLoUXQCqfFtRFEuGpYlhnwKgtNfKaPuMen0bEJu94yJruFpT9DHM3syBivn9MBFdI4HTHnGR6y_DYp1y_lOzz-a0ujZO4CIJhha-5QHorsVcQvrP0QpWUnoaoeKZb2OtE-KnPUZ0sIygiHMoOOQaZnyWWSuWRNgJA");\'>
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                <div class="absolute top-4 left-4 z-20">
                    <span class="bg-vibrant-pink text-white font-label-caps text-label-caps px-3 py-1 rounded uppercase tracking-wider text-[10px]">Mente &amp; Cuerpo</span>
                </div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md font-bold mb-2 text-vibrant-pink group-hover:text-electric-orange transition-colors">Pilates Funcional</h3>
                <p class="font-body-md text-on-surface-variant mb-4 flex-grow">Control, precisión y movimiento consciente.</p>
                <ul class="space-y-2 mb-6">
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">self_improvement</span> Conexión mente-cuerpo</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">balance</span> Equilibrio y postura</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">airline_seat_recline_normal</span> Flexibilidad profunda</li>
                </ul>
                <div class="flex justify-between items-center border-t border-white/10 pt-4 mt-auto">
                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="material-symbols-outlined text-[18px]">timer</span><span class="font-label-caps text-[11px]">60 MIN</span></div>
                    <span class="material-symbols-outlined text-electric-orange group-hover:translate-x-2 transition-transform duration-300">arrow_forward</span>
                </div>
            </div>
        </div>

        <!-- Card 5: +60 -->
        <div id="card-act-60" class="card-acrylic rounded-xl overflow-hidden group cursor-pointer transition-all duration-500 hover:-translate-y-2 flex flex-col">
            <div class="h-56 relative overflow-hidden shrink-0">
                <div class="absolute inset-0 bg-cover bg-center group-hover:scale-110 transition-transform duration-700"
                    style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuChBeNr57xe-LyAWT59PPujv1nJoQ4GYy42IdpZ9BgLSA1e6GLWOwqvZfY9rGjepIREjYS_E1PCT0ntlKu3O69V2QUwEvZuWX85Pxh9lYIJ0erb8R1VEuYQkR70spqHf3nt8XisbKaJlG7DPVj71lVVd5s9ZRq1jtzqXy2ZAbUugWzVBrKdvp_3sy1fdH7z2Qxz-tUYWB8l-A20cK-hPXCvCg-xMPI5JLtya1PoYWvWyH0xc8MmTaTmdg");'>
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                <div class="absolute top-4 left-4 z-20">
                    <span class="bg-electric-orange text-white font-label-caps text-label-caps px-3 py-1 rounded uppercase tracking-wider text-[10px]">Longevidad</span>
                </div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md font-bold mb-2 text-electric-orange group-hover:text-vibrant-pink transition-colors">+60 (Active Aging)</h3>
                <p class="font-body-md text-on-surface-variant mb-4 flex-grow">Vitalidad sin límites. Entrenamiento inteligente para la salud.</p>
                <ul class="space-y-2 mb-6">
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">favorite_border</span> Mejora cardiovascular</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">bone</span> Salud ósea</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">accessibility_new</span> Fuerza funcional</li>
                </ul>
                <div class="flex justify-between items-center border-t border-white/10 pt-4 mt-auto">
                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="material-symbols-outlined text-[18px]">timer</span><span class="font-label-caps text-[11px]">60 MIN</span></div>
                    <span class="material-symbols-outlined text-electric-orange group-hover:translate-x-2 transition-transform duration-300">arrow_forward</span>
                </div>
            </div>
        </div>

        <!-- Card 6: Open Box -->
        <div id="card-act-openbox" class="card-acrylic rounded-xl overflow-hidden group cursor-pointer transition-all duration-500 hover:-translate-y-2 flex flex-col">
            <div class="h-56 relative overflow-hidden shrink-0">
                <div class="absolute inset-0 bg-cover bg-center group-hover:scale-110 transition-transform duration-700"
                    style=\'background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBZ6JGqivvKAVsASjqNWxZ2HVLqDPbE8loHjG4QSLQBMEtC-k5jM1uasdMROTM1h5v9RZoyNtyfj5gRAjMdoKn05U4XQR3hHq25Jj61M0PVUQpHhNms4rnGpArzQlj9y0RiDFkYgm8HujpUDOAXyDTTeCKdku-rb7VwlL2qI8IKRnfmHYCfLHwXOUOtmOk8Am0LLHzAgZ5cV6mr5cwmasR06VNOl_GlzT1HzSAxmKaxVpERv-cgbnbvrQ");\'>
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10"></div>
                <div class="absolute top-4 left-4 z-20">
                    <span class="bg-surface-bright text-on-surface font-label-caps text-label-caps px-3 py-1 rounded uppercase tracking-wider text-[10px] border border-brushed-metal">Entrenamiento Libre</span>
                </div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md font-bold mb-2 text-on-surface group-hover:text-electric-orange transition-colors">Open Box</h3>
                <p class="font-body-md text-on-surface-variant mb-4 flex-grow">Tu espacio, tu ritmo, tus reglas.</p>
                <ul class="space-y-2 mb-6">
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">schedule</span> Flexibilidad horaria</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">sports_martial_arts</span> Entrenamiento libre</li>
                    <li class="flex items-center gap-2 text-sm text-on-surface-variant"><span class="material-symbols-outlined text-electric-orange text-[16px]">verified</span> Equipamiento premium</li>
                </ul>
                <div class="flex justify-between items-center border-t border-white/10 pt-4 mt-auto">
                    <div class="flex items-center gap-2 text-on-surface-variant"><span class="material-symbols-outlined text-[18px]">timer</span><span class="font-label-caps text-[11px]">TODO EL DÍA</span></div>
                    <span class="material-symbols-outlined text-electric-orange group-hover:translate-x-2 transition-transform duration-300">arrow_forward</span>
                </div>
            </div>
        </div>
    </div>
</div>
</section>

<!-- ═══════════ STAFF ═══════════ -->
<section id="staff" class="w-full py-20 px-6 bg-surface">
<div class="max-w-7xl mx-auto">
    <div class="section-title mb-12">
        <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black uppercase tracking-tight">
            <span class="text-white">NUESTRO STAFF </span><span class="text-electric-orange">DE ÉLITE</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-4">
            Nuestros entrenadores son veteranos de la industria cuidadosamente seleccionados, dedicados a forjar el potencial en bruto en un rendimiento innegable. Sin excusas, solo resultados.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-6 auto-rows-[minmax(300px,_auto)]">
        <!-- Juan Pablo Sena (12 cols - Full width) -->
        <div id="card-juanpablo" class="md:col-span-12 group relative rounded-xl overflow-hidden bg-surface-elevated border border-brushed-metal metallic-edge transition-transform duration-500 hover:-translate-y-2 cursor-pointer h-[500px] md:h-[600px]">
            <div class="absolute inset-0 z-0">
                <img class="w-full h-full object-cover object-top opacity-90 group-hover:opacity-100 transition-opacity duration-500"
                    src="assets/images/jp_sena.jpg"
                    alt="Juan Pablo Sena"/>
                <div class="absolute inset-0 bg-gradient-to-t from-background via-background/60 to-transparent"></div>
            </div>
            <!-- Top Badge -->
            <div class="absolute top-8 left-8 z-20">
                <div class="inline-block bg-vibrant-pink text-white font-label-caps text-[12px] uppercase px-4 py-1.5 rounded tracking-widest font-bold shadow-lg">Entrenador Jefe</div>
            </div>
            <!-- Bottom Content -->
            <div class="relative z-10 p-8 h-full flex flex-col justify-end pointer-events-none">
                <h2 class="font-headline-md text-3xl md:text-4xl text-white mb-1 uppercase italic font-black shadow-black drop-shadow-md">JUAN PABLO SENA</h2>
                <p class="font-label-caps text-primary uppercase tracking-widest mb-4 drop-shadow">Lic. Educación Física &amp; Preparador Físico</p>
                <p class="font-body-md text-on-surface-variant max-w-2xl mb-2 drop-shadow">
                    Especializado en Funcional, Pilates Funcional, Alta Intensidad y metodología Cross Training. En formación Hyrox.
                </p>
                <p class="font-label-caps text-electric-orange text-xs uppercase tracking-widest mt-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 drop-shadow">Hacer click para ver más →</p>
            </div>
        </div>

        <!-- Santiago Hernández (6 cols) -->
        <div id="card-santiago" class="md:col-span-6 group relative rounded-xl overflow-hidden bg-surface-elevated border border-brushed-metal metallic-edge transition-transform duration-500 hover:-translate-y-2 flex flex-col cursor-pointer">
            <div class="h-64 relative overflow-hidden">
                <img class="w-full h-full object-cover object-top opacity-80 group-hover:scale-105 transition-transform duration-700"
                    src="assets/images/santiago_card.jpg"
                    alt="Santiago Hernández"/>
                <div class="absolute inset-0 bg-gradient-to-t from-surface-elevated to-transparent"></div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md text-white uppercase italic">Santiago Hernández</h3>
                <p class="font-label-caps text-electric-orange uppercase tracking-widest mb-4 text-[10px]">Licenciado en Educación Física</p>
                <p class="text-sm text-on-surface-variant mb-4">Especialista en fuerza funcional, desarrollo de potencia y acondicionamiento físico de alto nivel.</p>
                <div class="mt-auto pt-4 border-t border-brushed-metal flex justify-between items-center">
                    <span class="font-label-caps text-on-surface-variant text-[10px]">ENTRENADOR SENIOR</span>
                    <span class="material-symbols-outlined text-steel-silver group-hover:text-primary transition-colors">fitness_center</span>
                </div>
            </div>
        </div>

        <!-- Noelia Lima Latorre (6 cols) -->
        <div id="card-noelia" class="md:col-span-6 group relative rounded-xl overflow-hidden bg-surface-elevated border border-brushed-metal metallic-edge transition-transform duration-500 hover:-translate-y-2 flex flex-col cursor-pointer">
            <div class="h-64 relative overflow-hidden">
                <img class="w-full h-full object-cover object-top opacity-80 group-hover:scale-105 transition-transform duration-700"
                    src="assets/images/noelia_card.jpg"
                    alt="Noelia Lima Latorre"/>
                <div class="absolute inset-0 bg-gradient-to-t from-surface-elevated to-transparent"></div>
            </div>
            <div class="p-6 flex-grow flex flex-col">
                <h3 class="font-headline-md text-headline-md text-white uppercase italic">Noelia Lima Latorre</h3>
                <p class="font-label-caps text-primary uppercase tracking-widest mb-4 text-[10px]">Licenciada en Educación Física</p>
                <p class="text-sm text-on-surface-variant mb-4">Especialista en entrenamiento GAP y acondicionamiento específico para salud y estética corporal.</p>
                <div class="mt-auto pt-4 border-t border-brushed-metal flex justify-between items-center">
                    <span class="font-label-caps text-on-surface-variant text-[10px]">ENTRENADORA SENIOR</span>
                    <span class="material-symbols-outlined text-steel-silver group-hover:text-primary transition-colors">accessibility_new</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Team Banner Full Width -->
    <div class="mt-12 rounded-2xl overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.5)] border border-white/10 relative group h-[400px] md:h-[500px]">
        <div class="absolute inset-0 bg-gradient-to-t from-background via-transparent to-transparent z-10"></div>
        <img class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-700"
            src="assets/images/team_banner.jpg"
            alt="JPS Training Team"/>
        <div class="absolute bottom-6 left-8 z-20">
            <h3 class="font-display-xl text-headline-md md:text-headline-lg text-white font-black italic uppercase tracking-tighter">EL EQUIPO</h3>
            <p class="font-label-caps text-electric-orange tracking-widest text-sm uppercase mt-1">Compromiso. Disciplina. Resultados.</p>
        </div>
    </div>
</div>
</section>

<!-- ═══════════ PLANES ═══════════ -->
<section id="planes" class="w-full py-20 px-6">
<div class="max-w-7xl mx-auto">
    <div class="section-title mb-12">
        <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black uppercase tracking-tight">
            <span class="text-white">ELIGE TU </span><span class="text-electric-orange">PODER</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-4">
            Selecciona el plan que se adapte a tu ambición. Sin compromisos, solo resultados.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto items-end pt-8">
        <!-- Basic -->
        <article class="plan-card bg-surface-elevated border border-brushed-metal rounded-xl p-8 flex flex-col top-highlight relative" data-plan-index="0">
            <div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">BÁSICO</div>
            <div class="mb-8">
                <h2 class="plan-title font-label-caps text-label-caps text-steel-silver mb-2 tracking-widest uppercase">2 veces por semana</h2>
                <div class="flex items-baseline gap-2">
                    <span class="plan-price font-stat-value text-stat-value text-on-surface">$1.650</span>
                    <span class="font-body-md text-on-surface-variant">/ mes</span>
                </div>
            </div>
            <ul class="flex-grow space-y-4 mb-8">
                <li class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-steel-silver text-[20px] mt-0.5">check_circle</span>
                    <span class="font-body-md text-on-surface-variant">Válido para todas las modalidades</span>
                </li>
            </ul>
            <button class="plan-btn w-full py-3 border border-steel-silver text-on-surface font-label-caps text-label-caps uppercase rounded hover:bg-surface-bright transition-colors">EMPEZAR BÁSICO</button>
        </article>

        <!-- Popular -->
        <article class="plan-card bg-surface-elevated border border-brushed-metal rounded-xl p-8 flex flex-col top-highlight relative" data-plan-index="1">
            <div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">MÁS POPULAR</div>
            <div class="mb-8">
                <h2 class="plan-title font-label-caps text-label-caps text-electric-orange mb-2 tracking-widest uppercase">3 veces por semana</h2>
                <div class="flex items-baseline gap-2">
                    <span class="plan-price font-stat-value text-stat-value text-on-surface">$1.900</span>
                    <span class="font-body-md text-on-surface-variant">/ mes</span>
                </div>
            </div>
            <ul class="flex-grow space-y-4 mb-8">
                <li class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-electric-orange text-[20px] mt-0.5" style="font-variation-settings: \'FILL\' 1;">check_circle</span>
                    <span class="font-body-md text-on-surface-variant">Válido para todas las modalidades</span>
                </li>
            </ul>
            <button class="plan-btn w-full py-3 border border-electric-orange text-electric-orange font-label-caps text-label-caps uppercase rounded hover:bg-electric-orange/10 transition-colors">ELEGIR PREMIUM</button>
        </article>

        <!-- Elite -->
        <article class="plan-card bg-surface-elevated border border-brushed-metal rounded-xl p-8 flex flex-col top-highlight relative" data-plan-index="2">
            <div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">PREMIUM ELITE</div>
            <div class="mb-8">
                <h2 class="plan-title font-label-caps text-label-caps text-tertiary-fixed-dim mb-2 tracking-widest uppercase">Ilimitado</h2>
                <div class="flex items-baseline gap-2">
                    <span class="plan-price font-stat-value text-stat-value text-on-surface">$2.100</span>
                    <span class="font-body-md text-on-surface-variant">/ mes</span>
                </div>
            </div>
            <ul class="flex-grow space-y-4 mb-8">
                <li class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-tertiary-fixed-dim text-[20px] mt-0.5">check_circle</span>
                    <span class="font-body-md text-on-surface-variant">Válido para todas las modalidades</span>
                </li>
            </ul>
            <button class="plan-btn w-full py-3 border border-tertiary-fixed-dim text-tertiary-fixed-dim font-label-caps text-label-caps uppercase rounded hover:bg-tertiary-fixed-dim/10 transition-colors">EMPEZAR ELITE</button>
        </article>
    </div>
</div>
</section>

<!-- ═══════════ HORARIOS ═══════════ -->
<section id="horarios" class="w-full py-20 px-6 bg-surface">
<div class="max-w-7xl mx-auto">
    <div class="section-title mb-10">
        <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black uppercase tracking-tight">
            <span class="text-white">HORARIOS DE </span><span class="text-electric-orange">ENTRENAMIENTO</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-4">
            Organiza tu semana y alcanza tu máximo potencial con nuestras clases diseñadas para el rendimiento élite.
        </p>
    </div>

    <!-- Filtros -->
    <div class="flex flex-wrap items-center gap-3 mb-8" id="schedule-filters">
        <button data-filter="all" class="filter-btn active flex items-center gap-2 px-4 py-2 rounded-full border border-[#FF8A00] bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white text-sm font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[18px]">apps</span> TODOS
        </button>
        <button data-filter="Hybrid Training" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/20 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">bolt</span> HYBRID
        </button>
        <button data-filter="Functional Strength" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/20 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">fitness_center</span> FUNCTIONAL STRENGTH
        </button>
        <button data-filter="GAP" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/20 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">accessibility_new</span> GAP
        </button>
        <button data-filter="Pilates Funcional" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/20 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">self_improvement</span> PILATES FUNCIONAL
        </button>
        <button data-filter="+60" class="filter-btn flex items-center gap-2 px-4 py-2 rounded-full border border-white/20 text-on-surface hover:border-[#FF8A00] text-sm font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[18px] text-[#FF8A00]">elderly</span> +60
        </button>
    </div>

    <!-- Grid de Horarios (renderizado por JS) -->
    <div class="overflow-x-auto mb-10">
        <div class="min-w-[800px] w-full grid grid-cols-[auto_repeat(5,1fr)] gap-3 text-center pb-4" id="horarios-grid-container">
            <!-- JS populates this -->
        </div>
    </div>

    <!-- Open Box Banner -->
    <div class="mt-4 bg-surface-elevated rounded-xl border border-brushed-metal p-6 flex flex-col md:flex-row items-center gap-6 top-highlight">
        <div class="w-20 h-20 rounded-xl overflow-hidden flex-shrink-0 border border-white/10 shadow-2xl">
            <img alt="Open Box JPS" class="w-full h-full object-cover"
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuAVv0XO8nuU_T2mfwIyBw0v40S8LpqiAGURVS6-w5yScTQ8_xdB95vJmmL0uFTNNsdIfmQ0qZ9EKOsKF33opl--hmmkU_q-ZwAK1d0t_TZgmFu2EAOByk7sZ00LQ3M1JKbp2EOheCBMc0vAZm0WsIDJMaDDv6PAoUaIzvvFPMRiDZ3K5D9Kvn3tn9MuUei06iuTfdwxalR8zVE3dStqpzwHJsCDj9F3X2uWjqtka0v-ZYzK19fkWYzFOg"/>
        </div>
        <div class="text-center md:text-left">
            <h3 class="font-headline-md text-white uppercase italic"><span class="bg-red-600 text-white px-2 py-1 rounded font-bold">OPEN BOX</span></h3>
            <p class="font-body-md text-on-surface-variant mt-1">Entrenamiento libre disponible durante todo el horario de apertura del gimnasio (06:00 a 21:00), coincidiendo con el horario de clases.</p>
        </div>
    </div>
</div>
</section>

<!-- ═══════════ CONTACTO ═══════════ -->
<section id="contacto" class="w-full py-24 px-6 bg-surface-container-lowest">
<div class="max-w-4xl mx-auto">
    <div class="section-title mb-10">
        <h2 class="font-display-xl text-headline-lg-mobile md:text-headline-lg font-black uppercase tracking-tight">
            <span class="text-white">PONTE EN </span><span class="text-electric-orange">CONTACTO</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-xl mt-4">
            ¿Listo para transformar tu vida? Déjanos tus datos y nos pondremos en contacto contigo a la brevedad.
        </p>
    </div>
    <form class="flex flex-col gap-6 text-left" onsubmit="event.preventDefault(); alert(\'¡Gracias por comunicarte! Te contactaremos a la brevedad.\');">
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
        <button type="submit" class="w-full py-4 rounded-xl font-label-caps font-bold text-white bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] hover:opacity-90 transition-opacity uppercase tracking-widest mt-2">
            Enviar Mensaje
        </button>
    </form>
</div>
</section>

</main>

<footer class="w-full bg-surface-dim border-t border-brushed-metal py-12 px-16 flex flex-col items-center">
    <div class="text-headline-md font-display-xl italic font-black mb-6 bg-gradient-to-r from-electric-orange to-vibrant-pink bg-clip-text text-transparent">
        JPS TRAINING
    </div>
    <div class="flex flex-wrap justify-center gap-6 mb-8">
        <a class="font-body-md text-on-surface-variant hover:text-vibrant-pink transition-colors" href="#">Política de Privacidad</a>
        <a class="font-body-md text-on-surface-variant hover:text-vibrant-pink transition-colors" href="#">Términos de Servicio</a>
        <a class="font-body-md text-on-surface-variant hover:text-vibrant-pink transition-colors" href="#">Preguntas Frecuentes</a>
        <a class="font-body-md text-on-surface-variant hover:text-vibrant-pink transition-colors" href="#">Ubicación</a>
    </div>
    <div class="font-label-caps text-on-surface-variant opacity-60">© 2024 JPS TRAINING. TODOS LOS DERECHOS RESERVADOS.</div>
</footer>

<!-- Staff Modals -->
<div id="modal-juanpablo" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('assets/images/jp_sena.jpg');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="JUAN PABLO SENA"></h3>
            <p class="typewriter-text font-label-caps text-electric-orange font-bold uppercase tracking-widest mb-6" data-text="ENTRENADOR PERSONAL Y PREPARADOR FÍSICO" data-delay="800"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-2xl mb-6" data-text="Licenciado en Educación Física. Especializado en Entrenamiento Funcional, Pilates Funcional, Entrenamiento de alta intensidad y Metodología Cross Training." data-delay="1500"></p>
            <div class="typewriter-text bg-surface/50 p-4 rounded-xl border border-white/10 text-sm text-[#FF8A00] inline-block self-start backdrop-blur-md" data-text="⚡ En formación en entrenamiento Híbrido en Academia Hyrox!" data-delay="3000"></div>
        </div>
    </div>
</div>

<div id="modal-santiago" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('assets/images/santiago_card.jpg');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="SANTIAGO HERNÁNDEZ"></h3>
            <p class="typewriter-text font-label-caps text-electric-orange font-bold uppercase tracking-widest mb-6" data-text="LICENCIADO EN EDUCACIÓN FÍSICA" data-delay="800"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-2xl" data-text="Especialista en fuerza funcional, desarrollo de potencia y acondicionamiento físico de alto nivel." data-delay="1500"></p>
        </div>
    </div>
</div>

<div id="modal-noelia" class="staff-modal">
    <div class="staff-modal-content group">
        <div class="modal-bg" style="background-image: url('assets/images/noelia_card.jpg');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background via-background/90 to-background/40 z-10 rounded-2xl"></div>
        <span class="close-btn z-50">&times;</span>
        <div class="relative z-20 h-full flex flex-col justify-end p-8 md:p-12">
            <h3 class="typewriter-text text-headline-lg-mobile md:text-headline-lg font-display-xl font-black italic text-white uppercase mb-2" data-text="NOELIA LIMA LATORRE"></h3>
            <p class="typewriter-text font-label-caps text-electric-orange font-bold uppercase tracking-widest mb-6" data-text="LICENCIADA EN EDUCACIÓN FÍSICA" data-delay="800"></p>
            <p class="typewriter-text text-body-lg text-on-surface-variant leading-relaxed max-w-2xl" data-text="Especialista en entrenamiento GAP (Glúteos, Abdomen y Piernas) y tonificación muscular." data-delay="1500"></p>
        </div>
    </div>
</div>

<script src="script.js"></script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! {len(html)} bytes written")

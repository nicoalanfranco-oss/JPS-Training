import os

index_filepath = r'c:\Users\nicoa\OneDrive\Documentos\9 - Nico Labs\JPS Training\index.html'
script_filepath = r'c:\Users\nicoa\OneDrive\Documentos\9 - Nico Labs\JPS Training\script.js'

index_content = """<!DOCTYPE html>
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
                    colors: {
                        "primary": "#ffb599",
                        "electric-orange": "#FF8A00",
                        "vibrant-pink": "#E01E5A",
                        "brushed-metal": "#2A2A2A",
                        "surface": "#121212",
                        "surface-elevated": "#1E1E1E",
                        "on-surface": "#FFFFFF",
                        "on-surface-variant": "#A0A0A0"
                    }
                }
            }
        }
    </script>
    <style>
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
    </style>
</head>
<body class="bg-black text-on-surface font-sans antialiased overflow-x-hidden">

<!-- Fixed Header Nav -->
<header class="fixed top-0 left-0 w-full z-50 bg-black/80 backdrop-blur-md border-b border-white/10 px-8 py-4 flex items-center justify-between">
    <div class="flex items-center gap-3">
        <span class="font-display-xl text-xl font-black italic tracking-wider bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent">JPS TRAINING</span>
    </div>
    <nav class="hidden md:flex items-center gap-8 text-sm font-bold tracking-widest uppercase text-on-surface-variant">
        <a href="#entrenamiento" class="hover:text-[#FF8A00] transition-colors">Entrenamiento</a>
        <a href="#staff" class="hover:text-[#FF8A00] transition-colors">Staff</a>
        <a href="#planes" class="hover:text-[#FF8A00] transition-colors">Planes</a>
        <a href="#horarios" class="hover:text-[#FF8A00] transition-colors">Horarios</a>
        <a href="#contacto" class="hover:text-[#FF8A00] transition-colors">Contacto</a>
    </nav>
    <button onclick="document.getElementById('contacto').scrollIntoView({behavior: 'smooth'})" class="px-6 py-2.5 rounded-full bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white text-xs font-bold uppercase tracking-widest hover:opacity-90 transition-opacity">
        ÚNETE AL EQUIPO
    </button>
</header>

<main class="pt-20">

<!-- Hero Section -->
<section class="relative w-full min-h-[90vh] flex items-center justify-center overflow-hidden py-16 px-4">
    <!-- Ambient Overlay -->
    <div class="absolute inset-0 bg-radial-at-c from-[#FF8A00]/10 via-black to-black opacity-60"></div>

    <!-- 3D Floating Asset Left (Kettlebell) -->
    <div class="hidden lg:block absolute left-12 top-1/2 -translate-y-1/2 z-20 hero-3d-left w-64 h-64 rounded-3xl overflow-hidden shadow-[0_10px_40px_rgba(224,30,90,0.3)] border border-white/10">
        <img src="assets/images/kettlebell.jpg" alt="3D Kettlebell JPS" class="w-full h-full object-cover"/>
    </div>

    <!-- Center Hero Content -->
    <div class="relative z-10 flex flex-col items-center justify-center text-center max-w-4xl mx-auto gap-8">
        <!-- Logo -->
        <div class="w-48 h-48 md:w-60 md:h-60 rounded-full overflow-hidden shadow-[0_0_50px_rgba(255,138,0,0.3)] border-4 border-[#FF8A00]/40 bg-surface-elevated flex items-center justify-center transform hover:scale-105 transition-transform duration-500">
            <img alt="JPS Training Logo" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCYp_jqKD1QU0NOJdbPFTWGg4dmxmGhsfU5zLEf_Jnv1cX5uIFI9v7qXpbtzu6i84ub2uOgn3rkR2uWM9tzj3so3de0NBp-Hab2mXbehmbTPxPJ4dgSJPOrSwiO12WCOIYwxeDBBWY-L7Jw4SW5tPJ0bcSdYpI2hWouDpv1jKcIB9mOltaQB0pb0r2NnyO7o52WTqrTzH87-Ey_Oi_0VcqD2eKFlGxSYTa6HgVl9qSI_f679lsNaH3efW1-R3kVPU1DcPs"/>
        </div>

        <h1 class="font-display-xl text-3xl md:text-5xl font-black uppercase tracking-tight max-w-3xl leading-tight">
            Eleva tu rendimiento al <span class="bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent">máximo</span>
        </h1>

        <button onclick="document.getElementById('contacto').scrollIntoView({behavior: 'smooth'})" class="group relative inline-flex items-center justify-center px-10 py-4 font-bold text-white tracking-widest rounded-full bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] shadow-[0_0_30px_rgba(255,138,0,0.4)] hover:scale-105 transition-all duration-300 uppercase text-sm">
            ÚNETE AL EQUIPO
            <span class="material-symbols-outlined ml-2 group-hover:translate-x-1 transition-transform">arrow_forward</span>
        </button>
    </div>

    <!-- 3D Floating Asset Right (Dumbbell) -->
    <div class="hidden lg:block absolute right-12 top-1/2 -translate-y-1/2 z-20 hero-3d-right w-64 h-64 rounded-3xl overflow-hidden shadow-[0_10px_40px_rgba(255,138,0,0.3)] border border-white/10">
        <img src="assets/images/dumbbell.jpg" alt="3D Dumbbell JPS" class="w-full h-full object-cover"/>
    </div>
</section>

<!-- Location Section -->
<section class="w-full py-16 px-6 bg-surface border-t border-white/5">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row gap-12 items-center">
        <div class="w-full md:w-1/2 flex flex-col gap-6">
            <div class="section-title-box">
                <h2 class="font-display-xl text-3xl md:text-4xl font-black italic uppercase">
                    <span class="text-white">NUESTRA </span>
                    <span class="text-[#FF8A00]">UBICACIÓN</span>
                </h2>
                <p class="font-body-lg text-on-surface-variant mt-2">Visítanos en nuestras instalaciones de primer nivel.</p>
            </div>
            <div class="flex items-start gap-4 bg-surface-elevated p-6 rounded-2xl border border-white/10">
                <span class="material-symbols-outlined text-[#FF8A00] text-3xl">location_on</span>
                <div>
                    <h3 class="font-bold text-white mb-1 text-lg">Dirección</h3>
                    <p class="text-on-surface-variant leading-relaxed">
                        Elías abdo 162 bis<br/>
                        Entre rivera y Dr ivo<br/>
                        Tacuarembó, Uruguay
                    </p>
                </div>
            </div>
        </div>
        <div class="w-full md:w-1/2 h-[350px] rounded-2xl overflow-hidden border border-white/10 relative shadow-2xl">
            <iframe title="Mapa JPS" class="w-full h-full grayscale opacity-80 hover:grayscale-0 transition-all duration-500" src="https://maps.google.com/maps?q=El%C3%ADas%20abdo%20162%20bis,%20Tacuaremb%C3%B3&t=&z=15&ie=UTF8&iwloc=&output=embed"></iframe>
        </div>
    </div>
</section>

<!-- Modalidades / Entrenamiento Section -->
<section id="entrenamiento" class="w-full py-20 px-6 max-w-7xl mx-auto">
    <div class="section-title-box">
        <h2 class="font-display-xl text-3xl md:text-5xl font-black italic uppercase">
            <span class="text-white">MODALIDADES DE </span>
            <span class="text-[#FF8A00]">ENTRENAMIENTO</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-2">
            Elige tu camino. Entrenamiento de alta intensidad y precisión diseñado para superar tus límites y forjar un rendimiento de élite.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Card 1 -->
        <div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-colors group">
            <div>
                <span class="bg-[#E01E5A] text-white text-[10px] font-bold uppercase px-3 py-1 rounded tracking-wider">Híbrido</span>
                <h3 class="text-xl font-bold text-white mt-4 mb-2 group-hover:text-[#FF8A00] transition-colors">Hybrid Training</h3>
                <p class="text-sm text-on-surface-variant mb-6">La combinación definitiva de potencia, resistencia y agilidad.</p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>DURACIÓN: 60 MIN</span>
                <span class="material-symbols-outlined text-[#FF8A00]">arrow_forward</span>
            </div>
        </div>

        <!-- Card 2 -->
        <div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-colors group">
            <div>
                <span class="bg-[#FF8A00] text-white text-[10px] font-bold uppercase px-3 py-1 rounded tracking-wider">Fuerza</span>
                <h3 class="text-xl font-bold text-white mt-4 mb-2 group-hover:text-[#FF8A00] transition-colors">Functional Strength</h3>
                <p class="text-sm text-on-surface-variant mb-6">Construye un cuerpo más fuerte, inteligente y preparado.</p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>DURACIÓN: 45 MIN</span>
                <span class="material-symbols-outlined text-[#FF8A00]">arrow_forward</span>
            </div>
        </div>

        <!-- Card 3 -->
        <div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-colors group">
            <div>
                <span class="bg-yellow-500 text-black text-[10px] font-bold uppercase px-3 py-1 rounded tracking-wider">Tonificación</span>
                <h3 class="text-xl font-bold text-white mt-4 mb-2 group-hover:text-[#FF8A00] transition-colors">GAP</h3>
                <p class="text-sm text-on-surface-variant mb-6">Esculpe, tonifica y fortalece el centro de tu poder.</p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>DURACIÓN: 45 MIN</span>
                <span class="material-symbols-outlined text-[#FF8A00]">arrow_forward</span>
            </div>
        </div>

        <!-- Card 4 -->
        <div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-colors group">
            <div>
                <span class="bg-[#E01E5A] text-white text-[10px] font-bold uppercase px-3 py-1 rounded tracking-wider">Mente & Cuerpo</span>
                <h3 class="text-xl font-bold text-white mt-4 mb-2 group-hover:text-[#FF8A00] transition-colors">Pilates Funcional</h3>
                <p class="text-sm text-on-surface-variant mb-6">Control, precisión y movimiento consciente.</p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>DURACIÓN: 50 MIN</span>
                <span class="material-symbols-outlined text-[#FF8A00]">arrow_forward</span>
            </div>
        </div>

        <!-- Card 5 -->
        <div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-colors group">
            <div>
                <span class="bg-[#FF8A00] text-white text-[10px] font-bold uppercase px-3 py-1 rounded tracking-wider">Longevidad</span>
                <h3 class="text-xl font-bold text-white mt-4 mb-2 group-hover:text-[#FF8A00] transition-colors">+60 (Active Aging)</h3>
                <p class="text-sm text-on-surface-variant mb-6">Vitalidad sin límites. Entrenamiento inteligente para la salud.</p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>DURACIÓN: 45 MIN</span>
                <span class="material-symbols-outlined text-[#FF8A00]">arrow_forward</span>
            </div>
        </div>

        <!-- Card 6 -->
        <div class="bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-colors group">
            <div>
                <span class="bg-red-600 text-white text-[10px] font-bold uppercase px-3 py-1 rounded tracking-wider">Entrenamiento Libre</span>
                <h3 class="text-xl font-bold text-white mt-4 mb-2 group-hover:text-[#FF8A00] transition-colors">Open Box</h3>
                <p class="text-sm text-on-surface-variant mb-6">Entrenamiento libre disponible en todo el horario de apertura.</p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>TODO EL DÍA (06:00 - 21:00)</span>
                <span class="material-symbols-outlined text-[#FF8A00]">arrow_forward</span>
            </div>
        </div>
    </div>
</section>

<!-- Staff Section -->
<section id="staff" class="w-full py-20 px-6 max-w-7xl mx-auto">
    <div class="section-title-box">
        <h2 class="font-display-xl text-3xl md:text-5xl font-black italic uppercase">
            <span class="text-white">NUESTRO STAFF </span>
            <span class="text-[#FF8A00]">DE ÉLITE</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-2">
            Nuestros entrenadores son veteranos de la industria cuidadosamente seleccionados, dedicados a forjar el potencial en bruto en un rendimiento innegable. Sin excusas, solo resultados.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Juan Pablo Sena -->
        <div id="card-juanpablo" class="cursor-pointer bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-all hover:-translate-y-2 group">
            <div>
                <div class="inline-block bg-[#E01E5A] text-white text-[10px] font-bold uppercase px-3 py-1 rounded mb-4">Director & Head Coach</div>
                <h3 class="text-2xl font-bold text-white mb-1 uppercase italic">Juan Pablo Sena</h3>
                <p class="text-xs text-[#FF8A00] font-bold uppercase tracking-widest mb-4">Lic. Educación Física & Preparador Físico</p>
                <p class="text-sm text-on-surface-variant line-clamp-3 mb-6">
                    Especializado en Funcional, Pilates Funcional, Alta Intensidad y metodología Cross Training. En formación Hyrox.
                </p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>VER PERFIL COMPLETO</span>
                <span class="material-symbols-outlined text-[#FF8A00] group-hover:translate-x-1 transition-transform">arrow_forward</span>
            </div>
        </div>

        <!-- Santiago Hernández -->
        <div id="card-santiago" class="cursor-pointer bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-all hover:-translate-y-2 group">
            <div>
                <div class="inline-block bg-[#FF8A00] text-white text-[10px] font-bold uppercase px-3 py-1 rounded mb-4">Entrenador Senior</div>
                <h3 class="text-2xl font-bold text-white mb-1 uppercase italic">Santiago Hernández</h3>
                <p class="text-xs text-[#FF8A00] font-bold uppercase tracking-widest mb-4">Lic. Educación Física</p>
                <p class="text-sm text-on-surface-variant line-clamp-3 mb-6">
                    Especialista en fuerza funcional, sobrecarga progresiva y desarrollo atlético de alto impacto.
                </p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>VER PERFIL COMPLETO</span>
                <span class="material-symbols-outlined text-[#FF8A00] group-hover:translate-x-1 transition-transform">arrow_forward</span>
            </div>
        </div>

        <!-- Noelia Lima Latorre -->
        <div id="card-noelia" class="cursor-pointer bg-surface-elevated rounded-2xl overflow-hidden border border-white/10 p-6 flex flex-col justify-between hover:border-[#FF8A00] transition-all hover:-translate-y-2 group">
            <div>
                <div class="inline-block bg-yellow-500 text-black text-[10px] font-bold uppercase px-3 py-1 rounded mb-4">Entrenadora Senior</div>
                <h3 class="text-2xl font-bold text-white mb-1 uppercase italic">Noelia Lima Latorre</h3>
                <p class="text-xs text-[#FF8A00] font-bold uppercase tracking-widest mb-4">Lic. Educación Física</p>
                <p class="text-sm text-on-surface-variant line-clamp-3 mb-6">
                    Especialista en entrenamiento GAP y acondicionamiento específico para salud y estética corporal.
                </p>
            </div>
            <div class="border-t border-white/10 pt-4 flex justify-between items-center text-xs text-on-surface-variant">
                <span>VER PERFIL COMPLETO</span>
                <span class="material-symbols-outlined text-[#FF8A00] group-hover:translate-x-1 transition-transform">arrow_forward</span>
            </div>
        </div>
    </div>
</section>

<!-- Planes / Pricing Section -->
<section id="planes" class="w-full py-20 px-6 max-w-7xl mx-auto">
    <div class="section-title-box">
        <h2 class="font-display-xl text-3xl md:text-5xl font-black italic uppercase">
            <span class="text-white">ELIGE TU </span>
            <span class="text-[#FF8A00]">PODER</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-2">
            Selecciona el plan que se adapte a tu ambición. Sin compromisos, solo resultados.
        </p>
    </div>

    <!-- Pricing Grid (3 aligned cards initially) -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-end pt-8" id="pricing-grid">
        <!-- Card 1 -->
        <article class="plan-card bg-surface-elevated border border-white/10 rounded-2xl p-8 flex flex-col relative transition-all duration-500" data-plan-index="0">
            <div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">
                EMPEZAR BÁSICO
            </div>
            <div class="mb-8">
                <h3 class="plan-title font-label-caps text-[#FF8A00] text-sm font-bold tracking-widest uppercase mb-2">2 VECES X SEMANA</h3>
                <div class="flex items-baseline gap-2">
                    <span class="plan-price font-display-xl text-4xl md:text-5xl font-black text-white">$1.650</span>
                    <span class="text-on-surface-variant text-sm">/ mes</span>
                </div>
            </div>
            <ul class="flex-grow space-y-4 mb-8">
                <li class="flex items-center gap-3 text-on-surface-variant text-sm">
                    <span class="material-symbols-outlined text-[#FF8A00] text-[20px]">check_circle</span>
                    Válido para todas las modalidades
                </li>
            </ul>
            <button onclick="document.getElementById('contacto').scrollIntoView({behavior: 'smooth'})" class="plan-btn w-full py-4 border border-white/20 text-white font-bold text-xs uppercase tracking-widest rounded-xl transition-all duration-300">
                EMPEZAR BÁSICO
            </button>
        </article>

        <!-- Card 2 -->
        <article class="plan-card bg-surface-elevated border border-white/10 rounded-2xl p-8 flex flex-col relative transition-all duration-500" data-plan-index="1">
            <div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">
                MÁS POPULAR
            </div>
            <div class="mb-8">
                <h3 class="plan-title font-label-caps text-[#FF8A00] text-sm font-bold tracking-widest uppercase mb-2">3 VECES X SEMANA</h3>
                <div class="flex items-baseline gap-2">
                    <span class="plan-price font-display-xl text-4xl md:text-5xl font-black text-white">$1.900</span>
                    <span class="text-on-surface-variant text-sm">/ mes</span>
                </div>
            </div>
            <ul class="flex-grow space-y-4 mb-8">
                <li class="flex items-center gap-3 text-on-surface-variant text-sm">
                    <span class="material-symbols-outlined text-[#FF8A00] text-[20px]">check_circle</span>
                    Válido para todas las modalidades
                </li>
            </ul>
            <button onclick="document.getElementById('contacto').scrollIntoView({behavior: 'smooth'})" class="plan-btn w-full py-4 border border-white/20 text-white font-bold text-xs uppercase tracking-widest rounded-xl transition-all duration-300">
                ELEGIR PREMIUM
            </button>
        </article>

        <!-- Card 3 -->
        <article class="plan-card bg-surface-elevated border border-white/10 rounded-2xl p-8 flex flex-col relative transition-all duration-500" data-plan-index="2">
            <div class="plan-badge hidden absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-5 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg whitespace-nowrap">
                PREMIUM ELITE
            </div>
            <div class="mb-8">
                <h3 class="plan-title font-label-caps text-[#FF8A00] text-sm font-bold tracking-widest uppercase mb-2">ILIMITADO</h3>
                <div class="flex items-baseline gap-2">
                    <span class="plan-price font-display-xl text-4xl md:text-5xl font-black text-white">$2.100</span>
                    <span class="text-on-surface-variant text-sm">/ mes</span>
                </div>
            </div>
            <ul class="flex-grow space-y-4 mb-8">
                <li class="flex items-center gap-3 text-on-surface-variant text-sm">
                    <span class="material-symbols-outlined text-[#FF8A00] text-[20px]">check_circle</span>
                    Válido para todas las modalidades
                </li>
            </ul>
            <button onclick="document.getElementById('contacto').scrollIntoView({behavior: 'smooth'})" class="plan-btn w-full py-4 border border-white/20 text-white font-bold text-xs uppercase tracking-widest rounded-xl transition-all duration-300">
                EMPEZAR ELITE
            </button>
        </article>
    </div>
</section>

<!-- Horarios Section -->
<section id="horarios" class="w-full py-20 px-6 max-w-7xl mx-auto">
    <div class="section-title-box">
        <h2 class="font-display-xl text-3xl md:text-5xl font-black italic uppercase">
            <span class="text-white">HORARIOS DE </span>
            <span class="text-[#FF8A00]">ENTRENAMIENTO</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-2">
            Organiza tu semana y alcanza tu máximo potencial con nuestras clases diseñadas para el rendimiento élite.
        </p>
    </div>

    <!-- Filter Badges -->
    <div class="flex flex-wrap items-center justify-start gap-3 mb-8 w-full" id="schedule-filters">
        <button data-filter="all" class="filter-btn active flex items-center gap-2 px-5 py-2.5 rounded-full border border-[#FF8A00] bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white text-xs font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[16px]">apps</span> TODOS
        </button>
        <button data-filter="Hybrid Training" class="filter-btn flex items-center gap-2 px-5 py-2.5 rounded-full border border-white/20 text-white hover:border-[#FF8A00] text-xs font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[16px] text-[#FF8A00]">bolt</span> HYBRID
        </button>
        <button data-filter="Functional Strength" class="filter-btn flex items-center gap-2 px-5 py-2.5 rounded-full border border-white/20 text-white hover:border-[#FF8A00] text-xs font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[16px] text-[#FF8A00]">fitness_center</span> FUNCTIONAL STRENGTH
        </button>
        <button data-filter="GAP" class="filter-btn flex items-center gap-2 px-5 py-2.5 rounded-full border border-white/20 text-white hover:border-[#FF8A00] text-xs font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[16px] text-[#FF8A00]">accessibility_new</span> GAP
        </button>
        <button data-filter="Pilates Funcional" class="filter-btn flex items-center gap-2 px-5 py-2.5 rounded-full border border-white/20 text-white hover:border-[#FF8A00] text-xs font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[16px] text-[#FF8A00]">self_improvement</span> PILATES FUNCIONAL
        </button>
        <button data-filter="+60" class="filter-btn flex items-center gap-2 px-5 py-2.5 rounded-full border border-white/20 text-white hover:border-[#FF8A00] text-xs font-bold transition-all duration-300">
            <span class="material-symbols-outlined text-[16px] text-[#FF8A00]">elderly</span> +60
        </button>
    </div>

    <!-- Interactive Grid Table (Original visual layout from screenshot 1!) -->
    <div class="overflow-x-auto mb-12">
        <div class="min-w-[850px] w-full grid grid-cols-[auto_repeat(5,1fr)] gap-4 text-center pb-8" id="horarios-grid-container">
            <!-- Dynamic Grid Populated by script.js -->
        </div>
    </div>

    <!-- Open Box Banner -->
    <div class="bg-surface-elevated rounded-2xl border border-white/10 p-6 flex flex-col md:flex-row items-center gap-6">
        <div class="w-16 h-16 rounded-xl bg-red-600 flex items-center justify-center text-white shrink-0 font-bold text-xl">
            <span class="material-symbols-outlined text-3xl">sports_gymnastics</span>
        </div>
        <div>
            <h3 class="text-lg font-bold text-white uppercase italic"><span class="bg-red-600 text-white px-2 py-1 rounded font-bold">OPEN BOX</span></h3>
            <p class="text-sm text-on-surface-variant mt-1">Entrenamiento libre disponible durante todo el horario de apertura del gimnasio (06:00 a 21:00), coincidiendo con el horario de clases.</p>
        </div>
    </div>
</section>

<!-- Contact Section -->
<section id="contacto" class="w-full py-20 px-6 max-w-7xl mx-auto border-t border-white/5">
    <div class="section-title-box">
        <h2 class="font-display-xl text-3xl md:text-5xl font-black italic uppercase">
            <span class="text-white">PONTE EN </span>
            <span class="text-[#FF8A00]">CONTACTO</span>
        </h2>
        <p class="font-body-lg text-on-surface-variant max-w-2xl mt-2">
            ¿Listo para transformar tu vida? Déjanos tus datos y nos pondremos en contacto contigo a la brevedad.
        </p>
    </div>

    <form class="max-w-3xl flex flex-col gap-6" onsubmit="event.preventDefault(); alert('¡Gracias por comunicarte! Te contactaremos a la brevedad.');">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex flex-col gap-2">
                <label class="text-xs font-bold text-on-surface-variant uppercase tracking-wider">Nombre Completo</label>
                <input type="text" required placeholder="Tu nombre" class="w-full bg-surface-elevated border border-white/10 rounded-xl py-4 px-4 text-white focus:border-[#FF8A00] focus:outline-none"/>
            </div>
            <div class="flex flex-col gap-2">
                <label class="text-xs font-bold text-on-surface-variant uppercase tracking-wider">Teléfono / WhatsApp</label>
                <input type="tel" required placeholder="Tu teléfono" class="w-full bg-surface-elevated border border-white/10 rounded-xl py-4 px-4 text-white focus:border-[#FF8A00] focus:outline-none"/>
            </div>
        </div>
        <div class="flex flex-col gap-2">
            <label class="text-xs font-bold text-on-surface-variant uppercase tracking-wider">Mensaje o Consulta</label>
            <textarea rows="4" placeholder="¿En qué podemos ayudarte?" class="w-full bg-surface-elevated border border-white/10 rounded-xl py-4 px-4 text-white focus:border-[#FF8A00] focus:outline-none"></textarea>
        </div>
        <button type="submit" class="w-full py-4 rounded-xl font-bold text-white bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] hover:opacity-90 transition-opacity uppercase tracking-widest mt-2">
            Enviar Mensaje
        </button>
    </form>
</section>

</main>

<footer class="w-full bg-black border-t border-white/10 py-12 px-6 flex flex-col items-center">
    <div class="text-2xl font-black italic mb-4 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] bg-clip-text text-transparent">
        JPS TRAINING
    </div>
    <p class="text-xs text-on-surface-variant opacity-60">
        © 2024 JPS TRAINING. TODOS LOS DERECHOS RESERVADOS.
    </p>
</footer>

<!-- Modals Container -->
<div id="modal-juanpablo" class="staff-modal">
    <div class="staff-modal-content">
        <span class="close-btn">&times;</span>
        <h3 class="text-2xl font-bold text-[#FF8A00] mb-1">Juan Pablo Sena</h3>
        <p class="text-xs text-white font-bold uppercase tracking-widest mb-4">Entrenador Personal y Preparador Físico</p>
        <p class="text-sm text-on-surface-variant mb-4 leading-relaxed">
            Licenciado en Educación Física. Especializado en Entrenamiento Funcional, Pilates De Hoy (Pilates Funcional), Entrenamiento de alta intensidad y Metodología Cross Training.
        </p>
        <div class="bg-surface p-3 rounded-lg border border-white/10 text-xs text-[#FF8A00]">
            ⚡ En formación en entrenamiento Híbrido en Academia Hyrox!
        </div>
    </div>
</div>

<div id="modal-santiago" class="staff-modal">
    <div class="staff-modal-content">
        <span class="close-btn">&times;</span>
        <h3 class="text-2xl font-bold text-[#FF8A00] mb-1">Santiago Hernández</h3>
        <p class="text-xs text-white font-bold uppercase tracking-widest mb-4">Licenciado en Educación Física</p>
        <p class="text-sm text-on-surface-variant leading-relaxed">
            Especialista en fuerza funcional, desarrollo de potencia y acondicionamiento físico de alto nivel.
        </p>
    </div>
</div>

<div id="modal-noelia" class="staff-modal">
    <div class="staff-modal-content">
        <span class="close-btn">&times;</span>
        <h3 class="text-2xl font-bold text-[#FF8A00] mb-1">Noelia Lima Latorre</h3>
        <p class="text-xs text-white font-bold uppercase tracking-widest mb-4">Licenciada en Educación Física</p>
        <p class="text-sm text-on-surface-variant leading-relaxed">
            Especialista en entrenamiento GAP (Glúteos, Abdomen y Piernas) y tonificación muscular.
        </p>
    </div>
</div>

<script src="script.js"></script>
</body>
</html>
"""

script_content = """document.addEventListener('DOMContentLoaded', () => {
    const API_BASE = 'https://studio-main-1--studio-4748759464-52942.us-east4.hosted.app';
    const GIMNASIO_ID = 'b9cc34ff-0e3b-4564-aa2d-ac3390cf5239';

    async function loadWebData() {
        try {
            const [horariosRes, preciosRes] = await Promise.all([
                fetch(`${API_BASE}/api/web/horarios?gimnasio_id=${GIMNASIO_ID}`),
                fetch(`${API_BASE}/api/web/precios?gimnasio_id=${GIMNASIO_ID}`)
            ]);

            if (horariosRes.ok) {
                const horarios = await horariosRes.json();
                window.allHorarios = horarios || [];
                window.currentFilter = 'all';
                renderScheduleGrid();
            }
            if (preciosRes.ok) {
                const precios = await preciosRes.json();
                renderDynamicPrices(precios || []);
            }
        } catch (error) {
            console.error('Error cargando datos de la web:', error);
        }
    }

    // --- Render Grid like Screenshot 1 ---
    function renderScheduleGrid() {
        const gridContainer = document.getElementById('horarios-grid-container');
        if (!gridContainer) return;

        const horarios = window.allHorarios || [];

        // Unique sorted times
        const timeSet = new Set(horarios.map(h => h.hora.substring(0, 5)));
        const times = Array.from(timeSet).sort();

        // Default times if empty
        if (times.length === 0) {
            times.push('06:00', '07:00', '08:00', '09:00', '13:30', '16:00', '17:00', '18:00', '19:00', '20:00');
        }

        const days = [
            { num: 1, name: 'LUNES' },
            { num: 2, name: 'MARTES' },
            { num: 3, name: 'MIÉRCOLES' },
            { num: 4, name: 'JUEVES' },
            { num: 5, name: 'VIERNES' }
        ];

        let html = '';

        // 1. Header Row
        html += `<div class="py-4 px-2"></div>`;
        days.forEach(d => {
            html += `<div class="bg-[#1E1E1E] rounded-xl border border-white/10 py-4 px-2 font-black text-[#FF8A00] tracking-wider text-xs uppercase shadow-md">${d.name}</div>`;
        });

        // 2. Slots Rows
        times.forEach(timeStr => {
            // Time Column
            html += `<div class="flex items-center justify-end pr-4 font-black text-[#FF8A00] text-sm">${timeStr}</div>`;

            // Day Columns 1 to 5
            days.forEach(day => {
                const match = horarios.find(h => Number(h.dia_semana) === day.num && h.hora.substring(0, 5) === timeStr);

                if (match) {
                    const actName = match.nombre_actividad;
                    let styleClass = 'bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white';
                    let actDisplay = actName.toUpperCase();

                    if (actName.toLowerCase().includes('functional strength')) {
                        styleClass = 'bg-[#1E293B] text-white border border-slate-700';
                        actDisplay = '<span>FUNCTIONAL</span><span>STRENGTH</span>';
                    } else if (actName.toLowerCase().includes('pilates')) {
                        styleClass = 'bg-[#FF8A00] text-black';
                        actDisplay = '<span>PILATES</span><span>FUNCIONAL</span>';
                    } else if (actName.toLowerCase().includes('gap')) {
                        styleClass = 'bg-yellow-500 text-black';
                        actDisplay = 'GAP';
                    } else if (actName.toLowerCase().includes('60')) {
                        styleClass = 'bg-yellow-500 text-black';
                        actDisplay = '+ 60';
                    }

                    html += `
                    <div data-activity="${actName}" class="slot-pill ${styleClass} rounded-xl py-3 px-2 text-xs font-bold uppercase tracking-wider flex flex-col items-center justify-center leading-tight shadow-lg transition-all duration-300">
                        ${actDisplay}
                    </div>`;
                } else {
                    html += `<div class="py-3 px-2"></div>`;
                }
            });
        });

        gridContainer.innerHTML = html;
        applyScheduleFilter();
    }

    function applyScheduleFilter() {
        const filter = window.currentFilter || 'all';
        const slots = document.querySelectorAll('.slot-pill');

        slots.forEach(slot => {
            const act = slot.getAttribute('data-activity') || '';
            if (filter === 'all' || act.toLowerCase().includes(filter.toLowerCase())) {
                slot.style.opacity = '1';
                slot.style.filter = 'none';
                slot.style.pointerEvents = 'auto';
            } else {
                slot.style.opacity = '0.15';
                slot.style.filter = 'grayscale(100%)';
                slot.style.pointerEvents = 'none';
            }
        });
    }

    // --- Setup Filters ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterBtns.forEach(b => {
                b.classList.remove('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'text-white', 'border-[#FF8A00]');
                b.classList.add('border-white/20', 'text-white');
            });
            e.currentTarget.classList.remove('border-white/20', 'text-white');
            e.currentTarget.classList.add('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'text-white', 'border-[#FF8A00]');

            window.currentFilter = e.currentTarget.getAttribute('data-filter');
            applyScheduleFilter();
        });
    });

    // --- Dynamic Pricing Rotation like Request 3 ---
    function renderDynamicPrices(precios) {
        const cards = document.querySelectorAll('.plan-card');
        if (!cards.length) return;

        if (precios && precios.length > 0) {
            precios.slice(0, 3).forEach((plan, i) => {
                if (cards[i]) {
                    const titleEl = cards[i].querySelector('.plan-title');
                    const priceEl = cards[i].querySelector('.plan-price');
                    if (titleEl) titleEl.textContent = plan.modalidad.toUpperCase();
                    if (priceEl) priceEl.textContent = `$${Math.round(plan.ultimo_precio).toLocaleString('es-UY')}`;
                }
            });
        }

        let activeIdx = 1; // start middle card

        function updateHighlight(index) {
            cards.forEach((card, idx) => {
                const badge = card.querySelector('.plan-badge');
                const btn = card.querySelector('.plan-btn');

                if (idx === index) {
                    // Elevate and Glow
                    card.style.transform = 'translateY(-20px) scale(1.03)';
                    card.style.borderColor = '#FF8A00';
                    card.style.boxShadow = '0 0 45px rgba(255, 138, 0, 0.4)';
                    card.style.zIndex = '20';
                    if (badge) badge.classList.remove('hidden');
                    if (btn) {
                        btn.className = 'plan-btn w-full py-4 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white font-bold text-xs uppercase tracking-widest rounded-xl shadow-lg transition-all duration-300';
                    }
                } else {
                    // Reset to equal height
                    card.style.transform = 'translateY(0px) scale(1)';
                    card.style.borderColor = 'rgba(255, 255, 255, 0.1)';
                    card.style.boxShadow = 'none';
                    card.style.zIndex = '1';
                    if (badge) badge.classList.add('hidden');
                    if (btn) {
                        btn.className = 'plan-btn w-full py-4 border border-white/20 text-white font-bold text-xs uppercase tracking-widest rounded-xl transition-all duration-300';
                    }
                }
            });
        }

        updateHighlight(activeIdx);

        setInterval(() => {
            activeIdx = (activeIdx + 1) % cards.length;
            updateHighlight(activeIdx);
        }, 3500);
    }

    loadWebData();

    // --- Setup Modals for Staff ---
    function setupModal(triggerId, modalId) {
        const trigger = document.getElementById(triggerId);
        const modal = document.getElementById(modalId);
        if (!trigger || !modal) return;

        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            modal.style.display = 'block';
        });

        modal.addEventListener('click', (e) => {
            if (e.target === modal || e.target.classList.contains('close-btn')) {
                modal.style.display = 'none';
            }
        });
    }

    // Staff modal styles
    const style = document.createElement('style');
    style.textContent = `
        .staff-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            z-index: 9999;
        }
        .staff-modal-content {
            background: #1E1E1E;
            color: #fff;
            padding: 2.5rem;
            border-radius: 16px;
            max-width: 500px;
            margin: 10% auto;
            position: relative;
            border: 1px solid rgba(255, 138, 0, 0.3);
            box-shadow: 0 0 50px rgba(255, 138, 0, 0.2);
        }
        .close-btn {
            position: absolute; top: 15px; right: 20px;
            font-size: 28px; cursor: pointer; color: #FF8A00;
        }
    `;
    document.head.appendChild(style);

    setupModal('card-noelia', 'modal-noelia');
    setupModal('card-santiago', 'modal-santiago');
    setupModal('card-juanpablo', 'modal-juanpablo');
});
"""

with open(index_filepath, 'w', encoding='utf-8') as f:
    f.write(index_content)

with open(script_filepath, 'w', encoding='utf-8') as f:
    f.write(script_content)

print("HTML and JS rebuilt perfectly!")

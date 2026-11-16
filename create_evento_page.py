# -*- coding: utf-8 -*-
"""
Script to generate the complete Sub-landing for HYBRID GAME JPS (evento.html).
Updated with exact coordinates: [-31.736888, -56.016837]
Official Maps URL: https://maps.app.goo.gl/hSMyVs9ka88JRSyS6
"""
import json
import shutil

# Load schedule data
with open('public/hybrid_schedule.json', 'r', encoding='utf-8') as f:
    schedule_data = json.load(f)

# Load exact route coords (123 waypoints with internal entrance drive into Modena)
with open('public/modena_route.json', 'r', encoding='utf-8') as f:
    route_coords = json.load(f)

coords_json = json.dumps(route_coords)
schedule_json = json.dumps(schedule_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html class="dark" lang="es">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport"/>
    <title>HYBRID GAME JPS 2026 | Sábado 21 de Noviembre • Módena Eventos</title>
    <meta name="description" content="Primera edición del Hybrid Game JPS en Módena Eventos, Tacuarembó. 50 duplas confirmadas, 15 gimnasios del norte del país. ¡Entrada libre y gratuita para el público! Barra Bruma Beer, cantina y sorteos." />
    
    <!-- Open Graph -->
    <meta property="og:title" content="HYBRID GAME JPS | Sábado 21 de Noviembre" />
    <meta property="og:description" content="¡50 duplas, 15 gimnasios y toda la energía! Vení a alentar a tu equipo en Módena Eventos. Entrada gratis para espectadores." />
    <meta property="og:image" content="public/hybrid-barra-bruma.jpg" />
    <meta property="og:type" content="website" />

    <link rel="icon" type="image/png" href="https://lh3.googleusercontent.com/aida-public/AB6AXuCYp_jqKD1QU0NOJdbPFTWGg4dmxmGhsfU5zLEf_Jnv1cX5uIFI9v7qXpbtzu6i84ub2uOgn3rkR2uWM9tzj3so3de0NBp-Hab2mXbehmbTPxPJ4dgSJPOrSwiO12WCOIYwxeDBBWY-L7Jw4SW5tPJ0bcSdYpI2hWouDpv1jKcIB9mOltaQB0pb0r2NnyO7o52WTqrTzH87-Ey_Oi_0VcqD2eKFlGxSYTa6HgVl9qSI_f679lsNaH3efW1-R3kVPU1DcPs" />

    <!-- Tailwind CDN with plugins -->
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>

    <!-- Leaflet CSS & JS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

    <!-- Google Fonts & Material Symbols -->
    <link rel="preconnect" href="https://fonts.googleapis.com"/>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
    <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,300..900;1,300..900&family=JetBrains+Mono:ital,wght@0,400..800;1,400..800&family=Montserrat:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>

    <script id="tailwind-config">
        tailwind.config = {{
            darkMode: "class",
            theme: {{
                extend: {{
                    colors: {{
                        "primary": "#ffb599",
                        "brushed-metal": "#2A2A2A",
                        "steel-silver": "#C0C0C0",
                        "surface-elevated": "#1E1E1E",
                        "on-surface-variant": "#e4bfb1",
                        "surface-bright": "#393939",
                        "vibrant-pink": "#E01E5A",
                        "electric-orange": "#FF8A00",
                        "vibrant-yellow": "#F5C518",
                        "on-surface": "#e5e2e1",
                        "surface": "#131313",
                        "background": "#0c0c10",
                        "surface-container-lowest": "#0a0a0d",
                        "surface-dim": "#111116",
                    }},
                    fontFamily: {{
                        "display": ["Montserrat", "sans-serif"],
                        "mono": ["JetBrains Mono", "monospace"],
                        "body": ["Hanken Grotesk", "sans-serif"]
                    }}
                }},
            }},
        }}
    </script>

    <style>
        html {{
            scroll-behavior: smooth;
            background-color: #0c0c10;
        }}
        body {{
            font-family: 'Hanken Grotesk', sans-serif;
            background-color: #0c0c10;
            color: #e5e2e1;
            overflow-x: hidden;
        }}
        .font-display {{
            font-family: 'Montserrat', sans-serif;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        .btn-gradient {{
            background: linear-gradient(135deg, #FF8A00 0%, #E01E5A 100%);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }}
        .btn-gradient:hover {{
            box-shadow: 0 0 25px rgba(255, 138, 0, 0.5);
            transform: translateY(-2px);
        }}
        .btn-gradient-gold {{
            background: linear-gradient(135deg, #F5C518 0%, #FF8A00 100%);
            transition: all 0.3s ease;
        }}
        .btn-gradient-gold:hover {{
            box-shadow: 0 0 25px rgba(245, 197, 24, 0.4);
            transform: translateY(-2px);
        }}
        .card-acrylic {{
            background: rgba(22, 22, 28, 0.75);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .card-glow-orange {{
            box-shadow: 0 0 35px rgba(255, 138, 0, 0.12);
        }}
        .badge-pulse {{
            animation: pulseAura 2.2s infinite ease-in-out;
        }}
        @keyframes pulseAura {{
            0%, 100% {{ box-shadow: 0 0 0 0 rgba(255, 138, 0, 0.5); }}
            50% {{ box-shadow: 0 0 0 8px rgba(255, 138, 0, 0); }}
        }}

        /* Leaflet Live Map styles (Burguerama inspired for Modena arrival) */
        @keyframes carRadarRing {{
            0% {{ transform: scale(0.6); opacity: 0.95; }}
            100% {{ transform: scale(2.4); opacity: 0; }}
        }}
        .car-pulse-ring {{
            position: absolute;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background-color: #FF8A00;
            animation: carRadarRing 2s infinite ease-out;
            pointer-events: none;
        }}
        @keyframes pinArrivalDrop {{
            0% {{
                transform: translateY(-40px) scale(0.3);
                opacity: 0;
            }}
            60% {{
                transform: translateY(0) scale(1.15);
                opacity: 1;
            }}
            80% {{
                transform: translateY(-6px) scale(0.95);
            }}
            100% {{
                transform: translateY(0) scale(1);
                opacity: 1;
            }}
        }}
        @keyframes storeCardPop {{
            0% {{
                transform: translate(-50%, 15px) scale(0.6);
                opacity: 0;
            }}
            65% {{
                transform: translate(-50%, -4px) scale(1.05);
                opacity: 1;
            }}
            100% {{
                transform: translate(-50%, 0) scale(1);
                opacity: 1;
            }}
        }}
        .pin-drop-anim {{
            animation: pinArrivalDrop 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }}
        .store-card-pop-anim {{
            animation: storeCardPop 0.65s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s both;
        }}
        .leaflet-container {{
            background-color: #111116 !important;
            font-family: inherit !important;
            cursor: pointer !important;
        }}
        .leaflet-tile {{
            filter: brightness(0.75) contrast(1.2) saturate(0.85) invert(0.9) hue-rotate(180deg);
        }}
        .custom-leaflet-marker {{
            background: transparent !important;
            border: none !important;
        }}

        /* Subtle scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: #0d0d12;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #2A2A2A;
            border-radius: 9999px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #FF8A00;
        }}

        /* Filter chip active style */
        .filter-chip.active {{
            background: linear-gradient(135deg, #FF8A00, #E01E5A);
            color: #ffffff;
            border-color: #FF8A00;
            box-shadow: 0 4px 14px rgba(255, 138, 0, 0.35);
        }}
    </style>
</head>
<body class="bg-background text-on-surface antialiased min-h-screen flex flex-col selection:bg-electric-orange selection:text-white">

    <!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-electric-orange via-vibrant-pink to-electric-orange text-white text-xs font-mono font-bold py-2 px-4 text-center tracking-wide flex items-center justify-center gap-2 sticky top-0 z-50 shadow-lg">
        <span class="w-2 h-2 rounded-full bg-white animate-ping"></span>
        <span>¡ESTE SÁBADO 21 DE NOVIEMBRE EN MÓDENA EVENTOS! ENTRADA LIBRE Y GRATUITA PARA ESPECTADORES 🍻</span>
        <a href="#como-llegar" class="underline hover:opacity-80 transition-opacity ml-1 hidden sm:inline">Cómo llegar &rarr;</a>
    </div>

    <!-- Main Navigation Bar -->
    <header class="w-full bg-surface-dim/90 backdrop-blur-xl border-b border-white/10 sticky top-[33px] z-40 transition-all">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            
            <!-- Left: Back to JPS + Brand -->
            <div class="flex items-center gap-4">
                <a href="index.html" class="flex items-center gap-1.5 text-xs font-mono font-bold text-on-surface-variant hover:text-white bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-full border border-white/10 transition-colors" title="Regresar a la página principal de JPS Training">
                    <span class="material-symbols-outlined text-[16px]">arrow_back</span>
                    <span>JPS Training</span>
                </a>
                
                <div class="h-6 w-px bg-white/15 hidden sm:block"></div>

                <a href="#inicio" class="flex items-center gap-2 group">
                    <span class="font-display font-black text-xl sm:text-2xl tracking-tighter bg-gradient-to-r from-electric-orange via-primary to-vibrant-pink bg-clip-text text-transparent group-hover:scale-105 transition-transform">
                        HYBRID GAME
                    </span>
                    <span class="font-mono text-[10px] font-black uppercase px-2 py-0.5 rounded bg-electric-orange/20 text-electric-orange border border-electric-orange/40">
                        1ª EDICIÓN
                    </span>
                </a>
            </div>

            <!-- Desktop Nav Links -->
            <nav class="hidden md:flex items-center gap-6 text-xs font-mono font-bold text-on-surface-variant">
                <a href="#espectadores" class="hover:text-electric-orange transition-colors">Vení a Alentar</a>
                <a href="#experiencia" class="hover:text-electric-orange transition-colors">Barra Bruma & Comida</a>
                <a href="#fixture" class="hover:text-electric-orange transition-colors flex items-center gap-1">
                    <span>Horarios & Parejas</span>
                    <span class="text-[9px] bg-electric-orange text-white px-1.5 py-0.2 rounded-full">50</span>
                </a>
                <a href="#atletas" class="hover:text-electric-orange transition-colors">Check-In Atletas</a>
                <a href="#como-llegar" class="hover:text-electric-orange transition-colors flex items-center gap-1 text-white">
                    <span class="material-symbols-outlined text-[14px] text-vibrant-pink">near_me</span>
                    <span>Módena Eventos</span>
                </a>
            </nav>

            <!-- Actions Right -->
            <div class="flex items-center gap-2 sm:gap-3">
                <a href="https://maps.app.goo.gl/hSMyVs9ka88JRSyS6" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center gap-1.5 text-xs font-mono font-bold px-3.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 text-white border border-white/15 transition-all" title="Abrir ubicación exacta en Google Maps">
                    <span class="material-symbols-outlined text-[16px] text-red-500">location_on</span>
                    <span>Abrir Maps</span>
                </a>

                <a href="https://api.whatsapp.com/send?text=%C2%A1Hola!%20Te%20comparto%20la%20p%C3%A1gina%20del%20HYBRID%20GAME%20JPS%20este%20s%C3%A1bado%2021%20de%20Noviembre%20en%20M%C3%B3dena%20Eventos.%20%C2%A1Entrada%20gratis%20para%20alentar,%20Barra%20Bruma%20Beer%20y%2050%20duplas!%20Mir%C3%A1%20horarios%20y%20c%C3%B3mo%20llegar%20ac%C3%A1:%20https://jpstraining.uy/evento.html" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-xs font-mono font-bold px-4 py-2 rounded-xl bg-[#25D366] hover:bg-[#20ba59] text-white shadow-lg shadow-[#25d366]/20 transition-all hover:scale-105" title="Compartir este evento por WhatsApp con amigos">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    <span class="hidden sm:inline">Invitar Amigos</span>
                </a>
            </div>

        </div>
    </header>

    <!-- Main Content Container -->
    <main class="flex-grow">

        <!-- ══════════════════════════════════════════════
             HERO SECTION
        ══════════════════════════════════════════════ -->
        <section id="inicio" class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden">
            <!-- Background Ambient Glows -->
            <div class="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-electric-orange/15 rounded-full blur-[140px] pointer-events-none"></div>
            <div class="absolute bottom-0 right-10 w-96 h-96 bg-vibrant-pink/15 rounded-full blur-[120px] pointer-events-none"></div>

            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="text-center max-w-4xl mx-auto">
                    
                    <!-- Top Pill Badges -->
                    <div class="inline-flex flex-wrap items-center justify-center gap-2 mb-6">
                        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-electric-orange/15 border border-electric-orange/40 text-electric-orange font-mono text-xs font-bold badge-pulse">
                            <span class="w-2 h-2 rounded-full bg-electric-orange"></span>
                            <span>SÁBADO 21 DE NOVIEMBRE • 11:00 HS</span>
                        </div>
                        <div class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-white font-mono text-xs font-bold">
                            <span class="material-symbols-outlined text-[14px] text-vibrant-pink">location_on</span>
                            <span>MÓDENA EVENTOS, TACUAREMBÓ</span>
                        </div>
                        <div class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 font-mono text-xs font-black tracking-wider">
                            <span>🎟️ ESPECTADORES GRATIS</span>
                        </div>
                    </div>

                    <!-- Main Event Title -->
                    <h1 class="font-display font-black text-5xl sm:text-7xl lg:text-8xl tracking-tight text-white uppercase italic leading-none mb-6">
                        HYBRID <span class="bg-gradient-to-r from-electric-orange via-vibrant-yellow to-vibrant-pink bg-clip-text text-transparent">GAME</span>
                        <span class="block text-3xl sm:text-4xl lg:text-5xl tracking-widest text-on-surface-variant font-mono not-italic mt-2">
                            JPS TRAINING
                        </span>
                    </h1>

                    <!-- Lead Paragraph focused on spectators and excitement -->
                    <p class="font-body text-lg sm:text-2xl text-on-surface-variant mb-8 max-w-3xl mx-auto leading-relaxed">
                        ¡50 Duplas de Élite confirmadas y 15 gimnasios de todo el norte uruguayo! 
                        <strong class="text-white font-black block sm:inline"> Vení a alentar a tu equipo favorito</strong>, viví la adrenalina del fitness híbrido y disfrutá una jornada imperdible con Barra Bruma Beer, cantina y sorteos.
                    </p>

                    <!-- LIVE COUNTDOWN TIMER -->
                    <div class="card-acrylic rounded-2xl p-4 sm:p-6 mb-10 max-w-xl mx-auto border border-electric-orange/30 shadow-2xl card-glow-orange">
                        <div class="text-xs font-mono font-bold text-electric-orange tracking-widest uppercase mb-3 flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-[16px] animate-spin">timer</span>
                            <span>CUENTA REGRESIVA PARA EL INICIO</span>
                        </div>
                        <div class="grid grid-cols-4 gap-2 sm:gap-4 text-center">
                            <div class="bg-surface-dim/80 rounded-xl p-2.5 sm:p-3 border border-white/5">
                                <span id="cd-days" class="font-display font-black text-2xl sm:text-4xl text-white block">00</span>
                                <span class="font-mono text-[10px] sm:text-xs text-on-surface-variant uppercase">Días</span>
                            </div>
                            <div class="bg-surface-dim/80 rounded-xl p-2.5 sm:p-3 border border-white/5">
                                <span id="cd-hours" class="font-display font-black text-2xl sm:text-4xl text-electric-orange block">00</span>
                                <span class="font-mono text-[10px] sm:text-xs text-on-surface-variant uppercase">Horas</span>
                            </div>
                            <div class="bg-surface-dim/80 rounded-xl p-2.5 sm:p-3 border border-white/5">
                                <span id="cd-minutes" class="font-display font-black text-2xl sm:text-4xl text-white block">00</span>
                                <span class="font-mono text-[10px] sm:text-xs text-on-surface-variant uppercase">Min</span>
                            </div>
                            <div class="bg-surface-dim/80 rounded-xl p-2.5 sm:p-3 border border-white/5">
                                <span id="cd-seconds" class="font-display font-black text-2xl sm:text-4xl text-vibrant-pink block">00</span>
                                <span class="font-mono text-[10px] sm:text-xs text-on-surface-variant uppercase">Seg</span>
                            </div>
                        </div>
                    </div>

                    <!-- Call To Action Buttons -->
                    <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                        <a href="#como-llegar" class="btn-gradient w-full sm:w-auto px-8 py-4 rounded-xl font-mono text-sm font-black text-white uppercase tracking-wider flex items-center justify-center gap-2 shadow-xl">
                            <span class="material-symbols-outlined text-[18px]">directions_car</span>
                            <span>Cómo Llegar a Módena (Ver Auto)</span>
                        </a>
                        <a href="#fixture" class="card-acrylic hover:bg-white/10 text-white border border-white/20 w-full sm:w-auto px-7 py-4 rounded-xl font-mono text-sm font-bold uppercase tracking-wider flex items-center justify-center gap-2 transition-all">
                            <span class="material-symbols-outlined text-[18px] text-electric-orange">format_list_bulleted</span>
                            <span>Ver Horarios & Duplas</span>
                        </a>
                        <a href="public/hybrid-game-fixture.pdf" download="Fixture_Hybrid_Game_JPS.pdf" class="card-acrylic hover:bg-white/10 text-on-surface-variant hover:text-white border border-white/10 w-full sm:w-auto px-5 py-4 rounded-xl font-mono text-xs font-bold uppercase tracking-wider flex items-center justify-center gap-1.5 transition-all" title="Descargar documento oficial en PDF">
                            <span class="material-symbols-outlined text-[18px] text-vibrant-yellow">download</span>
                            <span>Descargar PDF</span>
                        </a>
                    </div>

                </div>
            </div>
        </section>


        <!-- ══════════════════════════════════════════════
             STATS RIBBON
        ══════════════════════════════════════════════ -->
        <section class="border-y border-white/10 bg-surface-dim/60 py-8 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-2 md:grid-cols-5 gap-6 text-center">
                    
                    <div class="p-3">
                        <div class="font-display font-black text-3xl sm:text-4xl text-electric-orange">50</div>
                        <div class="font-mono text-xs font-bold text-white uppercase mt-1">Duplas Confirmadas</div>
                        <div class="text-[11px] text-on-surface-variant font-mono">¡Cupos Agotados!</div>
                    </div>

                    <div class="p-3">
                        <div class="font-display font-black text-3xl sm:text-4xl text-white">15</div>
                        <div class="font-mono text-xs font-bold text-white uppercase mt-1">Gimnasios Unidos</div>
                        <div class="text-[11px] text-on-surface-variant font-mono">Norte de Uruguay 🇺🇾</div>
                    </div>

                    <div class="p-3">
                        <div class="font-display font-black text-3xl sm:text-4xl text-vibrant-pink">6</div>
                        <div class="font-mono text-xs font-bold text-white uppercase mt-1">Categorías</div>
                        <div class="text-[11px] text-on-surface-variant font-mono">Open & Pro (W / M / Mix)</div>
                    </div>

                    <div class="p-3">
                        <div class="font-display font-black text-3xl sm:text-4xl text-emerald-400">100%</div>
                        <div class="font-mono text-xs font-bold text-white uppercase mt-1">Entrada Gratis</div>
                        <div class="text-[11px] text-on-surface-variant font-mono">Espectadores Bienvenidos</div>
                    </div>

                    <div class="col-span-2 md:col-span-1 p-3">
                        <div class="font-display font-black text-3xl sm:text-4xl text-vibrant-yellow">8+ HS</div>
                        <div class="font-mono text-xs font-bold text-white uppercase mt-1">De Fiesta y Fitness</div>
                        <div class="text-[11px] text-on-surface-variant font-mono">Desde las 11:00 hs</div>
                    </div>

                </div>
            </div>
        </section>


        <!-- ══════════════════════════════════════════════
             ESPECTADORES: LA FIESTA DEL FITNESS (POR QUÉ VENIR)
        ══════════════════════════════════════════════ -->
        <section id="espectadores" class="py-16 md:py-24 relative overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                
                <div class="text-center max-w-3xl mx-auto mb-14">
                    <span class="inline-block px-3 py-1 rounded-full bg-electric-orange/15 border border-electric-orange/40 text-electric-orange font-mono text-xs font-black uppercase mb-3">
                        📣 ¡VENÍ A ALENTAR!
                    </span>
                    <h2 class="font-display font-black text-3xl sm:text-5xl uppercase tracking-tight text-white leading-tight mb-4">
                        UNA EXPERIENCIA PENSADA <br class="hidden sm:inline"/>
                        <span class="text-electric-orange">PARA TODA LA COMUNIDAD</span>
                    </h2>
                    <p class="font-body text-base sm:text-lg text-on-surface-variant">
                        No tenés que competir para ser protagonista. Módena Eventos abre sus puertas con acceso totalmente libre para que disfrutes de un sábado espectacular al aire libre apoyando a tus amigos, familia y gimnasios.
                    </p>
                </div>

                <!-- 4 Highlight Cards -->
                <div id="experiencia" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
                    
                    <!-- Barra Bruma -->
                    <div class="card-acrylic rounded-2xl p-6 border-l-4 border-l-electric-orange hover:translate-y-[-4px] transition-all">
                        <div class="w-12 h-12 rounded-xl bg-electric-orange/20 text-electric-orange flex items-center justify-center text-2xl mb-4">
                            🍻
                        </div>
                        <h3 class="font-display font-black text-lg text-white uppercase mb-2">Barra Bruma Beer</h3>
                        <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                            Cerveza artesanal tirada, bien fría y refrescante durante toda la jornada. El punto de encuentro oficial para brindar entre heat y heat.
                        </p>
                    </div>

                    <!-- Cantina y Comida -->
                    <div class="card-acrylic rounded-2xl p-6 border-l-4 border-l-vibrant-pink hover:translate-y-[-4px] transition-all">
                        <div class="w-12 h-12 rounded-xl bg-vibrant-pink/20 text-vibrant-pink flex items-center justify-center text-2xl mb-4">
                            🍔
                        </div>
                        <h3 class="font-display font-black text-lg text-white uppercase mb-2">Cantina & Gastronomía</h3>
                        <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                            Opciones ricas para almorzar, merendar y picar algo rico mientras ves competir a las mejores duplas de la región.
                        </p>
                    </div>

                    <!-- Challenges con Sponsors -->
                    <div class="card-acrylic rounded-2xl p-6 border-l-4 border-l-vibrant-yellow hover:translate-y-[-4px] transition-all">
                        <div class="w-12 h-12 rounded-xl bg-vibrant-yellow/20 text-vibrant-yellow flex items-center justify-center text-2xl mb-4">
                            🎁
                        </div>
                        <h3 class="font-display font-black text-lg text-white uppercase mb-2">Challenges con Premios</h3>
                        <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                            ¡Retos y desafíos especiales de nuestros sponsors para que el público también juegue, participe y se lleve premios geniales!
                        </p>
                    </div>

                    <!-- Tremenda Vista Módena -->
                    <div class="card-acrylic rounded-2xl p-6 border-l-4 border-l-emerald-400 hover:translate-y-[-4px] transition-all">
                        <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl mb-4">
                            👓
                        </div>
                        <h3 class="font-display font-black text-lg text-white uppercase mb-2">Tremenda Vista Panorámica</h3>
                        <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                            El predio de Módena Eventos ofrece comodidades de primer nivel y visión directa a cada estación de ejercicio y pista.
                        </p>
                    </div>

                </div>

                <!-- 3 Client Flyers Showcase (Interactive Lightbox) -->
                <div class="mb-12">
                    <div class="flex items-center justify-between mb-6 flex-wrap gap-2">
                        <div>
                            <span class="font-mono text-xs text-electric-orange uppercase font-bold tracking-wider">AFICHES OFICIALES</span>
                            <h3 class="font-display font-black text-2xl text-white uppercase">Información Gráfica del Evento</h3>
                        </div>
                        <span class="font-mono text-xs text-on-surface-variant">Clic en cualquier render para ampliar</span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        
                        <!-- Flyer 1: Bruma & Fiesta -->
                        <div onclick="openLightbox('public/hybrid-barra-bruma.jpg', 'Barra Bruma Beer, Cantina y Challenges')" class="card-acrylic rounded-2xl overflow-hidden border border-white/10 group cursor-pointer relative hover:border-electric-orange transition-all">
                            <div class="aspect-[4/5] overflow-hidden bg-black/40 relative">
                                <img src="public/hybrid-barra-bruma.jpg" alt="Flyer Barra Bruma Beer y Cantina Hybrid Game JPS" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/>
                                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-80 group-hover:opacity-60 transition-opacity"></div>
                                <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between">
                                    <span class="font-mono text-xs font-bold text-white bg-black/60 backdrop-blur px-2.5 py-1 rounded-md border border-white/20">
                                        🍻 Barra Bruma & Cantina
                                    </span>
                                    <span class="w-8 h-8 rounded-full bg-electric-orange text-white flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
                                        <span class="material-symbols-outlined text-[18px]">zoom_in</span>
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Flyer 2: 50 Duplas & Espectadores Gratis -->
                        <div onclick="openLightbox('public/hybrid-inscripciones-cerradas.jpg', '¡50 Duplas Confirmadas! Espectadores Gratis')" class="card-acrylic rounded-2xl overflow-hidden border border-white/10 group cursor-pointer relative hover:border-electric-orange transition-all">
                            <div class="aspect-[4/5] overflow-hidden bg-black/40 relative">
                                <img src="public/hybrid-inscripciones-cerradas.jpg" alt="Flyer 50 Duplas Confirmadas 15 Gimnasios Espectadores Gratis" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/>
                                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-80 group-hover:opacity-60 transition-opacity"></div>
                                <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between">
                                    <span class="font-mono text-xs font-bold text-white bg-black/60 backdrop-blur px-2.5 py-1 rounded-md border border-white/20">
                                        🎟️ 50 Duplas • Espectadores Gratis
                                    </span>
                                    <span class="w-8 h-8 rounded-full bg-electric-orange text-white flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
                                        <span class="material-symbols-outlined text-[18px]">zoom_in</span>
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Flyer 3: Check-in Atletas -->
                        <div onclick="openLightbox('public/hybrid-checkin.jpg', 'Información Importante de Check-in para Atletas')" class="card-acrylic rounded-2xl overflow-hidden border border-white/10 group cursor-pointer relative hover:border-electric-orange transition-all">
                            <div class="aspect-[4/5] overflow-hidden bg-black/40 relative">
                                <img src="public/hybrid-checkin.jpg" alt="Flyer Check-in Atletas y Documentación Obligatoria" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/>
                                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-80 group-hover:opacity-60 transition-opacity"></div>
                                <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between">
                                    <span class="font-mono text-xs font-bold text-white bg-black/60 backdrop-blur px-2.5 py-1 rounded-md border border-white/20">
                                        📋 Check-in & Reglamento
                                    </span>
                                    <span class="w-8 h-8 rounded-full bg-electric-orange text-white flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
                                        <span class="material-symbols-outlined text-[18px]">zoom_in</span>
                                    </span>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </section>


        <!-- ══════════════════════════════════════════════
             FIXTURE & BUSCADOR INTERACTIVO DE HORARIOS Y DUPLAS
        ══════════════════════════════════════════════ -->
        <section id="fixture" class="py-16 md:py-24 bg-surface-dim/70 border-y border-white/10 relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                
                <!-- Section Header -->
                <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-8">
                    <div>
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-electric-orange/15 border border-electric-orange/40 text-electric-orange font-mono text-xs font-bold uppercase mb-2">
                            <span class="material-symbols-outlined text-[14px]">timer</span> CRONOGRAMA OFICIAL
                        </div>
                        <h2 class="font-display font-black text-3xl sm:text-4xl uppercase text-white">
                            FIXTURE DE HEATS Y PAREJAS
                        </h2>
                        <p class="font-body text-sm sm:text-base text-on-surface-variant max-w-2xl mt-1">
                            Buscá a tu dupla favorita por nombre, gimnasio o categoría. Mirá su horario asignado de largada para estar presente alentando.
                        </p>
                    </div>

                    <a href="public/hybrid-game-fixture.pdf" download="Fixture_Hybrid_Game_JPS.pdf" class="btn-gradient inline-flex items-center gap-2 px-5 py-3 rounded-xl font-mono text-xs font-bold text-white shrink-0 self-start md:self-auto shadow-md">
                        <span class="material-symbols-outlined text-[16px]">picture_as_pdf</span>
                        <span>Descargar Fixture Completo (PDF)</span>
                    </a>
                </div>

                <!-- Interactive Search & Category Filter Controls -->
                <div class="card-acrylic rounded-2xl p-4 sm:p-6 mb-8 border border-white/10 space-y-4">
                    
                    <!-- Search Input -->
                    <div class="relative">
                        <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-on-surface-variant">
                            <span class="material-symbols-outlined text-[20px]">search</span>
                        </span>
                        <input 
                            id="schedule-search" 
                            type="text" 
                            placeholder="Buscar por nombre de atleta, hit o gimnasio... (Ej: Mónica, Nordic, Modo Power, 14:00)" 
                            class="w-full pl-11 pr-10 py-3.5 bg-black/50 border border-white/15 rounded-xl text-white placeholder-on-surface-variant/60 font-body text-sm focus:outline-none focus:border-electric-orange focus:ring-1 focus:ring-electric-orange transition-all"
                        />
                        <button id="schedule-clear" class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-on-surface-variant hover:text-white hidden">
                            <span class="material-symbols-outlined text-[18px]">close</span>
                        </button>
                    </div>

                    <!-- Category Pills Filter -->
                    <div class="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none" id="category-filters">
                        <button class="filter-chip active px-3.5 py-1.5 rounded-full border border-white/15 font-mono text-xs font-bold whitespace-nowrap transition-all" data-category="ALL">
                            Todos (55 Heats)
                        </button>
                        <button class="filter-chip px-3.5 py-1.5 rounded-full border border-white/15 font-mono text-xs font-bold whitespace-nowrap transition-all bg-white/5 hover:bg-white/10" data-category="OPEN WOMEN">
                            Open Women (11:00)
                        </button>
                        <button class="filter-chip px-3.5 py-1.5 rounded-full border border-white/15 font-mono text-xs font-bold whitespace-nowrap transition-all bg-white/5 hover:bg-white/10" data-category="OPEN MEN">
                            Open Men (14:00)
                        </button>
                        <button class="filter-chip px-3.5 py-1.5 rounded-full border border-white/15 font-mono text-xs font-bold whitespace-nowrap transition-all bg-white/5 hover:bg-white/10" data-category="OPEN MIXTO">
                            Open Mixto (14:45)
                        </button>
                        <button class="filter-chip px-3.5 py-1.5 rounded-full border border-white/15 font-mono text-xs font-bold whitespace-nowrap transition-all bg-white/5 hover:bg-white/10" data-category="PRO WOMEN">
                            Pro Women (16:30)
                        </button>
                        <button class="filter-chip px-3.5 py-1.5 rounded-full border border-white/15 font-mono text-xs font-bold whitespace-nowrap transition-all bg-white/5 hover:bg-white/10" data-category="PRO MEN">
                            Pro Men (16:45)
                        </button>
                        <button class="filter-chip px-3.5 py-1.5 rounded-full border border-white/15 font-mono text-xs font-bold whitespace-nowrap transition-all bg-white/5 hover:bg-white/10" data-category="PRO MIXTO">
                            Pro Mixto (17:45)
                        </button>
                    </div>

                    <!-- Quick Counters -->
                    <div class="flex items-center justify-between text-xs font-mono text-on-surface-variant pt-2 border-t border-white/5">
                        <span id="filtered-count">Mostrando 57 eventos</span>
                        <span class="text-electric-orange">⚠️ Cada atleta debe hacer check-in 30 min antes</span>
                    </div>

                </div>

                <!-- Schedule Grid Container -->
                <div id="schedule-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <!-- Populated by JavaScript -->
                </div>

                <!-- Empty State -->
                <div id="schedule-empty" class="hidden text-center py-12 card-acrylic rounded-2xl border border-white/10">
                    <span class="material-symbols-outlined text-4xl text-on-surface-variant mb-2">search_off</span>
                    <p class="font-display font-bold text-lg text-white">No se encontraron duplas</p>
                    <p class="font-body text-sm text-on-surface-variant mt-1">Probá buscando con otro nombre o limpiá los filtros.</p>
                    <button onclick="resetFilters()" class="mt-4 px-4 py-2 rounded-lg bg-electric-orange/20 text-electric-orange border border-electric-orange/40 font-mono text-xs font-bold hover:bg-electric-orange hover:text-white transition-all">
                        Limpiar Búsqueda
                    </button>
                </div>

            </div>
        </section>


        <!-- ══════════════════════════════════════════════
             CHECK-IN ATLETAS & REQUISITOS OBLIGATORIOS
        ══════════════════════════════════════════════ -->
        <section id="atletas" class="py-16 md:py-24 relative overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                
                <div class="card-acrylic rounded-3xl p-6 sm:p-10 md:p-14 border border-electric-orange/40 relative shadow-2xl overflow-hidden">
                    <!-- Decorative watermarks -->
                    <div class="absolute -right-20 -bottom-20 w-80 h-80 rounded-full bg-electric-orange/10 blur-3xl pointer-events-none"></div>

                    <div class="max-w-3xl mb-10">
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-electric-orange/15 border border-electric-orange/40 text-electric-orange font-mono text-xs font-black uppercase mb-3">
                            ⚠️ ACREDITACIÓN OFICIAL
                        </div>
                        <h2 class="font-display font-black text-3xl sm:text-4xl text-white uppercase leading-tight mb-3">
                            INFORMACIÓN IMPORTANTE: <br/>
                            <span class="text-electric-orange">CHECK-IN DE ATLETAS</span>
                        </h2>
                        <p class="font-body text-on-surface-variant text-base">
                            Todos los atletas participantes deberán cumplir con el siguiente protocolo antes de ingresar a la zona de competencia:
                        </p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                        
                        <!-- Regla 1: Horario -->
                        <div class="bg-surface-dim/80 p-5 rounded-2xl border border-white/10 flex items-start gap-4">
                            <div class="w-10 h-10 rounded-xl bg-electric-orange/20 text-electric-orange flex items-center justify-center shrink-0">
                                <span class="material-symbols-outlined text-[22px]">schedule</span>
                            </div>
                            <div>
                                <h4 class="font-display font-bold text-white text-base mb-1">Horario de Check-in</h4>
                                <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                                    Cada dupla deberá realizar el check-in como <strong>mínimo 30 minutos antes</strong> de su horario de largada asignado.
                                </p>
                            </div>
                        </div>

                        <!-- Regla 2: Presentación en Dupla -->
                        <div class="bg-surface-dim/80 p-5 rounded-2xl border border-white/10 flex items-start gap-4">
                            <div class="w-10 h-10 rounded-xl bg-vibrant-pink/20 text-vibrant-pink flex items-center justify-center shrink-0">
                                <span class="material-symbols-outlined text-[22px]">groups</span>
                            </div>
                            <div>
                                <h4 class="font-display font-bold text-white text-base mb-1">Presentación de la Dupla</h4>
                                <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                                    Ambos integrantes de la dupla deberán presentarse <strong>juntos</strong> en la zona de acreditación oficial.
                                </p>
                            </div>
                        </div>

                        <!-- Regla 3: Documentación Obligatoria -->
                        <div class="bg-surface-dim/80 p-5 rounded-2xl border border-white/10 flex items-start gap-4">
                            <div class="w-10 h-10 rounded-xl bg-vibrant-yellow/20 text-vibrant-yellow flex items-center justify-center shrink-0">
                                <span class="material-symbols-outlined text-[22px]">badge</span>
                            </div>
                            <div>
                                <h4 class="font-display font-bold text-white text-base mb-1">Documentación Obligatoria</h4>
                                <ul class="font-body text-sm text-on-surface-variant space-y-1 mt-1">
                                    <li class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-electric-orange"></span> Cédula de Identidad.</li>
                                    <li class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-electric-orange"></span> Carné de salud vigente o certificado de aptitud física.</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Regla 4: Zona de Largada -->
                        <div class="bg-surface-dim/80 p-5 rounded-2xl border border-white/10 flex items-start gap-4">
                            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0">
                                <span class="material-symbols-outlined text-[22px]">flag</span>
                            </div>
                            <div>
                                <h4 class="font-display font-bold text-white text-base mb-1">Luego del Check-in</h4>
                                <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                                    Una vez acreditada, la dupla debe presentarse en la zona de largada <strong>10 minutos antes</strong> de su horario asignado, lista para competir.
                                </p>
                            </div>
                        </div>

                    </div>

                    <!-- Organization Reminder Callout -->
                    <div class="bg-gradient-to-r from-electric-orange/20 to-vibrant-pink/20 border border-electric-orange/40 rounded-2xl p-5 text-center">
                        <p class="font-display font-black text-white text-sm sm:text-base uppercase tracking-wider italic">
                            ¡La organización y la puntualidad también son parte del desafío!
                        </p>
                    </div>

                </div>

            </div>
        </section>


        <!-- ══════════════════════════════════════════════
             CÓMO LLEGAR: ANIMACIÓN DE AUTO LLEGANDO A MÓDENA
        ══════════════════════════════════════════════ -->
        <section id="como-llegar" class="py-16 md:py-24 bg-surface-dim/80 border-t border-white/10 relative overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                
                <!-- Section Header -->
                <div class="text-center max-w-3xl mx-auto mb-10">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-electric-orange/15 border border-electric-orange/40 text-electric-orange font-mono text-xs font-bold uppercase mb-2">
                        <span class="material-symbols-outlined text-[14px]">directions_car</span> RUTA EN VIVO A LA SEDE
                    </div>
                    <h2 class="font-display font-black text-3xl sm:text-5xl uppercase tracking-tight text-white mb-3">
                        CÓMO LLEGAR A <span class="text-electric-orange">MÓDENA EVENTOS</span>
                    </h2>
                    <p class="font-body text-base text-on-surface-variant">
                        Ubicado en un predio privilegiado en Tacuarembó. En Google Maps está marcada la entrada de la calle, y el auto recorre la ruta e ingresa por la entrada hasta el punto exacto donde se ubica el salón y la pista:
                    </p>
                </div>

                <!-- Leaflet Live Route Card (Car animation to Modena) -->
                <div class="card-acrylic rounded-3xl overflow-hidden border border-white/15 shadow-2xl p-3 sm:p-4 mb-8">
                    
                    <!-- Header Info Bar -->
                    <div class="flex flex-wrap items-center justify-between gap-3 px-3 py-2.5 mb-2 bg-surface-dim/90 rounded-2xl border border-white/5">
                        <div class="flex items-center gap-2">
                            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                            <span class="font-mono text-xs font-bold text-white uppercase">Recorrido Oficial Tacuarembó &rarr; Entrada &rarr; Predio Módena</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-mono text-on-surface-variant">4.6 km aprox. • ~8 min</span>
                            <a href="https://maps.app.goo.gl/hSMyVs9ka88JRSyS6" target="_blank" rel="noopener noreferrer" class="font-mono text-xs text-electric-orange hover:underline font-bold inline-flex items-center gap-1" title="Abrir ubicación exacta en Google Maps">
                                <span>Ver en Maps</span>
                                <span class="material-symbols-outlined text-[14px]">open_in_new</span>
                            </a>
                        </div>
                    </div>

                    <!-- Map Container -->
                    <div class="relative w-full h-[420px] sm:h-[500px] rounded-2xl overflow-hidden border border-white/10 select-none shadow-inner group">
                        
                        <div id="live-route-map" class="w-full h-full cursor-pointer" title="Hacé clic para abrir la ubicación exacta en Google Maps"></div>

                        <!-- Top Floating CTA Badge directo a Google Maps -->
                        <a 
                            href="https://maps.app.goo.gl/hSMyVs9ka88JRSyS6" 
                            target="_blank" 
                            rel="noopener noreferrer"
                            class="absolute top-4 right-4 z-[1000] inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-black/85 hover:bg-black text-white text-xs font-mono font-bold backdrop-blur-md border border-white/20 shadow-2xl transition-all hover:scale-105 active:scale-95 hover:text-electric-orange pointer-events-auto"
                            onclick="event.stopPropagation()"
                            title="Abrir la ficha oficial exacta de Módena Eventos en Google Maps"
                        >
                            <span class="material-symbols-outlined text-[16px] text-red-500">location_on</span>
                            <span>Abrir en Google Maps</span>
                            <span class="material-symbols-outlined text-[14px] text-gray-400">arrow_outward</span>
                        </a>

                        <!-- Bottom Floating Indicator -->
                        <div class="absolute bottom-4 left-4 z-[1000] bg-black/80 backdrop-blur-md border border-white/10 rounded-xl px-3 py-2 text-[11px] font-mono text-white pointer-events-none hidden sm:flex items-center gap-2">
                            <span>🚗</span>
                            <span>El auto recorre el camino y entra directo a Módena Eventos</span>
                        </div>

                    </div>

                </div>

                <!-- Location Action Bar & Details -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    
                    <div class="card-acrylic p-6 rounded-2xl border border-white/10">
                        <div class="flex items-center gap-3 mb-2">
                            <span class="material-symbols-outlined text-electric-orange text-2xl">pin_drop</span>
                            <h4 class="font-display font-bold text-white text-base">Ubicación Exacta</h4>
                        </div>
                        <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                            Módena Eventos, Tacuarembó.<br/>
                            <span class="text-xs font-mono text-electric-orange">Coords: -31.736888, -56.016837</span><br/>
                            Acceso directo por calle principal hasta el portón del predio.
                        </p>
                    </div>

                    <div class="card-acrylic p-6 rounded-2xl border border-white/10">
                        <div class="flex items-center gap-3 mb-2">
                            <span class="material-symbols-outlined text-emerald-400 text-2xl">local_parking</span>
                            <h4 class="font-display font-bold text-white text-base">Estacionamiento Amplio</h4>
                        </div>
                        <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                            Gran predio interno con zona de estacionamiento vigilado para vehículos, camionetas y motos de los atletas y espectadores.
                        </p>
                    </div>

                    <div class="card-acrylic p-6 rounded-2xl border border-white/10 flex flex-col justify-between">
                        <div>
                            <div class="flex items-center gap-3 mb-2">
                                <span class="material-symbols-outlined text-vibrant-pink text-2xl">navigation</span>
                                <h4 class="font-display font-bold text-white text-base">Navegar con tu GPS</h4>
                            </div>
                            <p class="font-body text-sm text-on-surface-variant">
                                Abrí el enlace directo en tu celular para activar el GPS de Google Maps o Waze.
                            </p>
                        </div>
                        <a href="https://maps.app.goo.gl/hSMyVs9ka88JRSyS6" target="_blank" rel="noopener noreferrer" class="btn-gradient-gold text-black font-mono font-bold text-xs uppercase px-4 py-2.5 rounded-xl text-center mt-3 shadow-md flex items-center justify-center gap-1.5">
                            <span class="material-symbols-outlined text-[16px]">near_me</span>
                            <span>Iniciar Navegación GPS</span>
                        </a>
                    </div>

                </div>

            </div>
        </section>


        <!-- ══════════════════════════════════════════════
             LOS 15 GIMNASIOS REPRESENTADOS
        ══════════════════════════════════════════════ -->
        <section class="py-14 border-t border-white/10 bg-surface-dim/40">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <span class="font-mono text-xs font-bold text-electric-orange uppercase tracking-wider block mb-2">UNIÓN DEPORTIVA DEL NORTE</span>
                <h3 class="font-display font-black text-2xl sm:text-3xl uppercase text-white mb-8">
                    15 Gimnasios & Equipos Representados
                </h3>

                <div class="flex flex-wrap items-center justify-center gap-3 sm:gap-4 max-w-4xl mx-auto">
                    <span class="px-4 py-2 rounded-xl bg-orange-950/60 border border-orange-500/40 text-orange-400 font-mono text-xs font-bold shadow-sm">
                        🏋️ JPS Training
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-blue-950/60 border border-blue-500/40 text-blue-400 font-mono text-xs font-bold shadow-sm">
                        ⚡ Nordic
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-amber-950/60 border border-amber-500/40 text-amber-400 font-mono text-xs font-bold shadow-sm">
                        💥 Modo Power
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-emerald-400 font-mono text-xs font-bold shadow-sm">
                        🌿 Evolution
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-purple-950/60 border border-purple-500/40 text-purple-400 font-mono text-xs font-bold shadow-sm">
                        🎯 Enfoque
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-rose-950/60 border border-rose-500/40 text-rose-400 font-mono text-xs font-bold shadow-sm">
                        🥊 Charlies
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-lime-950/60 border border-lime-500/40 text-lime-400 font-mono text-xs font-bold shadow-sm">
                        🚴 Strongbike
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-sky-950/60 border border-sky-500/40 text-sky-400 font-mono text-xs font-bold shadow-sm">
                        🏟️ Polideportivo
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-teal-950/60 border border-teal-500/40 text-teal-400 font-mono text-xs font-bold shadow-sm">
                        🔥 Híbrido GC
                    </span>
                    <span class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-on-surface-variant font-mono text-xs font-bold">
                        🇺🇾 Duplas Invitadas & Afiliadas
                    </span>
                </div>
            </div>
        </section>


        <!-- ══════════════════════════════════════════════
             PREGUNTAS FRECUENTES PARA ESPECTADORES
        ══════════════════════════════════════════════ -->
        <section class="py-16 border-t border-white/10 relative">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                
                <div class="text-center mb-10">
                    <span class="font-mono text-xs font-bold text-electric-orange uppercase tracking-wider">RESOLVÉ TUS DUDAS</span>
                    <h3 class="font-display font-black text-2xl sm:text-3xl text-white uppercase mt-1">
                        Preguntas Frecuentes del Público
                    </h3>
                </div>

                <div class="space-y-4">
                    
                    <div class="card-acrylic p-5 rounded-2xl border border-white/10">
                        <h4 class="font-display font-bold text-white text-base mb-1 flex items-center gap-2">
                            <span class="text-electric-orange">¿</span>¿Tiene algún costo la entrada para el público?<span class="text-electric-orange">?</span>
                        </h4>
                        <p class="font-body text-sm text-on-surface-variant">
                            ¡Ninguno! La entrada es <strong>100% libre y gratuita</strong> para toda la familia, amigos y público que quiera venir a disfrutar y alentar.
                        </p>
                    </div>

                    <div class="card-acrylic p-5 rounded-2xl border border-white/10">
                        <h4 class="font-display font-bold text-white text-base mb-1 flex items-center gap-2">
                            <span class="text-electric-orange">¿</span>¿Puedo llevar mate, termo y reposera?<span class="text-electric-orange">?</span>
                        </h4>
                        <p class="font-body text-sm text-on-surface-variant">
                            ¡Claro que sí! El predio de Módena Eventos es amplio y súper cómodo. Podés traer tu reposera para instalarte a ver los heats de la tarde.
                        </p>
                    </div>

                    <div class="card-acrylic p-5 rounded-2xl border border-white/10">
                        <h4 class="font-display font-bold text-white text-base mb-1 flex items-center gap-2">
                            <span class="text-electric-orange">¿</span>¿Habrá comida y bebidas en el lugar?<span class="text-electric-orange">?</span>
                        </h4>
                        <p class="font-body text-sm text-on-surface-variant">
                            Sí, contaremos con la <strong>Barra Bruma Beer</strong> oficial con cerveza artesanal tirada bien fría, además de cantina con diversas opciones de comidas y bebidas sin alcohol.
                        </p>
                    </div>

                    <div class="card-acrylic p-5 rounded-2xl border border-white/10">
                        <h4 class="font-display font-bold text-white text-base mb-1 flex items-center gap-2">
                            <span class="text-electric-orange">¿</span>¿A qué hora empieza y a qué hora termina?<span class="text-electric-orange">?</span>
                        </h4>
                        <p class="font-body text-sm text-on-surface-variant">
                            El primer heat (Open Women) comienza puntual a las <strong>11:00 hs</strong>. La jornada se extiende durante toda la tarde con Open Men, Open Mixto, Pro Women, Pro Men, Pro Mixto y culmina cerca de las <strong>18:30 hs</strong> con la premiación y cierre.
                        </p>
                    </div>

                </div>

            </div>
        </section>

    </main>


    <!-- ══════════════════════════════════════════════
         FOOTER
    ══════════════════════════════════════════════ -->
    <footer class="bg-surface-container-lowest border-t border-white/10 py-12 text-center text-xs font-mono text-on-surface-variant">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-6">
            
            <div class="text-left">
                <div class="font-display font-black text-lg text-white">
                    HYBRID GAME <span class="text-electric-orange">JPS</span>
                </div>
                <div class="text-[11px] text-on-surface-variant mt-0.5">
                    1ª Edición Oficial • Módena Eventos • Tacuarembó, Uruguay
                </div>
            </div>

            <div class="flex items-center gap-4">
                <a href="index.html" class="hover:text-white transition-colors">Inicio JPS</a>
                <span>•</span>
                <a href="#fixture" class="hover:text-white transition-colors">Cronograma</a>
                <span>•</span>
                <a href="#como-llegar" class="hover:text-white transition-colors">Cómo Llegar</a>
                <span>•</span>
                <a href="https://maps.app.goo.gl/hSMyVs9ka88JRSyS6" target="_blank" rel="noopener noreferrer" class="hover:text-electric-orange transition-colors">Google Maps</a>
            </div>

            <div class="text-right">
                <a href="https://api.whatsapp.com/send?phone=59898859708" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 hover:bg-white/10 text-white border border-white/10 transition-colors">
                    <span class="material-symbols-outlined text-[14px] text-emerald-400">chat</span>
                    <span>Contacto Organización</span>
                </a>
            </div>

        </div>
    </footer>


    <!-- ══════════════════════════════════════════════
         LIGHTBOX / MODAL FOR OFFICIAL FLYERS
    ══════════════════════════════════════════════ -->
    <div id="lightbox-modal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex items-center justify-center p-4" onclick="closeLightbox()">
        <div class="relative max-w-4xl max-h-[90vh] flex flex-col items-center" onclick="event.stopPropagation()">
            <button onclick="closeLightbox()" class="absolute -top-12 right-0 text-white/80 hover:text-white text-sm font-mono flex items-center gap-1 bg-white/10 px-3 py-1.5 rounded-full">
                <span>Cerrar</span>
                <span class="material-symbols-outlined text-[16px]">close</span>
            </button>
            <img id="lightbox-img" src="" alt="Flyer ampliado" class="max-w-full max-h-[82vh] object-contain rounded-xl border border-white/20 shadow-2xl"/>
            <p id="lightbox-caption" class="text-white font-mono text-xs mt-3 text-center"></p>
        </div>
    </div>


    <!-- ══════════════════════════════════════════════
         DATA & CLIENT LOGIC SCRIPT
    ══════════════════════════════════════════════ -->
    <script>
        // Injected Schedule Data
        const SCHEDULE_DATA = {schedule_json};

        // Injected Route Coordinates (Car route straight to Modena exact coordinates)
        const ROUTE_COORDS = {coords_json};
        const STORE_COORDS = [-31.736888, -56.016837];
        const START_COORDS = [-31.716055, -55.985788];
        const GOOGLE_MAPS_URL = 'https://maps.app.goo.gl/hSMyVs9ka88JRSyS6';

        // ══════════════════════════════════════════════
        // 1. COUNTDOWN TIMER
        // ══════════════════════════════════════════════
        function initCountdown() {{
            // Target: November 21, 2026, 11:00:00 (Local Time Uruguay UTC-3)
            const targetDate = new Date('2026-11-21T11:00:00-03:00').getTime();

            function update() {{
                const now = new Date().getTime();
                const diff = targetDate - now;

                if (diff <= 0) {{
                    document.getElementById('cd-days').textContent = '00';
                    document.getElementById('cd-hours').textContent = '00';
                    document.getElementById('cd-minutes').textContent = '00';
                    document.getElementById('cd-seconds').textContent = '00';
                    return;
                }}

                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((diff % (1000 * 60)) / 1000);

                document.getElementById('cd-days').textContent = String(days).padStart(2, '0');
                document.getElementById('cd-hours').textContent = String(hours).padStart(2, '0');
                document.getElementById('cd-minutes').textContent = String(minutes).padStart(2, '0');
                document.getElementById('cd-seconds').textContent = String(seconds).padStart(2, '0');
            }}

            update();
            setInterval(update, 1000);
        }}

        // ══════════════════════════════════════════════
        // 2. SCHEDULE RENDERER & INTERACTIVE SEARCH
        // ══════════════════════════════════════════════
        let currentCategory = 'ALL';
        let currentSearchQuery = '';

        function getGymBadgeClass(gymName) {{
            const g = (gymName || '').toLowerCase();
            if (g.includes('jps')) return 'bg-orange-950/60 text-orange-400 border-orange-500/40';
            if (g.includes('nordic')) return 'bg-blue-950/60 text-blue-400 border-blue-500/40';
            if (g.includes('modo power')) return 'bg-amber-950/60 text-amber-400 border-amber-500/40';
            if (g.includes('evolution')) return 'bg-emerald-950/60 text-emerald-400 border-emerald-500/40';
            if (g.includes('enfoque')) return 'bg-purple-950/60 text-purple-400 border-purple-500/40';
            if (g.includes('charlies')) return 'bg-rose-950/60 text-rose-400 border-rose-500/40';
            if (g.includes('strongbike')) return 'bg-lime-950/60 text-lime-400 border-lime-500/40';
            if (g.includes('polideportivo')) return 'bg-sky-950/60 text-sky-400 border-sky-500/40';
            if (g.includes('híbrido')) return 'bg-teal-950/60 text-teal-400 border-teal-500/40';
            return 'bg-white/5 text-on-surface-variant border-white/10';
        }}

        function renderSchedule() {{
            const container = document.getElementById('schedule-container');
            const emptyNotice = document.getElementById('schedule-empty');
            const counter = document.getElementById('filtered-count');

            const filtered = SCHEDULE_DATA.filter(item => {{
                // Category match
                if (currentCategory !== 'ALL') {{
                    if (item.type === 'awards') {{
                        if (currentCategory.includes('OPEN') && !item.title.includes('OPEN')) return false;
                        if (currentCategory.includes('PRO') && !item.title.includes('PRO')) return false;
                    }} else if (item.category !== currentCategory) {{
                        return false;
                    }}
                }}

                // Search query match
                if (currentSearchQuery) {{
                    const q = currentSearchQuery.toLowerCase();
                    if (item.type === 'awards') {{
                        return item.title.toLowerCase().includes(q) || item.time.includes(q);
                    }} else {{
                        const full = `${{item.p1}} ${{item.p2}} ${{item.g1}} ${{item.g2}} ${{item.hit}} ${{item.time}} ${{item.category}}`.toLowerCase();
                        return full.includes(q);
                    }}
                }}

                return true;
            }});

            counter.textContent = `Mostrando ${{filtered.length}} ${{filtered.length === 1 ? 'evento' : 'eventos'}}`;

            if (filtered.length === 0) {{
                container.innerHTML = '';
                emptyNotice.classList.remove('hidden');
                return;
            }}

            emptyNotice.classList.add('hidden');

            container.innerHTML = filtered.map(item => {{
                if (item.type === 'awards') {{
                    return `
                        <div class="col-span-1 md:col-span-2 lg:col-span-3 card-acrylic rounded-2xl p-6 border-2 border-vibrant-yellow/50 bg-gradient-to-r from-amber-950/30 via-surface-dim to-amber-950/30 shadow-xl my-2 flex flex-col sm:flex-row items-center justify-between gap-4">
                            <div class="flex items-center gap-4 text-center sm:text-left">
                                <div class="w-14 h-14 rounded-2xl bg-vibrant-yellow/20 text-vibrant-yellow flex items-center justify-center text-3xl shrink-0">
                                    🏆
                                </div>
                                <div>
                                    <div class="inline-block px-2.5 py-0.5 rounded-full bg-vibrant-yellow/20 text-vibrant-yellow font-mono text-[11px] font-black uppercase mb-1">
                                        ${{item.time}} HS • CEREMONIA OFICIAL
                                    </div>
                                    <h3 class="font-display font-black text-xl text-white uppercase tracking-tight">${{item.title}}</h3>
                                    <p class="font-body text-xs sm:text-sm text-on-surface-variant mt-1">${{item.description}}</p>
                                </div>
                            </div>
                            <span class="px-4 py-2 rounded-xl bg-vibrant-yellow/10 border border-vibrant-yellow/30 text-vibrant-yellow font-mono text-xs font-bold uppercase shrink-0">
                                🎖️ Podio & Premios
                            </span>
                        </div>
                    `;
                }}

                const g1Class = getGymBadgeClass(item.g1);
                const g2Class = getGymBadgeClass(item.g2);

                return `
                    <div class="card-acrylic rounded-2xl p-5 border border-white/10 hover:border-electric-orange/50 transition-all flex flex-col justify-between group">
                        <div>
                            <!-- Header with Time & Category -->
                            <div class="flex items-center justify-between gap-2 mb-3">
                                <div class="flex items-center gap-2">
                                    <span class="px-2.5 py-1 rounded-lg bg-electric-orange/20 text-electric-orange font-mono text-xs font-black">
                                        ${{item.time}} HS
                                    </span>
                                    <span class="font-mono text-[11px] text-on-surface-variant font-bold">
                                        Hit #${{item.hit}}
                                    </span>
                                </div>
                                <span class="font-mono text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-white/5 text-on-surface-variant border border-white/10">
                                    ${{item.category}}
                                </span>
                            </div>

                            <!-- Dupla Athletes -->
                            <div class="space-y-2.5 my-3">
                                <!-- Athlete 1 -->
                                <div class="bg-black/40 p-2.5 rounded-xl border border-white/5 flex items-center justify-between gap-2">
                                    <div class="flex items-center gap-2 min-w-0">
                                        <span class="w-5 h-5 rounded-full bg-electric-orange/20 text-electric-orange flex items-center justify-center text-[10px] font-mono font-bold shrink-0">1</span>
                                        <span class="font-display font-bold text-xs sm:text-sm text-white truncate" title="${{item.p1}}">
                                            ${{item.p1}}
                                        </span>
                                    </div>
                                    <span class="font-mono text-[10px] font-bold px-2 py-0.5 rounded-md border shrink-0 ${{g1Class}}">
                                        ${{item.g1 || 'Independiente'}}
                                    </span>
                                </div>

                                <!-- Athlete 2 -->
                                <div class="bg-black/40 p-2.5 rounded-xl border border-white/5 flex items-center justify-between gap-2">
                                    <div class="flex items-center gap-2 min-w-0">
                                        <span class="w-5 h-5 rounded-full bg-vibrant-pink/20 text-vibrant-pink flex items-center justify-center text-[10px] font-mono font-bold shrink-0">2</span>
                                        <span class="font-display font-bold text-xs sm:text-sm text-white truncate" title="${{item.p2}}">
                                            ${{item.p2}}
                                        </span>
                                    </div>
                                    <span class="font-mono text-[10px] font-bold px-2 py-0.5 rounded-md border shrink-0 ${{g2Class}}">
                                        ${{item.g2 || 'Independiente'}}
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Card Footer with Check-in Alert -->
                        <div class="pt-2 border-t border-white/5 flex items-center justify-between text-[10px] font-mono text-on-surface-variant">
                            <span class="flex items-center gap-1 text-electric-orange/90">
                                <span class="material-symbols-outlined text-[13px]">alarm</span>
                                <span>Check-in 30m antes</span>
                            </span>
                            <span class="text-white/60">Largada asignada</span>
                        </div>
                    </div>
                `;
            }}).join('');
        }}

        function setupFilters() {{
            const chips = document.querySelectorAll('#category-filters button');
            chips.forEach(chip => {{
                chip.addEventListener('click', () => {{
                    chips.forEach(c => c.classList.remove('active'));
                    chip.classList.add('active');
                    currentCategory = chip.getAttribute('data-category');
                    renderSchedule();
                }});
            }});

            const searchInput = document.getElementById('schedule-search');
            const clearBtn = document.getElementById('schedule-clear');

            searchInput.addEventListener('input', (e) => {{
                currentSearchQuery = e.target.value.trim();
                if (currentSearchQuery.length > 0) {{
                    clearBtn.classList.remove('hidden');
                }} else {{
                    clearBtn.classList.add('hidden');
                }}
                renderSchedule();
            }});

            clearBtn.addEventListener('click', () => {{
                searchInput.value = '';
                currentSearchQuery = '';
                clearBtn.classList.add('hidden');
                renderSchedule();
            }});
        }}

        function resetFilters() {{
            currentCategory = 'ALL';
            currentSearchQuery = '';
            document.getElementById('schedule-search').value = '';
            document.getElementById('schedule-clear').classList.add('hidden');
            const chips = document.querySelectorAll('#category-filters button');
            chips.forEach(c => c.classList.remove('active'));
            if (chips[0]) chips[0].classList.add('active');
            renderSchedule();
        }}

        // ══════════════════════════════════════════════
        // 3. LEAFLET LIVE ROUTE MAP ANIMATION (CAR TO EXACT MODENA LOCATION)
        // ══════════════════════════════════════════════
        function getDist(p1, p2) {{
            const dLat = p1[0] - p2[0];
            const dLng = (p1[1] - p2[1]) * Math.cos((p1[0] * Math.PI) / 180);
            return Math.sqrt(dLat * dLat + dLng * dLng);
        }}

        const segmentDistances = [];
        let totalDistance = 0;
        for (let i = 0; i < ROUTE_COORDS.length - 1; i++) {{
            const d = getDist(ROUTE_COORDS[i], ROUTE_COORDS[i + 1]);
            segmentDistances.push(d);
            totalDistance += d;
        }}

        function getPointAt(t) {{
            if (t <= 0) return {{ latLng: ROUTE_COORDS[0], segIndex: 0 }};
            if (t >= 1) return {{ latLng: ROUTE_COORDS[ROUTE_COORDS.length - 1], segIndex: ROUTE_COORDS.length - 2 }};

            const targetDist = t * totalDistance;
            let accumulated = 0;
            for (let i = 0; i < segmentDistances.length; i++) {{
                const nextAcc = accumulated + segmentDistances[i];
                if (targetDist <= nextAcc) {{
                    const segT = (targetDist - accumulated) / segmentDistances[i];
                    const p1 = ROUTE_COORDS[i];
                    const p2 = ROUTE_COORDS[i + 1];
                    const lat = p1[0] + (p2[0] - p1[0]) * segT;
                    const lng = p1[1] + (p2[1] - p1[1]) * segT;
                    return {{ latLng: [lat, lng], segIndex: i }};
                }}
                accumulated = nextAcc;
            }}
            return {{ latLng: ROUTE_COORDS[ROUTE_COORDS.length - 1], segIndex: ROUTE_COORDS.length - 2 }};
        }}

        // Car icon with glowing pulsating radar ring
        function createCarIcon() {{
            return L.divIcon({{
                className: 'custom-leaflet-marker',
                html: `
                    <div style="position: relative; width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; pointer-events: none;">
                        <div class="car-pulse-ring"></div>
                        <div style="
                            position: relative;
                            width: 36px;
                            height: 36px;
                            border-radius: 50%;
                            background: #0f172a;
                            border: 2.5px solid #FF8A00;
                            box-shadow: 0 4px 16px rgba(255, 138, 0, 0.6);
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            font-size: 19px;
                        ">
                            🚗
                        </div>
                    </div>
                `,
                iconSize: [48, 48],
                iconAnchor: [24, 24],
            }});
        }}

        // Start Point icon (JPS Training)
        function createStartIcon() {{
            return L.divIcon({{
                className: 'custom-leaflet-marker',
                html: `
                    <div style="display: flex; flex-direction: column; align-items: center; pointer-events: auto;">
                        <div style="
                            background: #111118;
                            border: 1.5px solid #FF8A00;
                            border-radius: 8px;
                            padding: 3px 8px;
                            font-family: Montserrat, sans-serif;
                            font-size: 10px;
                            font-weight: 800;
                            color: #FF8A00;
                            white-space: nowrap;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.7);
                            display: flex;
                            align-items: center;
                            gap: 4px;
                        ">
                            <span>🏋️‍♂️</span>
                            <span>JPS TRAINING (SALIDA)</span>
                        </div>
                        <div style="width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 5px solid #FF8A00;"></div>
                    </div>
                `,
                iconSize: [140, 32],
                iconAnchor: [70, 32],
            }});
        }}

        // Street Entrance waypoint marker (la entrada sobre la calle)
        function createEntranceIcon() {{
            return L.divIcon({{
                className: 'custom-leaflet-marker',
                html: `
                    <div style="display: flex; flex-direction: column; align-items: center; pointer-events: auto; opacity: 0.85;">
                        <div style="
                            background: rgba(17,17,24,0.9);
                            border: 1px solid rgba(255,255,255,0.25);
                            border-radius: 6px;
                            padding: 2px 6px;
                            font-family: 'JetBrains Mono', monospace;
                            font-size: 9px;
                            font-weight: 700;
                            color: #e5e2e1;
                            white-space: nowrap;
                        ">
                            <span>Entrada Calle</span>
                        </div>
                        <div style="width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 4px solid rgba(255,255,255,0.4);"></div>
                    </div>
                `,
                iconSize: [100, 24],
                iconAnchor: [50, 24],
            }});
        }}

        // Modena Eventos Arrival Marker (Exact spot inside Modena)
        function createModenaIcon(isArrived) {{
            if (!isArrived) {{
                return L.divIcon({{
                    className: 'custom-leaflet-marker',
                    html: '<div style="display: none;"></div>',
                    iconSize: [0, 0],
                    iconAnchor: [0, 0],
                }});
            }}

            return L.divIcon({{
                className: 'custom-leaflet-marker',
                html: `
                    <div style="position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; width: 220px; height: 180px; pointer-events: auto; overflow: visible;">
                        
                        <!-- Pop-up Modena Eventos Card -->
                        <div class="store-card-pop-anim" style="
                            position: absolute;
                            bottom: 56px;
                            left: 50%;
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                            filter: drop-shadow(0 8px 22px rgba(0,0,0,0.9));
                        ">
                            <!-- Card Box -->
                            <div style="
                                background: #0e0e14;
                                border: 2.5px solid #FF8A00;
                                border-radius: 14px;
                                padding: 8px 14px 9px 14px;
                                text-align: center;
                                white-space: nowrap;
                                box-shadow: 0 0 25px rgba(255, 138, 0, 0.45);
                            ">
                                <div style="display: flex; align-items: center; justify-content: center; gap: 5px; margin-bottom: 2px;">
                                    <span style="font-size: 13px;">📍</span>
                                    <span style="color: #FF8A00; font-size: 12px; font-weight: 900; letter-spacing: 0.8px; font-family: Montserrat, sans-serif;">MÓDENA EVENTOS</span>
                                </div>
                                <div style="color: #ffffff; font-size: 11px; font-weight: 800; font-family: Montserrat, sans-serif;">SEDE HYBRID GAME JPS</div>
                                <div style="color: #F5C518; font-size: 10px; font-weight: 700; font-family: 'JetBrains Mono', monospace; margin-top: 2px;">Tacuarembó • 21 de Noviembre</div>
                            </div>

                            <!-- Downward Pointer Arrow -->
                            <div style="
                                width: 0;
                                height: 0;
                                border-left: 7px solid transparent;
                                border-right: 7px solid transparent;
                                border-top: 7px solid #FF8A00;
                                margin-top: -1px;
                            "></div>
                        </div>

                        <!-- Drop Pin Style Google Maps -->
                        <div class="pin-drop-anim" style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); display: flex; flex-direction: column; align-items: center;">
                            <div style="
                                position: absolute;
                                bottom: -3px;
                                left: 50%;
                                transform: translateX(-50%);
                                width: 18px;
                                height: 6px;
                                background: rgba(0,0,0,0.4);
                                border-radius: 50%;
                                filter: blur(1px);
                            "></div>

                            <svg width="36" height="48" viewBox="0 0 34 46" fill="none" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));">
                                <path d="M17 0C7.61 0 0 7.61 0 17C0 29.75 17 46 17 46C17 46 34 29.75 34 17C34 7.61 26.39 0 17 0Z" fill="#EA4335"/>
                                <path d="M17 1C8.16 1 1 8.16 1 17C1 29.2 16.5 44.5 17 45C17.5 44.5 33 29.2 33 17C33 8.16 25.84 1 17 1Z" stroke="#C5221F" stroke-width="1.5"/>
                                <circle cx="17" cy="17" r="7" fill="white"/>
                            </svg>
                        </div>

                    </div>
                `,
                iconSize: [220, 180],
                iconAnchor: [110, 180],
            }});
        }}

        function initLiveMap() {{
            const mapContainer = document.getElementById('live-route-map');
            if (!mapContainer) return;

            const map = L.map(mapContainer, {{
                center: [-31.726, -56.002],
                zoom: 13,
                zoomControl: false,
                attributionControl: false,
                scrollWheelZoom: false,
                dragging: true,
                touchZoom: true,
            }});

            // OpenStreetMap tile layer (dark styled)
            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
            }}).addTo(map);

            L.control.zoom({{ position: 'bottomright' }}).addTo(map);

            const bounds = L.latLngBounds(ROUTE_COORDS);
            map.fitBounds(bounds, {{ padding: [50, 50] }});

            // Start marker at JPS Training
            L.marker(START_COORDS, {{
                icon: createStartIcon(),
                zIndexOffset: 800,
            }}).addTo(map);

            // Street entrance helper marker (sobre la calle donde gira hacia el predio)
            L.marker([-31.735504, -56.018274], {{
                icon: createEntranceIcon(),
                zIndexOffset: 700,
            }}).addTo(map);

            // Outer glowing polyline (electric orange)
            const routeGlow = L.polyline([], {{
                color: '#FF8A00',
                weight: 8,
                opacity: 0.45,
                lineCap: 'round',
                lineJoin: 'round',
            }}).addTo(map);

            // Inner crisp polyline (golden yellow)
            const routeMain = L.polyline([], {{
                color: '#F5C518',
                weight: 4,
                opacity: 0.95,
                lineCap: 'round',
                lineJoin: 'round',
            }}).addTo(map);

            // Car marker
            const carMarker = L.marker(ROUTE_COORDS[0], {{
                icon: createCarIcon(),
                zIndexOffset: 1200,
                opacity: 0,
            }}).addTo(map);

            // Modena Destination marker (exact point)
            const modenaMarker = L.marker(STORE_COORDS, {{
                icon: createModenaIcon(false),
                zIndexOffset: 2000,
            }}).addTo(map);

            // On click anywhere on map, open Google Maps link
            const openMaps = () => {{
                window.open(GOOGLE_MAPS_URL, '_blank', 'noopener,noreferrer');
            }};
            map.on('click', openMaps);
            carMarker.on('click', openMaps);
            modenaMarker.on('click', openMaps);

            // Continuous Animation Loop (11.5s per cycle)
            const CYCLE_DURATION = 11500;
            let startTime = null;
            let storeShown = false;

            function animate(timestamp) {{
                if (!startTime) startTime = timestamp;
                const elapsed = (timestamp - startTime) % CYCLE_DURATION;
                const cycleSec = elapsed / 1000;

                // FASE 1: Trazo dibujándose desde JPS por la calle e ingresando a Módena (0s a 3.2s)
                if (cycleSec < 3.2) {{
                    if (storeShown) {{
                        modenaMarker.setIcon(createModenaIcon(false));
                        storeShown = false;
                    }}
                    const drawProgress = Math.min(1, cycleSec / 3.2);
                    const {{ latLng, segIndex }} = getPointAt(drawProgress);
                    const drawnPath = [...ROUTE_COORDS.slice(0, segIndex + 1), latLng];

                    routeGlow.setLatLngs(drawnPath);
                    routeMain.setLatLngs(drawnPath);
                    carMarker.setOpacity(0);
                }}
                // FASE 2: El auto recorre la ruta, dobla en la entrada y entra a Módena; el camino detrás SE BORRA (3.2s a 8.2s)
                else if (cycleSec < 8.2) {{
                    if (storeShown) {{
                        modenaMarker.setIcon(createModenaIcon(false));
                        storeShown = false;
                    }}
                    const rideProgress = Math.min(1, (cycleSec - 3.2) / 5.0);
                    const {{ latLng, segIndex }} = getPointAt(rideProgress);

                    carMarker.setLatLng(latLng);
                    carMarker.setOpacity(1);

                    const remainingPath = [latLng, ...ROUTE_COORDS.slice(segIndex + 1)];
                    routeGlow.setLatLngs(remainingPath);
                    routeMain.setLatLngs(remainingPath);
                }}
                // FASE 3: Llegada exacta al predio de Módena Eventos + Pin drop + Cartel pop (8.2s a 10.5s)
                else if (cycleSec < 10.5) {{
                    routeGlow.setLatLngs([]);
                    routeMain.setLatLngs([]);

                    carMarker.setLatLng(STORE_COORDS);
                    carMarker.setOpacity(1);

                    if (!storeShown) {{
                        modenaMarker.setIcon(createModenaIcon(true));
                        storeShown = true;
                    }}
                }}
                // FASE 4: Fade out suave y reinicio (10.5s a 11.5s)
                else {{
                    const fadeProgress = (cycleSec - 10.5) / 1.0;
                    const opacity = Math.max(0, 1 - fadeProgress);

                    carMarker.setOpacity(opacity);
                    routeGlow.setLatLngs([]);
                    routeMain.setLatLngs([]);
                }}

                requestAnimationFrame(animate);
            }}

            requestAnimationFrame(animate);

            setTimeout(() => {{
                map.invalidateSize();
            }}, 300);
        }}

        // ══════════════════════════════════════════════
        // 4. LIGHTBOX HANDLER
        // ══════════════════════════════════════════════
        function openLightbox(src, caption) {{
            const modal = document.getElementById('lightbox-modal');
            const img = document.getElementById('lightbox-img');
            const cap = document.getElementById('lightbox-caption');
            img.src = src;
            cap.textContent = caption || '';
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }}

        function closeLightbox() {{
            const modal = document.getElementById('lightbox-modal');
            modal.classList.add('hidden');
            document.body.style.overflow = 'auto';
        }}

        // Close on ESC
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeLightbox();
        }});

        // ══════════════════════════════════════════════
        // INITIALIZATION
        // ══════════════════════════════════════════════
        document.addEventListener('DOMContentLoaded', () => {{
            initCountdown();
            setupFilters();
            renderSchedule();
            initLiveMap();
        }});
    </script>

</body>
</html>
'''

# Write to evento.html
with open('evento.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('Successfully generated evento.html with exact Modena coordinates!')

# Also copy to hybrid-game.html
shutil.copy2('evento.html', 'hybrid-game.html')
print('Successfully copied to hybrid-game.html!')

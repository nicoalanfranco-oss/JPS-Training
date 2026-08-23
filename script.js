document.addEventListener('DOMContentLoaded', () => {
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
                renderDynamicSchedules();
            }
            if (preciosRes.ok) {
                const precios = await preciosRes.json();
                renderDynamicPrices(precios || []);
            }
        } catch (error) {
            console.error('Error cargando datos de la web:', error);
        }
    }

    // --- Render schedule as a grid ---
    function renderDynamicSchedules() {
        const container = document.getElementById('horarios-grid-container');
        if (!container) return;

        const horarios = window.allHorarios || [];
        const filter = window.currentFilter || 'all';

        const filtered = filter === 'all'
            ? horarios
            : horarios.filter(h => h.nombre_actividad &&
                h.nombre_actividad.toLowerCase().includes(filter.toLowerCase()));

        if (filtered.length === 0) {
            container.innerHTML = '<div class="col-span-6 p-8 text-center text-on-surface-variant">No hay horarios disponibles.</div>';
            return;
        }

        const diasMostrados = [1, 2, 3, 4, 5]; // Lunes a Viernes
        const nombreDias = ['DOMINGO', 'LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO'];

        // Get unique times and sort them
        const times = [...new Set(filtered.map(h => (h.hora || '').substring(0, 5)))].filter(Boolean).sort();

        const actColors = {
            'hybrid': 'from-[#FF8A00] to-[#E01E5A] text-white',
            'functional': 'from-slate-700 to-slate-900 text-white',
            'pilates': 'from-[#FF8A00] to-[#FF6000] text-black',
            'gap': 'from-yellow-500 to-yellow-600 text-black',
            '60': 'from-yellow-400 to-amber-500 text-black',
        };

        function getGradient(name) {
            const lower = name.toLowerCase();
            if (lower.includes('hybrid')) return actColors['hybrid'];
            if (lower.includes('functional')) return actColors['functional'];
            if (lower.includes('pilates')) return actColors['pilates'];
            if (lower.includes('gap')) return actColors['gap'];
            if (lower.includes('60')) return actColors['60'];
            return 'from-[#FF8A00] to-[#E01E5A] text-white';
        }

        // Build header
        let html = `<div></div>`; // Empty top-left cell
        diasMostrados.forEach(diaNum => {
            html += `<div class="bg-surface-elevated text-electric-orange font-label-caps text-sm py-4 rounded-xl shadow-lg border border-white/5 tracking-widest flex items-center justify-center">${nombreDias[diaNum]}</div>`;
        });

        // Build rows
        times.forEach(time => {
            // Time column
            html += `<div class="flex items-center justify-center font-display-xl text-lg text-electric-orange font-bold pr-4">${time}</div>`;
            
            // Days columns
            diasMostrados.forEach(diaNum => {
                // Find class for this day and time
                const clase = filtered.find(h => Number(h.dia_semana) === diaNum && (h.hora || '').startsWith(time));
                
                if (clase) {
                    const act = clase.nombre_actividad || '';
                    const colorClass = getGradient(act);
                    html += `<div class="bg-gradient-to-r ${colorClass} rounded-xl shadow-lg py-4 px-2 font-label-caps text-xs font-bold uppercase tracking-widest flex items-center justify-center min-h-[60px] cursor-pointer hover:scale-105 transition-transform" onclick="document.getElementById('contacto').scrollIntoView({behavior:'smooth'})">${act}</div>`;
                } else {
                    // Empty cell
                    html += `<div></div>`;
                }
            });
        });

        container.innerHTML = html;
    }

    // --- Setup Filters ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterBtns.forEach(b => {
                b.classList.remove('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'border-[#FF8A00]', 'text-white');
                b.classList.add('border-white/20', 'text-on-surface');
            });
            e.currentTarget.classList.remove('border-white/20', 'text-on-surface');
            e.currentTarget.classList.add('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'border-[#FF8A00]', 'text-white');

            window.currentFilter = e.currentTarget.getAttribute('data-filter');
            renderDynamicSchedules();
        });
    });

    // --- Dynamic Pricing Rotation ---
    function renderDynamicPrices(precios) {
        const cards = document.querySelectorAll('.plan-card');
        if (!cards.length) return;

        // Map plan names to card indices by keywords
        const planMap = [
            { keywords: ['2 vec', '2vec', 'basico', 'básico', '1.650'], index: 0 },
            { keywords: ['3 vec', '3vec', 'popular', '1.900'], index: 1 },
            { keywords: ['ilimitado', 'elite', 'élite', '2.100'], index: 2 },
        ];

        if (precios && precios.length > 0) {
            precios.forEach(plan => {
                const modalidad = (plan.modalidad || '').toLowerCase();
                const precio = Math.round(plan.ultimo_precio || 0);

                let targetIdx = -1;
                for (const pm of planMap) {
                    if (pm.keywords.some(k => modalidad.includes(k))) {
                        targetIdx = pm.index;
                        break;
                    }
                }
                if (targetIdx === -1) {
                    const usedIndexes = planMap.map(p => p.index);
                    targetIdx = usedIndexes[precios.indexOf(plan)] ?? -1;
                }

                if (targetIdx >= 0 && cards[targetIdx]) {
                    const titleEl = cards[targetIdx].querySelector('.plan-title');
                    const priceEl = cards[targetIdx].querySelector('.plan-price');
                    if (titleEl) titleEl.textContent = plan.modalidad.toUpperCase();
                    if (priceEl) priceEl.textContent = `$${precio.toLocaleString('es-UY')}`;
                }
            });
        }

        let activeIdx = 1; // Start highlighting middle card

        function updateHighlight(index) {
            cards.forEach((card, idx) => {
                const badge = card.querySelector('.plan-badge');
                const btn = card.querySelector('.plan-btn');

                if (idx === index) {
                    card.style.transform = 'translateY(-20px) scale(1.04)';
                    card.style.borderColor = '#FF8A00';
                    card.style.boxShadow = '0 0 50px rgba(255, 138, 0, 0.4)';
                    card.style.zIndex = '20';
                    if (badge) badge.classList.remove('hidden');
                    if (btn) {
                        btn.className = 'plan-btn w-full py-4 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white font-bold text-xs uppercase tracking-widest rounded transition-all duration-300 relative z-10';
                    }
                } else {
                    card.style.transform = 'translateY(0px) scale(1)';
                    card.style.borderColor = '';
                    card.style.boxShadow = '';
                    card.style.zIndex = '1';
                    if (badge) badge.classList.add('hidden');
                    if (btn) {
                        btn.className = 'plan-btn w-full py-3 border border-white/30 text-on-surface font-label-caps text-label-caps uppercase rounded hover:bg-surface-bright transition-colors';
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

    // Staff modal styles
    const style = document.createElement('style');
    style.textContent = `
        .staff-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(15px);
            z-index: 9999;
            opacity: 0;
            transition: opacity 0.5s ease;
        }
        .staff-modal.show {
            display: block;
            opacity: 1;
        }
        .staff-modal-content {
            width: 90%;
            height: 85%;
            max-width: 1200px;
            margin: 5vh auto;
            position: relative;
            border-radius: 24px;
            overflow: hidden;
            border: 1px solid rgba(255, 138, 0, 0.2);
            box-shadow: 0 0 80px rgba(0, 0, 0, 0.8);
            transform: scale(0.95);
            transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .staff-modal.show .staff-modal-content {
            transform: scale(1);
        }
        .modal-bg {
            position: absolute;
            inset: 0;
            background-size: cover;
            background-position: center top;
            filter: brightness(0.75);
            transform: scale(1.02);
            transition: transform 8s ease-out, filter 1.5s ease;
            z-index: 0;
        }
        .staff-modal.show .modal-bg {
            transform: scale(1);
            filter: brightness(0.6);
        }
        .close-btn {
            position: absolute; top: 25px; right: 30px;
            font-size: 40px; cursor: pointer; color: white;
            opacity: 0.7; transition: all 0.3s ease;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        .close-btn:hover {
            opacity: 1; color: #FF8A00; transform: scale(1.1);
        }
        .typewriter-text {
            visibility: hidden;
        }
        .typewriter-text::after {
            content: '|';
            animation: blink 1s step-end infinite;
            color: #FF8A00;
        }
        .typewriter-text.typing {
            visibility: visible;
        }
        .typewriter-text.done::after {
            display: none;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        .fade-in-block {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }
        .fade-in-block.visible {
            opacity: 1;
            transform: translateY(0);
        }
    `;
    document.head.appendChild(style);

    function typeWriter(element, text, speed = 30) {
        element.innerHTML = '';
        element.classList.remove('done');
        element.classList.add('typing');
        let i = 0;
        return new Promise(resolve => {
            function type() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                } else {
                    element.classList.add('done');
                    resolve();
                }
            }
            type();
        });
    }

    function setupModal(triggerId, modalId) {
        const trigger = document.getElementById(triggerId);
        const modal = document.getElementById(modalId);
        if (!trigger || !modal) return;

        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            modal.style.display = 'block';
            void modal.offsetWidth;
            modal.classList.add('show');

            // Reset typewriter elements
            const typewriterEls = modal.querySelectorAll('.typewriter-text');
            typewriterEls.forEach(el => {
                el.innerHTML = '';
                el.classList.remove('typing', 'done');
                el.style.visibility = 'hidden';
            });

            // Reset fade-in blocks
            const fadeBlocks = modal.querySelectorAll('.fade-in-block');
            fadeBlocks.forEach(el => el.classList.remove('visible'));

            // Run typewriter effects sequentially
            let chainDelay = 0;
            typewriterEls.forEach(el => {
                const text = el.getAttribute('data-text');
                const baseDelay = parseInt(el.getAttribute('data-delay') || '0');
                const startDelay = Math.max(chainDelay, baseDelay);
                setTimeout(() => {
                    el.style.visibility = 'visible';
                    typeWriter(el, text, 30).then(() => {});
                }, startDelay);
                const typingTime = (text ? text.length * 35 : 0);
                chainDelay = startDelay + typingTime + 200;
            });

            // Fade-in blocks appear after all typewriting
            fadeBlocks.forEach((el, i) => {
                setTimeout(() => {
                    el.classList.add('visible');
                }, chainDelay + i * 200);
            });
        });

        modal.addEventListener('click', (e) => {
            if (e.target === modal || e.target.classList.contains('close-btn')) {
                modal.classList.remove('show');
                setTimeout(() => {
                    modal.style.display = 'none';
                }, 500); // match transition time
            }
        });
    }

    setupModal('card-noelia', 'modal-noelia');
    setupModal('card-santiago', 'modal-santiago');
    setupModal('card-juanpablo', 'modal-juanpablo');
    
    // Actividades Modals
    setupModal('card-act-hybrid', 'modal-act-hybrid');
    setupModal('card-act-functional', 'modal-act-functional');
    setupModal('card-act-gap', 'modal-act-gap');
    setupModal('card-act-pilates', 'modal-act-pilates');
    setupModal('card-act-60', 'modal-act-60');
    setupModal('card-act-openbox', 'modal-act-openbox');
});

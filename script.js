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

    // --- Render schedule as table rows (matches c335a21 structure) ---
    function renderDynamicSchedules() {
        const container = document.getElementById('horarios-dynamic-container');
        if (!container) return;

        const horarios = window.allHorarios || [];
        const filter = window.currentFilter || 'all';

        const filtered = filter === 'all'
            ? horarios
            : horarios.filter(h => h.nombre_actividad &&
                h.nombre_actividad.toLowerCase().includes(filter.toLowerCase()));

        if (filtered.length === 0) {
            container.innerHTML = '<tr><td colspan="4" class="p-8 text-center text-on-surface-variant">No hay horarios disponibles para esta modalidad.</td></tr>';
            return;
        }

        const diasNombre = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];

        // Sort by day then time
        const sorted = [...filtered].sort((a, b) => {
            const dayDiff = Number(a.dia_semana) - Number(b.dia_semana);
            if (dayDiff !== 0) return dayDiff;
            return (a.hora || '').localeCompare(b.hora || '');
        });

        const actColors = {
            'hybrid': 'from-[#FF8A00] to-[#E01E5A]',
            'functional': 'from-slate-700 to-slate-900',
            'pilates': 'from-[#FF8A00] to-[#FF6000]',
            'gap': 'from-yellow-500 to-yellow-600',
            '60': 'from-yellow-400 to-amber-500',
        };

        function getGradient(name) {
            const lower = name.toLowerCase();
            if (lower.includes('hybrid')) return actColors['hybrid'];
            if (lower.includes('functional')) return actColors['functional'];
            if (lower.includes('pilates')) return actColors['pilates'];
            if (lower.includes('gap')) return actColors['gap'];
            if (lower.includes('60')) return actColors['60'];
            return 'from-[#FF8A00] to-[#E01E5A]';
        }

        const rows = sorted.map(h => {
            const dia = diasNombre[Number(h.dia_semana)] || h.nombre_dia || '';
            const hora = (h.hora || '').substring(0, 5);
            const dur = h.duracion_minutos ? `${h.duracion_minutos}min` : '';
            const act = h.nombre_actividad || '';
            const grad = getGradient(act);

            return `<tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                <td class="p-4 text-sm text-on-surface">
                    <span class="font-bold text-electric-orange">${hora}</span>
                    ${dur ? `<span class="text-on-surface-variant ml-2 text-xs">${dur}</span>` : ''}
                    <div class="text-xs text-on-surface-variant mt-0.5">${dia}</div>
                </td>
                <td class="p-4">
                    <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold text-white bg-gradient-to-r ${grad} uppercase tracking-wide">
                        ${act}
                    </span>
                </td>
                <td class="p-4 hidden md:table-cell">
                    <span class="inline-flex items-center gap-1.5 text-xs font-medium text-green-400">
                        <span class="w-1.5 h-1.5 rounded-full bg-green-400 inline-block"></span>
                        Activo
                    </span>
                </td>
                <td class="p-4 text-right">
                    <button onclick="document.getElementById('contacto').scrollIntoView({behavior:'smooth'})"
                        class="text-xs font-bold text-electric-orange hover:text-vibrant-pink transition-colors uppercase tracking-wider">
                        Reservar →
                    </button>
                </td>
            </tr>`;
        }).join('');

        container.innerHTML = rows;
    }

    // --- Setup Filters ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterBtns.forEach(b => {
                b.classList.remove('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'border-[#FF8A00]');
                b.classList.add('border-white/10');
            });
            e.currentTarget.classList.remove('border-white/10');
            e.currentTarget.classList.add('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'border-[#FF8A00]');

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
                // Fallback: assign by order
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
                    card.style.transform = idx === 1 ? 'translateY(-16px) scale(1)' : 'translateY(0px) scale(1)';
                    card.style.borderColor = '';
                    card.style.boxShadow = '';
                    card.style.zIndex = idx === 1 ? '10' : '1';
                    if (badge) badge.classList.add('hidden');
                    if (btn) {
                        const isMid = idx === 1;
                        btn.className = isMid
                            ? 'plan-btn w-full py-4 text-white font-label-caps text-label-caps uppercase rounded btn-gradient hover:glow-effect transition-all relative z-10'
                            : 'plan-btn w-full py-3 border border-white/30 text-on-surface font-label-caps text-label-caps uppercase rounded hover:bg-surface-bright transition-colors';
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

    // --- Setup Staff Modals ---
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

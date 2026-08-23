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
            html += `<div class="bg-surface-elevated rounded-xl border border-brushed-metal py-4 px-2 font-headline-md text-electric-orange top-light shadow-md">${d.name}</div>`;
        });

        // 2. Slots Rows
        times.forEach(timeStr => {
            // Time Column
            html += `<div class="flex items-center justify-end pr-4 font-headline-md text-electric-orange">${timeStr}</div>`;

            // Day Columns 1 to 5
            days.forEach(day => {
                const match = horarios.find(h => Number(h.dia_semana) === day.num && h.hora.substring(0, 5) === timeStr);

                if (match) {
                    const actName = match.nombre_actividad;
                    let styleClass = 'bg-gradient-to-r from-electric-orange to-vibrant-pink text-white font-label-caps';
                    let actDisplay = actName.toUpperCase();

                    if (actName.toLowerCase().includes('functional strength')) {
                        styleClass = 'bg-slate-800 text-white font-label-caps';
                        actDisplay = '<span>FUNCTIONAL</span><span>STRENGTH</span>';
                    } else if (actName.toLowerCase().includes('pilates')) {
                        styleClass = 'bg-electric-orange text-surface-container-lowest font-label-caps';
                        actDisplay = '<span>PILATES</span><span>FUNCIONAL</span>';
                    } else if (actName.toLowerCase().includes('gap')) {
                        styleClass = 'bg-vibrant-yellow text-surface-container-lowest font-label-caps';
                        actDisplay = 'GAP';
                    } else if (actName.toLowerCase().includes('60')) {
                        styleClass = 'bg-vibrant-yellow text-surface-container-lowest font-label-caps';
                        actDisplay = '+ 60';
                    }

                    html += `
                    <div data-activity="${actName}" class="slot-pill ${styleClass} rounded-xl py-3 px-2 flex flex-col items-center justify-center leading-tight shadow-lg transition-all duration-300">
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

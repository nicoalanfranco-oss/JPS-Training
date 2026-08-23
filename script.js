document.addEventListener('DOMContentLoaded', () => {
    // --- API Data Load (direct from PostgreSQL via studio-main) ---
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

    function renderDynamicSchedules() {
        const container = document.getElementById('horarios-dynamic-container');
        if (!container) return;
        const horarios = window.allHorarios || [];
        const filter = window.currentFilter || 'all';
        const filteredHorarios = filter === 'all'
            ? horarios
            : horarios.filter(h => h.nombre_actividad && h.nombre_actividad.toLowerCase().includes(filter.toLowerCase()));
        if (filteredHorarios.length === 0) {
            container.innerHTML = '<tr><td colspan="4" class="p-8 text-center text-on-surface-variant">No hay horarios disponibles para esta modalidad.</td></tr>';
            return;
        }
        const diasSemana = [
            { num: 1, long: 'Lunes' },
            { num: 2, long: 'Martes' },
            { num: 3, long: 'Miércoles' },
            { num: 4, long: 'Jueves' },
            { num: 5, long: 'Viernes' },
            { num: 6, long: 'Sábado' },
            { num: 7, long: 'Domingo' },
        ];
        let html = '';
        diasSemana.forEach(dia => {
            const horariosDia = filteredHorarios.filter(h => Number(h.dia_semana) === dia.num);
            if (horariosDia.length === 0) return;
            html += `<tr class="bg-surface-elevated/50"><td colspan="4" class="p-4 font-bold text-[#ffb599] border-t border-white/5 bg-white/5">${dia.long}</td></tr>`;
            horariosDia.sort((a, b) => a.hora.localeCompare(b.hora)).forEach(h => {
                html += `
                <tr class="group hover:bg-white/5 transition-colors duration-200">
                    <td class="p-4 py-5 whitespace-nowrap">
                        <div class="flex items-center gap-3">
                            <span class="font-display-xl font-bold text-xl text-on-surface">${h.hora.substring(0, 5)}</span>
                            <span class="text-xs text-on-surface-variant bg-surface px-2 py-1 rounded">${h.duracion_min}m</span>
                        </div>
                    </td>
                    <td class="p-4 py-5">
                        <div class="font-bold text-on-surface mb-1">${h.nombre_actividad}</div>
                    </td>
                    <td class="p-4 py-5 hidden md:table-cell">
                        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                            Activo
                        </span>
                    </td>
                    <td class="p-4 py-5 text-right">
                        <a href="#contacto" class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-surface-elevated border border-white/10 text-on-surface hover:bg-[#ffb599] hover:text-[#5a1c00] hover:border-[#ffb599] transition-all duration-300 group-hover:-translate-y-1 group-hover:shadow-lg">
                            <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
                        </a>
                    </td>
                </tr>`;
            });
        });
        container.innerHTML = html;
    }

    function renderDynamicPrices(precios) {
        // En lugar de reemplazar todo el contenedor (que puede estar roto), vamos a buscar los contenedores de las tarjetas existentes en el DOM.
        // Asumimos que JPS tiene 3 tarjetas de planes.
        const planCards = document.querySelectorAll('.plan-card');
        if (planCards.length === 0 || precios.length === 0) return;

        // Ordenamos los precios como vengan de la bd, asumimos 3 planes principales
        const planesParaMostrar = precios.slice(0, 3);
        const etiquetas = ['EMPEZAR BÁSICO', 'ELEGIR PREMIUM', 'EMPEZAR ELITE'];
        const tagsSuperiores = ['BÁSICO', 'MÁS POPULAR', 'PREMIUM'];
        
        planesParaMostrar.forEach((plan, index) => {
            if (index >= planCards.length) return;
            const card = planCards[index];
            
            card.innerHTML = `
                ${index === 1 ? '<div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white px-4 py-1 rounded-full text-xs font-bold tracking-widest z-10">' + tagsSuperiores[index] + '</div>' : ''}
                <div class="mb-8">
                    <p class="text-[#FF8A00] font-label-caps tracking-widest mb-2">${plan.modalidad.toUpperCase()}</p>
                    <div class="flex items-baseline gap-2">
                        <span class="text-4xl font-display-xl font-black text-on-surface">$${Math.round(plan.ultimo_precio).toLocaleString('es-UY')}</span>
                        <span class="text-on-surface-variant font-body-md">/ mes</span>
                    </div>
                </div>
                <div class="flex-grow">
                    <ul class="space-y-4 font-body-md text-on-surface-variant">
                        <li class="flex items-center gap-3">
                            <span class="material-symbols-outlined text-[#FF8A00] text-[20px]">check_circle</span>
                            Válido para todas las modalidades
                        </li>
                    </ul>
                </div>
                <button onclick="document.getElementById('contacto').scrollIntoView({behavior: 'smooth'})" class="w-full mt-8 py-3 rounded-xl font-label-caps border border-white/10 text-on-surface hover:bg-gradient-to-r hover:from-[#FF8A00] hover:to-[#E01E5A] transition-all duration-300">
                    ${etiquetas[index]}
                </button>
            `;
            
            // Añadir estilos iniciales para la animación
            card.style.transition = 'all 0.5s ease';
            if(index === 1) card.classList.add('plan-highlighted');
        });

        // Effect of rotation (highlighting cards automatically)
        let currentIndex = 0;
        setInterval(() => {
            planCards.forEach(card => {
                card.classList.remove('scale-105', 'border-[#FF8A00]', 'shadow-2xl');
                const btn = card.querySelector('button');
                if (btn) btn.classList.remove('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]');
            });
            
            const currentCard = planCards[currentIndex];
            currentCard.classList.add('scale-105', 'border-[#FF8A00]', 'shadow-2xl');
            const currentBtn = currentCard.querySelector('button');
            if (currentBtn) currentBtn.classList.add('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]');

            currentIndex = (currentIndex + 1) % planCards.length;
        }, 3000);
    }

    loadWebData();
    
    // --- Setup Filters ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterBtns.forEach(b => {
                b.classList.remove('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'text-white', 'border-[#FF8A00]');
                b.classList.add('border-white/10', 'text-on-surface');
            });
            e.currentTarget.classList.remove('border-white/10', 'text-on-surface');
            e.currentTarget.classList.add('bg-gradient-to-r', 'from-[#FF8A00]', 'to-[#E01E5A]', 'text-white', 'border-[#FF8A00]');
            
            window.currentFilter = e.currentTarget.getAttribute('data-filter');
            renderDynamicSchedules();
        });
    });

    // --- Setup Modals for Staff ---
    function setupModal(triggerId, modalId) {
        const trigger = document.getElementById(triggerId);
        const modal = document.getElementById(modalId);
        if (!trigger || !modal) return;

        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.add('active');
            modal.style.display = 'block';
        });

        modal.addEventListener('click', (e) => {
            if (e.target === modal || e.target.classList.contains('close-btn')) {
                modal.classList.remove('active');
                modal.style.display = 'none';
            }
        });
    }

    // Add CSS for modals dynamically
    const style = document.createElement('style');
    style.textContent = `
        .staff-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(8px);
            z-index: 9999;
        }
        .staff-modal-content {
            background: #2a2a2a;
            color: #fff;
            padding: 2rem;
            border-radius: 8px;
            max-width: 500px;
            margin: 10% auto;
            position: relative;
        }
        .close-btn {
            position: absolute; top: 10px; right: 20px;
            font-size: 24px; cursor: pointer; color: #ffb599;
        }
    `;
    document.head.appendChild(style);

    // After DOM parsing, bind the modals (assuming JPS HTML uses card-noelia, card-santiago, card-juanpablo)
    setupModal('card-noelia', 'modal-noelia');
    setupModal('card-santiago', 'modal-santiago');
    setupModal('card-juanpablo', 'modal-juanpablo');
});

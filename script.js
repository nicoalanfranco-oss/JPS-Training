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
            'hybrid': 'bg-[#E01E5A] text-white',
            'functional': 'bg-slate-800 border-2 border-[#FF8A00] text-white',
            'pilates': 'bg-[#FFAA44] text-black',
            'gap': 'bg-[#0098FC] text-white',
            '60': 'bg-[#FFD700] text-black',
        };

        function getGradient(name) {
            const lower = name.toLowerCase();
            if (lower.includes('hybrid')) return actColors['hybrid'];
            if (lower.includes('functional')) return actColors['functional'];
            if (lower.includes('pilates')) return actColors['pilates'];
            if (lower.includes('gap')) return actColors['gap'];
            if (lower.includes('60')) return actColors['60'];
            return 'bg-gradient-to-r from-[#FF8A00] to-[#E01E5A] text-white';
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
                    html += `<div class="${colorClass} rounded-xl shadow-lg py-4 px-2 font-label-caps text-xs font-bold uppercase tracking-widest flex items-center justify-center min-h-[60px] cursor-pointer hover:scale-105 transition-transform" onclick="document.getElementById('contacto').scrollIntoView({behavior:'smooth'})">${act}</div>`;
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
            filter: none;
            transform: scale(1.01);
            transition: transform 8s ease-out;
            z-index: 0;
        }
        .staff-modal.show .modal-bg {
            transform: scale(1);
            filter: none;
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
        @keyframes posterBreathing {
            0%, 100% { transform: scale(1); filter: brightness(1) drop-shadow(0 0 15px rgba(255,138,0,0.3)); }
            50% { transform: scale(1.025); filter: brightness(1.08) drop-shadow(0 0 35px rgba(255,138,0,0.65)); }
        }
        .poster-pulse {
            animation: posterBreathing 5s ease-in-out infinite;
        }
        @keyframes liveAuraPulse {
            0%, 100% {
                box-shadow: 0 0 25px rgba(255, 138, 0, 0.4), 0 0 50px rgba(224, 30, 90, 0.35), inset 0 0 20px rgba(255, 138, 0, 0.15);
                border-color: rgba(255, 138, 0, 0.8);
            }
            50% {
                box-shadow: 0 0 65px rgba(255, 138, 0, 0.85), 0 0 100px rgba(224, 30, 90, 0.7), inset 0 0 35px rgba(255, 138, 0, 0.4);
                border-color: rgba(224, 30, 90, 1);
            }
        }
        .live-event-aura {
            animation: liveAuraPulse 2.2s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        }
        /* iPhone & iOS Safari Specific Optimizations */
        .staff-modal-content {
            -webkit-overflow-scrolling: touch;
            max-height: 85dvh;
        }
        button, a, input, select {
            touch-action: manipulation;
            -webkit-tap-highlight-color: transparent;
        }
        .poster-pulse, .live-event-aura {
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            -webkit-transform-style: preserve-3d;
            transform-style: preserve-3d;
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

    // Evento Modal
    setupModal('card-evento-trigger', 'modal-evento');

    // Permitir abrir el modal al hacer clic en cualquier parte de la tarjeta del evento
    const eventCardContainer = document.getElementById('event-card-container');
    if (eventCardContainer) {
        eventCardContainer.addEventListener('click', (e) => {
            if (e.target.closest('button') || e.target.closest('a')) return;
            const trigger = document.getElementById('card-evento-trigger');
            if (trigger) trigger.click();
        });
    }

    // --- Modal de Inscripción al Evento con Formulario e Email ---
    const btnAnotarse = document.getElementById('btn-anotarse-evento');
    const btnModalAnotarse = document.getElementById('btn-modal-anotarse-evento');
    const modalInscripcion = document.getElementById('modal-inscripcion-evento');

    function openInscripcionModal(e) {
        if (e) e.preventDefault();
        const modalEvento = document.getElementById('modal-evento');
        if (modalEvento) {
            modalEvento.classList.remove('show');
            setTimeout(() => { modalEvento.style.display = 'none'; }, 300);
        }
        
        if (modalInscripcion) {
            const form = document.getElementById('form-inscripcion-evento');
            if (form) form.reset();
            const header = document.getElementById('evt-form-header');
            const render = document.getElementById('evt-confirmation-render');
            if (header) header.classList.remove('hidden');
            if (form) form.classList.remove('hidden');
            if (render) render.classList.add('hidden');
            
            modalInscripcion.style.display = 'block';
            void modalInscripcion.offsetWidth;
            modalInscripcion.classList.add('show');
        }
    }

    if (btnAnotarse) btnAnotarse.addEventListener('click', openInscripcionModal);
    if (btnModalAnotarse) btnModalAnotarse.addEventListener('click', openInscripcionModal);

    const btnCloseFinal = document.getElementById('evt-btn-close-final');
    if (btnCloseFinal && modalInscripcion) {
        btnCloseFinal.addEventListener('click', () => {
            modalInscripcion.classList.remove('show');
            setTimeout(() => { modalInscripcion.style.display = 'none'; }, 500);
        });
    }

    if (modalInscripcion) {
        modalInscripcion.addEventListener('click', (e) => {
            if (e.target === modalInscripcion || e.target.classList.contains('close-btn')) {
                modalInscripcion.classList.remove('show');
                setTimeout(() => { modalInscripcion.style.display = 'none'; }, 500);
            }
        });
    }

    // Envío del Formulario de Inscripción de Evento
    const evtForm = document.getElementById('form-inscripcion-evento');
    if (evtForm) {
        evtForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const btnSubmit = document.getElementById('evt-btn-submit');
            const originalHTML = btnSubmit.innerHTML;

            const nombre = document.getElementById('evt-input-nombre').value.trim();
            const telefono = document.getElementById('evt-input-telefono').value.trim();
            const email = document.getElementById('evt-input-email').value.trim();
            const personas = document.getElementById('evt-input-personas').value;

            const mensajeCliente = `--------------------------------------------------------
🎉 CONFIRMACIÓN DE INSCRIPCIÓN AL EVENTO
--------------------------------------------------------

¡Hola ${nombre}!

Tu lugar para el Trekking JPS Training 2026 está CONFIRMADO.
Estamos muy entusiasmados de que te sumes a esta experiencia al aire libre.

📍 DETALLES DE TU INSCRIPCIÓN:
• Participante: ${nombre}
• Correo registrado: ${email}
• Teléfono: ${telefono}
• Acompañantes: ${personas}
• Evento: Trekking JPS Training 2026 (Valle Edén)
• Fecha y Hora: Sábado 12 de Septiembre — 13:00 hs
• Punto de Encuentro: Puente Colgante (Valle Edén, Tacuarembó)
• Recorrido: 9 km (Dificultad baja/moderado, apto para familias)
• Cierre: Merienda saludable y charla con San Gonzalez y Rominek en Chacra Los Nogales

🎒 RECOMENDACIONES DE EQUIPAMIENTO:
1. Calzado cómodo con buen agarre (campeonas de running o botas de trekking).
2. Ropa deportiva liviana + abrigo cómodo para el atardecer.
3. Botella de agua personal (mínimo 1.5L) y protector solar.

🖼️ AFICHE Y DETALLES DEL EVENTO:
Puedes visualizar el afiche oficial del evento en:
https://jpstraining.nico-family.com/public/evento.jpeg

--------------------------------------------------------
* Copia automática enviada a la administración de JPS Training (Juan Pablo Sena).
Si tienes dudas o necesitas modificar tu reserva, puedes responder a este correo o escribirnos por WhatsApp al 098 859 708.

¡Nos vemos el 12 de Septiembre!
Equipo JPS Training`;

            const payload = {
                nombre: nombre,
                telefono: telefono,
                email: email,
                destinatario: email,
                to: email,
                cc: 'jpstrainingtacuarembo@gmail.com',
                asunto: `¡Inscripción Confirmada! Trekking JPS Training 2026 - ${nombre}`,
                gimnasioId: GIMNASIO_ID,
                tipo: 'evento_confirmacion_cliente',
                imagenUrl: 'https://jpstraining.nico-family.com/public/evento.jpeg',
                mensaje: mensajeCliente
            };

            try {
                btnSubmit.disabled = true;
                btnSubmit.innerHTML = `<span class="material-symbols-outlined animate-spin text-[18px]">sync</span> PROCESANDO E INSCRIBIENDO...`;

                const response = await fetch(`${API_BASE}/api/web/contacto`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {
                    const confirmedEmail = document.getElementById('evt-confirmed-email');
                    const confirmedName = document.getElementById('evt-confirmed-name');
                    if (confirmedEmail) confirmedEmail.textContent = email;
                    if (confirmedName) confirmedName.textContent = nombre;

                    const waMsg = encodeURIComponent(`Hola JP! Acabo de inscribirme al Trekking JPS 2026. Mi nombre es ${nombre} (${email}).`);
                    const waBtn = document.getElementById('evt-whatsapp-direct');
                    if (waBtn) waBtn.href = `https://api.whatsapp.com/send?phone=59898859708&text=${waMsg}`;

                    const header = document.getElementById('evt-form-header');
                    const render = document.getElementById('evt-confirmation-render');
                    if (header) header.classList.add('hidden');
                    evtForm.classList.add('hidden');
                    if (render) render.classList.remove('hidden');
                } else {
                    const err = await response.json();
                    alert(`Hubo un inconveniente con el envío: ${err.error || 'Intenta nuevamente'}`);
                }
            } catch (err) {
                console.error('Error enviando inscripción al evento:', err);
                alert('No se pudo establecer conexión con el servidor. Reintenta en unos instantes.');
            } finally {
                btnSubmit.disabled = false;
                btnSubmit.innerHTML = originalHTML;
            }
        });
    }

    // --- Sistema de Eventos Especiales Compartibles & Deep Linking ---
    window.shareEvent = function() {
        const shareUrl = window.location.origin + window.location.pathname + '#evento';
        const shareData = {
            title: 'Trekking JPS Training 2026',
            text: '¡Acompáñanos al Trekking JPS Training en Valle Edén el próximo 12 de septiembre! Entrá al enlace para ver los detalles e inscribirte:',
            url: shareUrl
        };

        if (navigator.share) {
            navigator.share(shareData).catch((err) => {
                console.log('Compartir cancelado o no soportado:', err);
            });
        } else {
            navigator.clipboard.writeText(shareUrl).then(() => {
                alert('¡Enlace directo al evento copiado al portapapeles!\n\nLink: ' + shareUrl);
            }).catch(() => {
                alert('Enlace del evento:\n' + shareUrl);
            });
        }
    };

    function checkEventDeepLink() {
        if (window.location.hash === '#evento') {
            const eventSection = document.getElementById('evento');
            const eventCard = document.getElementById('event-card-container');
            if (eventSection) {
                setTimeout(() => {
                    const yOffset = -110;
                    const y = eventSection.getBoundingClientRect().top + window.pageYOffset + yOffset;
                    window.scrollTo({ top: y, behavior: 'smooth' });
                    if (eventCard) {
                        eventCard.classList.add('live-event-aura');
                    }
                }, 250);
            }
        }
    }
    window.addEventListener('hashchange', checkEventDeepLink);
    checkEventDeepLink();

    // --- Sistema de Baja Automática de Eventos Expirados ---
    const EVENT_EXPIRATION_DATE = new Date('2026-09-12T23:59:59'); // Evento Trekking: 12 de septiembre

    function checkEventExpiration() {
        const currentDate = new Date();
        if (currentDate > EVENT_EXPIRATION_DATE) {
            const topBanner = document.getElementById('top-event-banner');
            const eventNavLinks = document.querySelectorAll('a[href="#evento"]');
            const eventSection = document.getElementById('evento');
            const eventModal = document.getElementById('modal-evento');
            const inscripcionModal = document.getElementById('modal-inscripcion-evento');

            if (topBanner) topBanner.style.display = 'none';
            if (eventSection) eventSection.style.display = 'none';
            if (eventModal) eventModal.style.display = 'none';
            if (inscripcionModal) inscripcionModal.style.display = 'none';
            
            eventNavLinks.forEach(link => {
                link.style.display = 'none';
            });
        }
    }
    checkEventExpiration();

    // --- Envío Seguro del Formulario de Contacto ---
    const contactoForm = document.querySelector('#contacto form');
    if (contactoForm) {
        contactoForm.removeAttribute('onsubmit'); // Removemos el alert estático antiguo
        contactoForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const btnSubmit = contactoForm.querySelector('button[type="submit"]');
            const originalText = btnSubmit.textContent;
            
            const nombreInput = contactoForm.querySelector('input[type="text"]');
            const telefonoInput = contactoForm.querySelector('input[type="tel"]');
            const mensajeInput = contactoForm.querySelector('textarea');
            
            const payload = {
                nombre: nombreInput.value.trim(),
                telefono: telefonoInput.value.trim(),
                mensaje: mensajeInput.value.trim(),
                gimnasioId: GIMNASIO_ID
            };
            
            try {
                btnSubmit.disabled = true;
                btnSubmit.textContent = 'Enviando...';
                
                const response = await fetch(`${API_BASE}/api/web/contacto`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                
                if (response.ok) {
                    alert('¡Gracias por comunicarte! Los datos se enviaron y te contactaremos a la brevedad.');
                    contactoForm.reset();
                } else {
                    const errData = await response.json();
                    alert(`Hubo un problema al enviar: ${errData.error || 'Error desconocido'}`);
                }
            } catch (error) {
                console.error('Error submitting form:', error);
                alert('No se pudo establecer conexión con el servidor. Reintenta en unos instantes.');
            } finally {
                btnSubmit.disabled = false;
                btnSubmit.textContent = originalText;
            }
        });
    }
});

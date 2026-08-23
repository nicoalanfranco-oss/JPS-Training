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
                renderDynamicSchedules(horarios || []);
                console.log("Horarios cargados:", horarios);
            }
            if (preciosRes.ok) {
                const precios = await preciosRes.json();
                console.log("Precios cargados:", precios);
            }
        } catch (error) {
            console.error('Error cargando datos de la web:', error);
        }
    }

    function renderDynamicSchedules(horarios) {
        const container = document.getElementById('horarios-dynamic-container');
        if (!container) return;

        if (horarios.length === 0) {
            container.innerHTML = '<tr><td colspan="5" class="p-8 text-center text-on-surface-variant">No hay horarios disponibles.</td></tr>';
            return;
        }

        const diasSemana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];
        let html = '';

        diasSemana.forEach(dia => {
            const horariosDia = horarios.filter(h => h.nombre_dia.substring(0,3) === dia || (dia === 'Mié' && h.nombre_dia.includes('Mi')));
            if (horariosDia.length === 0) return;

            html += `<tr class="bg-surface-elevated/50"><td colspan="5" class="p-4 font-bold text-primary border-t border-white/5 bg-white/5">${dia}</td></tr>`;
            
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
                    <td class="p-4 py-5 hidden sm:table-cell">
                        <div class="flex items-center gap-2">
                            <span class="material-symbols-outlined text-[18px] text-primary">person</span>
                            <span class="text-sm text-on-surface-variant">${h.profesor || 'Sin asignar'}</span>
                        </div>
                    </td>
                    <td class="p-4 py-5 hidden md:table-cell">
                        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                            Activo
                        </span>
                    </td>
                    <td class="p-4 py-5 text-right">
                        <a href="#contacto" class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-surface-elevated border border-white/10 text-on-surface hover:bg-primary hover:text-on-primary hover:border-primary transition-all duration-300 group-hover:-translate-y-1 group-hover:shadow-lg">
                            <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
                        </a>
                    </td>
                </tr>`;
            });
        });

        container.innerHTML = html;
    }

    loadWebData();
    
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

    // Create Modal HTML
    const modalsContainer = document.createElement('div');
    modalsContainer.innerHTML = `
        <div id="modal-noelia" class="staff-modal">
            <div class="staff-modal-content">
                <span class="close-btn">&times;</span>
                <h3 class="text-2xl font-bold mb-4 text-[#ffb599]">Noelia Lima Latorre</h3>
                <p>Licenciada en Educación Física</p>
                <p>5 Años de experiencia</p>
                <p>Especialidad: Entrenamiento GAP</p>
                <ul class="list-disc pl-5 mt-2 text-sm text-gray-300">
                    <li>Iniciación en el arbitraje en natación</li>
                    <li>Instructora de entrenamiento funcional</li>
                    <li>Instructora de musculación</li>
                    <li>Instructora de pilates reformer y mat</li>
                    <li>Resucitación cardiaca básica (DEA)</li>
                </ul>
            </div>
        </div>
        <div id="modal-santiago" class="staff-modal">
            <div class="staff-modal-content">
                <span class="close-btn">&times;</span>
                <h3 class="text-2xl font-bold mb-4 text-[#ffb599]">Santiago Hernández</h3>
                <p>Lic. en Educación Física</p>
                <p>Entrenador Personal y Preparador Físico Deportivo</p>
                <p>3 años de experiencia</p>
                <ul class="list-disc pl-5 mt-2 text-sm text-gray-300">
                    <li>Fuerza y acondicionamiento</li>
                    <li>Fuerza funcional</li>
                    <li>Preparación física</li>
                    <li>Rendimiento deportivo</li>
                    <li>Entrenamiento funcional</li>
                    <li>Entrenamiento para la salud</li>
                </ul>
            </div>
        </div>
        <div id="modal-juanpablo" class="staff-modal">
            <div class="staff-modal-content">
                <span class="close-btn">&times;</span>
                <h3 class="text-2xl font-bold mb-4 text-[#ffb599]">Juan Pablo Sena</h3>
                <p>Licenciado en Educación Física</p>
                <p>Entrenador Personal y Preparador Físico.</p>
                <p>En formación en entrenamiento Híbrido en Academia Hyrox!</p>
                <ul class="list-disc pl-5 mt-2 text-sm text-gray-300">
                    <li>Entrenamiento Funcional</li>
                    <li>Pilates De Hoy. Pilates Funcional</li>
                    <li>Entrenamiento de alta intensidad</li>
                    <li>Metodología cross training</li>
                </ul>
            </div>
        </div>
    `;
    document.body.appendChild(modalsContainer);

    // After DOM parsing, you can bind these. Note: In the actual HTML you would need to add id="card-noelia" and id="card-santiago" to the respective elements.
    setupModal('card-noelia', 'modal-noelia');
    setupModal('card-santiago', 'modal-santiago');
    setupModal('card-juanpablo', 'modal-juanpablo');
});

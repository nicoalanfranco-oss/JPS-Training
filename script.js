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
    `;
    document.body.appendChild(modalsContainer);

    // After DOM parsing, you can bind these. Note: In the actual HTML you would need to add id="card-noelia" and id="card-santiago" to the respective elements.
    setupModal('card-noelia', 'modal-noelia');
    setupModal('card-santiago', 'modal-santiago');
});

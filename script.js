// Ruta del archivo JSON relativa al directorio de tu proyecto
const jsonFilePath = "datos.json";

// Función para cargar y mostrar los datos desde el JSON
function cargarDatos() {
    fetch(jsonFilePath)
        .then(response => {
            if (!response.ok) {
                throw new Error("No se pudo cargar el archivo JSON");
            }
            return response.json();
        })
        .then(data => {
            // Actualiza la salida HTML para incluir "elevation" y "azimuth"
            const dataContainer = document.getElementById("data");
            dataContainer.innerHTML = `
                <p>Temperatura del panel FV - Punto 1: ${data.dato1} °C</p>
                <p>Temperatura del panel FV - Punto 2: ${data.dato2} °C</p>
                <p>Temperatura del aire circundante: ${data.dato3} °C</p>
                <p>Piranómetro 1 - Irradiancia solar horizontal / global: ${data.dato5} W/m^2</p>
                <p>Piranómetro 2- Irradiancia solar incidente en el panel FV: ${data.dato4} W/m^2</p>
                <p>Anemometro: ${data.dato6} m/s</p>
                <p>Veleta: ${data.dato7} °</p>
                <p>Elevation: ${data.elevation.toFixed(2)} °</p>
                <p>Azimuth: ${data.azimuth.toFixed(2)} °</p>
            `;
        })
        .catch(error => {
            console.error("Error al cargar el JSON:", error);
        });
}

// Llamar a la función para cargar los datos cuando se carga la página
cargarDatos();

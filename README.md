# Sistema de Monitoreo Microclimático para Seguidor Solar

![Universidad Industrial de Santander](favicon.png)

## Descripción 📝
Sistema integral para monitorear variables microclimáticas y posición solar en tiempo real, diseñado para seguidores solares. Captura datos mediante Arduino, los procesa en Python y los visualiza en una interfaz web interactiva.

## Características principales ✨
- 📊 Registro continuo de 7 variables ambientales
- ☀️ Cálculo preciso de posición solar (azimuth y elevación)
- ⏱️ Actualización automática cada 30 segundos
- 💾 Almacenamiento en JSON (tiempo real) y Excel (histórico)
- 🌐 Visualización web responsive

## Estructura de archivos 📂
.
├── datos/ # Datos generados
│ ├── datos.json # Últimos registros (JSON)
│ └── datos.xlsx # Histórico completo (Excel)
├── src/ # Código fuente
│ ├── receive.py # Script principal de adquisición
│ ├── recibir.py # Utilidad para Excel
│ ├── recibir3.py # Versión alternativa
│ ├── script.js # Lógica web
│ └── index.html # Interfaz de usuario
└── assets/ # Recursos multimedia
├── styles.css # Estilos
└── imagen.jpg # Diagrama del sistema

Copy

## Requisitos técnicos ⚙️
### Hardware
- Placa Arduino con sensores conectados
- Puerto serial disponible (COM6 por defecto)

### Software
- Python 3.8+
- Bibliotecas Python:
  ```bash
  pip install pvlib pandas pyserial
Navegador web moderno (Chrome/Firefox recomendado)

Configuración inicial 🛠️
Clonar repositorio:

bash
Instalar dependencias:

bash
Copy
pip install -r requirements.txt
Configurar puerto serial en receive.py:

python
Copy
arduino_port = 'COM6'  # Cambiar según necesidad
Uso 🚀
Iniciar sistema de adquisición:

bash
Copy
python src/receive.py
Abrir interfaz web:

bash
Copy
start src/index.html  # Windows
open src/index.html   # macOS
Variables monitoreadas 🌡️
Sensor	Variable	Unidad
Dato1	Temp. panel PV (Pto1)	°C
Dato2	Temp. panel PV (Pto2)	°C
Dato3	Temp. aire	°C
Dato4	Irradiancia (panel)	W/m²
Dato5	Irradiancia global	W/m²
Dato6	Velocidad viento	m/s
Dato7	Dirección viento	°
-	Elevación solar	°
-	Azimuth solar	°
Licencia 📜
Proyecto desarrollado por Daniel García y Daniel Gutiérrez bajo licencia MIT.

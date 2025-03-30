import serial
import json
import datetime
import pvlib
import pandas as pd

# Configura la conexión serial (ajusta el puerto COM según tu configuración)
arduino_port = 'COM6'  # Reemplaza 'COMX' con el puerto correcto
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)

# Crea un diccionario para almacenar los datos
data = []

# Definir la ubicación y la zona horaria
latitud = 7.1420939356621105
longitud = -73.12132294503459
altitud = 967
zona_horaria = 'Etc/GMT+5'

try:
    while True:
        # Lee una línea de datos desde el Arduino
        line = ser.readline().decode().strip()

        # Divide la línea en valores separados por comas
        values = line.split(',')

        if len(values) == 7:  # Asegúrate de que haya 7 valores
            dato1, dato2, dato3, dato4, dato5, dato6, dato7 = map(float, values)

            # Obtener la fecha y hora actual
            fechahoy = datetime.datetime.now()

            # Obtener la ubicación
            ubicacion = pvlib.location.Location(latitud, longitud)

            # Definir la hora y fecha de interés
            fecha = pd.Timestamp(fechahoy, tz=zona_horaria)

            # Obtener la posición solar
            posicion_solar = pvlib.solarposition.get_solarposition(fecha, ubicacion.latitude, ubicacion.longitude, altitud)

            # Obtener el ángulo cenital
            azimuth = float(posicion_solar['azimuth'])
            elevation = float(posicion_solar['elevation'])

            # Almacena los datos en una lista
            data.append([fechahoy, dato1, dato2, dato3, dato4, dato5, dato6, dato7, elevation, azimuth])

            # Escribe el diccionario en un archivo JSON
            with open('datos.json', 'w') as json_file:
                json.dump(data, json_file)
                print("Datos escritos en datos.json")
                print(data)

            # Crear un DataFrame de pandas con los datos
            df = pd.DataFrame(data, columns=['FechaHora', 'Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5', 'Dato6', 'Dato7', 'Elevation', 'Azimuth'])

            # Guardar el DataFrame en un archivo Excel (xlsx)
            df.to_excel('datos.xlsx', index=False)
            print("Datos escritos en datos.xlsx")

except KeyboardInterrupt:
    ser.close()
    print("Conexión cerrada")
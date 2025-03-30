import serial
import json
import datetime
import pvlib
import pandas as pd
import os

# Configura la conexión serial (ajusta el puerto COM según tu configuración)
arduino_port = 'COM6'  # Reemplaza 'COMX' con el puerto correcto
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)

# Crea un diccionario para almacenar los datos
data = {}

# Definir la ubicación y la zona horaria
latitud = 7.1420939356621105
longitud = -73.12132294503459
altitud = 967
zona_horaria = 'Etc/GMT+5'

# Contador de archivos JSON creados
contar_json = 0

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

            # Almacena los datos en el diccionario
            data['Hora'] = fechahoy.strftime("%Y-%m-%d %H:%M:%S")
            data['dato1'] = dato1
            data['dato2'] = dato2
            data['dato3'] = dato3
            data['dato4'] = dato4
            data['dato5'] = dato5
            data['dato6'] = dato6
            data['dato7'] = dato7
            data['elevation'] = elevation  # Agrega la elevación
            data['azimuth'] = azimuth  # Agrega el azimuth

            # Escribe el diccionario en un archivo JSON
            with open('datos.json', 'w') as json_file:
                json.dump(data, json_file)
                print("Datos escritos en datos.json")
                print(data)

            # Incrementa el contador de archivos JSON creados
            contar_json += 1

            # Si se han creado 60 archivos JSON, actualiza el archivo de Excel
            if contar_json == 60:
                if contar_json == 1080:
                    if os.path.exists('datos.xlsx'):
                        os.remove('datos.xlsx')
                # Crear un DataFrame de pandas con los datos
                df = pd.DataFrame([data], columns=['Hora', 'Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5', 'Dato6', 'Dato7', 'Elevation', 'Azimuth'])

                # Guardar el DataFrame en un archivo Excel (xlsx)
                df.to_excel('datos.xlsx', index=False, mode='a', header=False)  # Modo 'a' para agregar sin reemplazar
                print("Datos agregados en datos.xlsx")

                # Reiniciar el contador de archivos JSON
                contar_json = 0

except KeyboardInterrupt:
    ser.close()
    print("Conexión cerrada")

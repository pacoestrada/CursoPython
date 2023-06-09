import json
import urllib.request

# Obtener el contenido JSON de la URL proporcionada
url = "https://api.tutiempo.net/json/?lan=es&apid=zwDX4azaz4X4Xqs&ll=40.4178,-3.7022"
# Envíamos una solicitud HTTP GET a la URL pedida en el ejercicio 6 y guarda la respuesta del servidor en la variable 'response'
respuesta = urllib.request.urlopen(url)

"""Leemos el contenido de 'respuesta'l y lo decodificamoso decodifica a una cadena de caracteres (usando 'utf-8')
 y luego lo convierte en un objeto de Python (diccionario) usando json.loads() """
data = json.loads(respuesta.read().decode('utf-8'))


# Imprimir la cabecera de la tabla
print(f'{"FECHA":<15} | {"TEMP MIN":<15} | {"TEMP MAX":<15} | {"HUMEDAD":<15} | {"VIENTO":<15} |{"DESCRIPCIÓN":<15}')
print("----------------------------------------------------------------------------------------------------------------")

# Iterar sobre los 7 días y mostrar la información en la tabla
for i in range(1, 8):
    day = data[f'day{i}'] # Accedemos al diccionario asociado al día específico utilizando el valor de 'i', y asignarlo a la variable 'day'
    date = day['date']
    max_temp = day['temperature_max']
    min_temp = day['temperature_min']
    wind = day['wind']
    humidity = day['humidity']
    text = day['text']
    print(f'{date:<15} | {min_temp:<15} | {max_temp:<15} | {humidity:<15} | {wind:<15} | {text:<16}')





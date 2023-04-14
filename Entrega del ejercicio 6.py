import json

# leer el contenido del archivo tiempo.json
with open('tiempo.json') as f:
    data = json.load(f)

# imprimir la cabecera de la tabla
print(f'{"FECHA":<15} | {"TEMP MIN":<15} | {"TEMP MAX":<15} | {"HUMEDAD":<15} | {"VIENTO":<15} |{"DESCRIPCIÓN":<15}')
print("----------------------------------------------------------------------------------------------------------------")


# iterar sobre los 7 días y mostrar la información en la tabla
for i in range(1, 8):
    day = data[f'day{i}']
    date = day['date']
    max_temp = day['temperature_max']
    min_temp = day['temperature_min']
    wind = day['wind']
    humidity = day['humidity']
    text = day['text']
    print(f'{date:<15} | {min_temp:<15} | {max_temp:<15} | {humidity:<15} | {wind:<15} | {text:<16}')




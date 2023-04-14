import json

# leer el contenido del archivo tiempo.json
with open('tiempo.json') as f:
    data = json.load(f)

# imprimir la cabecera de la tabla
print(f'{"Fecha":<15} | {"Máx Temp":<15} | {"Mín Temp":<15} | {"Viento":<15}  1 {"Humedad":<15} | {"Descripción":<15}')


# iterar sobre los 7 días y mostrar la información en la tabla
for i in range(1, 8):
    day = data[f'day{i}']
    date = day['date']
    max_temp = day['temperature_max']
    min_temp = day['temperature_min']
    wind = day['wind']
    humidity = day['humidity']
    text = day['text']
    print(f'{date:<15} {max_temp:<15} {min_temp:<15} {wind:<15} {humidity:<15} {text:<15}')




import json

# leer el contenido del archivo tiempo.json
with open('tiempo.json') as f:
    data = json.load(f)

# imprimir la cabecera de la tabla
print('{:<10} {:<15} {:<15} {:<15} {:<15}'.format('Fecha', 'Máx Temp', 'Mín Temp', 'Viento', 'Humedad'))

# iterar sobre los 7 días y mostrar la información en la tabla
for i in range(1, 8):
    day = data[f'day{i}']
    date = day['date']
    max_temp = day['temperature_max']
    min_temp = day['temperature_min']
    wind = day['wind']
    humidity = day['humidity']
    print('{:<10} {:<15} {:<15} {:<15} {:<15}'.format(date, max_temp, min_temp, wind, humidity))



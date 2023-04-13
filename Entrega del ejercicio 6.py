import json

# leer el archivo json
with open('tiempo.json', 'r') as f:
    tiempo = json.load(f)

# obtener la información necesaria para cada día
datos = []
for i in range(1, 8):
    dia = tiempo[f'day{i}']
    fecha = dia['date']
    max_temp = dia['temperature_max']
    min_temp = dia['temperature_min']
    texto = dia['text']
    datos.append((fecha, max_temp, min_temp, texto))

# mostrar la tabla
print('Fecha      Máx.  Mín.  Descripción')
for fecha, max_temp, min_temp, texto in datos:
    print(f'{fecha}  {max_temp:>4}ºC  {min_temp:>4}ºC  {texto}')

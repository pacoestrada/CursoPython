import json
import urllib.request
import tkinter as tk

# Obtenemos el contenido JSON de la URL proporcionada en el ejercicio 6.
url = "https://api.tutiempo.net/json/?lan=es&apid=zwDX4azaz4X4Xqs&ll=40.4178,-3.7022"

# Envíamos una solicitud HTTP GET a la URL del ejercicio 6 y guardamos la respuesta en la variable 'respuesta'
respuesta = urllib.request.urlopen(url)

""" Leeremos el contenido de 'respuesta' y lo decodificamos (usando 'utf-8')
 y luego lo convertimos en un diccionario de Python usando json.loads() """
data = json.loads(respuesta.read().decode('utf-8'))

# Creamos la ventana de Tkinter y configuramos su título y color de fondo
ventana = tk.Tk()
ventana.title("Pronóstico del tiempo")
ventana.configure(bg="#ADD8E6")

# Creamos la cabecera de la tabla y la agregamos a la ventana usando etiquetas
cabecera = ["FECHA", "TEMP MIN", "TEMP MAX", "HUMEDAD", "VIENTO", "DESCRIPCIÓN"]
for i, titulo in enumerate(cabecera):
    label = tk.Label(ventana, text=titulo, font=("Arial", 12, "bold"), bg="#BBFFBB")
    label.grid(row=0, column=i, padx=(5, 5), pady=(5, 5))

# Iteramos sobre los 7 días y mostramos la información en la ventana
for i in range(1, 8):
    day = data[f'day{i}']
    date = day['date']
    max_temp = day['temperature_max']
    min_temp = day['temperature_min']
    wind = day['wind']
    humidity = day['humidity']
    text = day['text']

    # Agregamos la información a la ventana usando etiquetas
    datos = [date, min_temp, max_temp, humidity, wind, text]
    for j, dato in enumerate(datos):
        if j == 0:  # Destacamos las fechas con un color diferente
            label = tk.Label(ventana, text=dato, fg="#FF0000", bg="#ADD8E6")
        else:
            label = tk.Label(ventana, text=dato, bg="#ADD8E6")
        label.grid(row=i, column=j, padx=(5, 5), pady=(5, 5))

# Ejecutamos el bucle principal de Tkinter para mostrar la ventana
ventana.mainloop()

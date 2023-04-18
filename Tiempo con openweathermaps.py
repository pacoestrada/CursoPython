import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime, timedelta

API_KEY = "API-KEY"#reemplazar aquí la llave del API

def obtener_pronostico(codigo_postal):
    url = f"http://api.openweathermap.org/data/2.5/forecast?zip={codigo_postal}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "200":
        raise ValueError("No se pudo obtener la información del tiempo.")

    pronostico = []
    for item in data["list"]:
        fecha = datetime.fromtimestamp(item["dt"])
        temp_min = item["main"]["temp_min"]
        temp_max = item["main"]["temp_max"]
        viento = item["wind"]["speed"]
        precipitacion = item["pop"] * 100
        pronostico.append((fecha, temp_min, temp_max, viento, precipitacion))

    return data["city"]["name"], pronostico


def mostrar_pronostico():
    codigo_postal = entry.get()
    try:
        ciudad, pronostico = obtener_pronostico(codigo_postal)
        resultado = f"Pronóstico del tiempo para {ciudad} en los próximos 7 días:\n\n"
        resultado += "Fecha\t\tTemp. Mín\tTemp. Máx\tViento (m/s)\tPrecipitación (%)\n"

        for fecha, temp_min, temp_max, viento, precipitacion in pronostico:
            resultado += f"{fecha.strftime('%Y-%m-%d')}\t{temp_min:.1f}°C\t\t{temp_max:.1f}°C\t\t{viento:.1f}\t\t{precipitacion:.0f}%\n"

        messagebox.showinfo("Pronóstico del tiempo", resultado)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Consulta del tiempo")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Introduce el código postal:")
label.grid(row=0, column=0, padx=(0, 5), pady=(0, 5))

entry = tk.Entry(frame)
entry.grid(row=0, column=1, pady=(0, 5))

button = tk.Button(frame, text="Consultar", command=mostrar_pronostico)
button.grid(row=1, columnspan=2, pady=(0, 5))

root.mainloop()

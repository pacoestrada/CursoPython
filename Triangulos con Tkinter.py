import tkinter as tk

def tipo_triangulo():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                resultado.config(text="Es un triángulo equilátero", fg="green")
            elif a==b or a==c or b==c:
                resultado.config(text="Es un triángulo isósceles", fg="green")
            else:
                resultado.config(text="Es un triángulo escaleno", fg="green")
        else:
            resultado.config(text="No se puede formar un triángulo", fg="red")
    except ValueError:
        resultado.config(text="Los valores introducidos no son numéricos", fg="red")
        

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Triángulos")
ventana.config(bg="lightblue")

# Crear frames
frame_info = tk.Frame(ventana, bg="lightblue")
frame_info.pack(pady=20)
frame_inputs = tk.Frame(ventana, bg="lightblue")
frame_inputs.pack(pady=20)
frame_resultado = tk.Frame(ventana, bg="lightblue")
frame_resultado.pack(pady=20)

# Crear widgets en frame_info
tk.Label(frame_info, text="Este programa calcula el tipo de triángulo que se forma\na partir de las medidas de sus lados.", 
         bg="lightblue", font=("Arial", 20)).pack()

# Crear widgets en frame_inputs
tk.Label(frame_inputs, text="Lado a: ", bg="lightblue", font=("Arial", 16)).grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(frame_inputs, font=("Arial", 16), width=10)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Lado b: ", bg="lightblue", font=("Arial", 16)).grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(frame_inputs, font=("Arial", 16), width=10)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Lado c: ", bg="lightblue", font=("Arial", 16)).grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(frame_inputs, font=("Arial", 16), width=10)
entry_c.grid(row=2, column=1, padx=10, pady=5)

# Crear widget en frame_resultado
resultado = tk.Label(frame_resultado, bg="lightblue", font=("Arial", 20))
resultado.pack()

# Crear botón para calcular
tk.Button(ventana, text="Calcular", bg="lightblue", font=("Arial", 20), command=tipo_triangulo).pack(pady=20)

ventana.mainloop()

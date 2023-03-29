# Crear lista de gastos vacía
gastos = []

# Preguntar al usuario si quiere indicar más gastos
continuar = input("Quieres introducir más gastos (si/no): ")

# Siempre que haya más gastos (respuesta si)
while continuar.lower() == "si":

# Pedimos los datos del gasto al usuario
    motivo = input("Motivo del gasto: ")
    lugar = input("Lugar del gasto: ")
    cantidad = float(input("Cantidad gastada: "))

#Creamos un diccionario que contenga la información del gasto
    gasto = {"motivo": motivo, "lugar": lugar, "cantidad": cantidad}

#Añadimos diccionario a la lista de gastos
    gastos.append(gasto)

#Preguntamos al usuario si quiere introducir más gastos
    continuar = input("Quieres introducir más gastos (si/no): ")

cantidad_total = 0

# Para cada gasto en la lista de gastos
print("\n")
print("GASTOS DESGLOSADOS Y TOTAL.\n")
for gasto in gastos:
#Salida con la información del gasto
    print(gasto['motivo'] + ' en ' + gasto['lugar'] + ' : ' + str(gasto['cantidad']) + ' euros')

# Acumulamos la cantidad del gasto en cantidad_total
    cantidad_total += gasto["cantidad"]

# Imprimir CANIDAD TOTAL acumulada en "cantidad_total", convertida en string
print("CANTIDAD TOTAL : " + str(cantidad_total) + "euros")





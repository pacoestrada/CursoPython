# Crear lista de gastos vacía
gastos = []

# Preguntar al usuario si quiere introducir más gastos
continuar = input("Quieres introducir más gastos (si/no): ")

# Mientras haya más gastos
while continuar.lower() == "si":
    # Pedir datos del gasto al usuario
    motivo = input("Motivo del gasto: ")
    lugar = input("Lugar del gasto: ")
    cantidad = float(input("Cantidad gastada: "))

    # Crear diccionario con la información del gasto
    gasto = {"motivo": motivo, "lugar": lugar, "cantidad": cantidad}

    # Añadir el diccionario a la lista de gastos
    gastos.append(gasto)

    # Preguntar al usuario si quiere introducir más gastos
    continuar = input("Quieres introducir más gastos (si/no): ")

cantidad_total = 0
# Para cada gasto en la lista de gastos
print("\n")
print("GASTOS DESGLOSADOS Y TOTAL.\n")
for gasto in gastos:
    # Imprimir información del gasto
    print(gasto['motivo'] + ' en ' + gasto['lugar'] + ' : ' + str(gasto['cantidad']) + ' euros')

    # Acumular la cantidad del gasto en cantidad_total
    cantidad_total += gasto["cantidad"]

# Imprimir cantidad_total
print("Cantidad total : " + str(cantidad_total) + "euros")





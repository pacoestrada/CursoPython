mes_usuario = input("Introduce el nombre de un mes: ")
mes = mes_usuario.lower()

if  (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == " agosto" or mes == "Octubre" or mes == "diciembre"):

    print("El mes de", mes_usuario, "tiene 31 días.")

elif mes == "febrero":
    print("El mes de", mes_usuario, "tiene 28 días.")

elif (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):

    print("El mes de", mes_usuario, "tiene 30 días.")

else:
    print("No conozco ese mes.")

mes = input("Introduce el nombre de un mes: ")
mes = mes.lower()

if  (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == " agosto" or mes == "Octubre" or mes == "diciembre"):

    print("El mes de", mes, "tiene 31 días.")

elif mes == "febrero":
    print("El mes de", mes, "tiene 28 días.")

elif (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
    dias = 30

    print("El mesde", mes, "tiene 30 días.")

else:
    print("No conozco ese mes.")

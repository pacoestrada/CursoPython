mes = input("Introduce el nombre de un mes: ")

if mes.lower() == "enero":
    dias = 31
elif mes.lower() == "febrero":
    dias = 28
elif mes.lower() == "marzo":
    dias = 31
elif mes.lower() == "abril":
    dias = 30
elif mes.lower() == "mayo":
    dias = 31
elif mes.lower() == "junio":
    dias = 30
elif mes.lower() == "julio":
    dias = 31
elif mes.lower() == "agosto":
    dias = 31
elif mes.lower() == "septiembre":
    dias = 30
elif mes.lower() == "octubre":
    dias = 31
elif mes.lower() == "noviembre":
    dias = 30
elif mes.lower() == "diciembre":
    dias = 31
else:
    print("No conozco ese mes.")
    dias = None

if dias is not None:
    print(f"{mes.capitalize()} tiene {dias} días.")
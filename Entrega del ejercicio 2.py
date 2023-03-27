#solicitamos al usuario que introduzca el mes

mes_usuario = input("Introduce el nombre de un mes: ")

#pasamos a minúsculas con el método lower()

mes = mes_usuario.lower()

#establecemos primer condicional con los meses de 31 días y, de cumplirs,la salida print

if  (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):

    print("El mes de", mes_usuario, "tiene 31 días.")

#de no cumplirse arriba, continuamos con febrero y, en su caso, la salida print

elif mes == "febrero":
    print("El mes de", mes_usuario, "tiene 28 días.")

#de no cumplirse arriba, continuamos con los meses de 30 días y, en su caso, la salida print

elif (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):

    print("El mes de", mes_usuario, "tiene 30 días.")

#si no se cumplen ninguna de las condiciones anteriores devolvemos la salida de "desconocido"

else:
    print("No conozco ese mes.")

    #FIN EJECUCIÓN

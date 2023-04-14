def calcula_nota_final(control1, control2, examen):
    """
    Calcula la nota final a partir de las notas de los controles y el examen.
    Si el estudiante ha suspendido el examen final, devuelve la nota del examen.
    Si el estudiante ha aprobado el examen final, devuelve una media ponderada
    en la que los controles valen un 10% cada uno y el examen final un 80% de la nota.
    """
    if examen < 5:
        return examen
    else:
        nota_final = 0.1 * (control1 + control2) + 0.8 * examen
        return round(nota_final, 2)


def extrae_datos(linea):
    """
    Extrae el nombre, apellidos y notas del alumno a partir de una línea del fichero.
    Devuelve los valores como una tupla.
    """
    campos = linea.strip().split(",")
    nombre = campos[0]
    apellidos = campos[1]
    control1 = float(campos[2])
    control2 = float(campos[3])
    examen = float(campos[4])
    return nombre, apellidos, control1, control2, examen


def calcula_notas_finales(nombre_fichero):
    """
    Lee el fichero con las notas de los alumnos y calcula sus notas finales.
    Imprime una línea por cada alumno con su nota final y si ha aprobado o no la asignatura.
    """
    with open(nombre_fichero, encoding="utf-8") as fichero:
        for linea in fichero:
            nombre, apellidos, control1, control2, examen = extrae_datos(linea)
            nota_final = calcula_nota_final(control1, control2, examen)
            if nota_final >= 5:
                print(nombre, apellidos, nota_final, "aprobado")
            else:
                print(nombre, apellidos, nota_final, "suspenso")

#llamamaos a la función sobre el archivo 'notas.csv' que hemos descargado en el ejercicio
calcula_notas_finales('notas.csv')

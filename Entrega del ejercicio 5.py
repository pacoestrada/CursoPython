import csv

def calcula_notas_finales(nombre_archivo):
    """
    Calcula las notas finales de un conjunto de alumnos a partir de un archivo CSV con el formato especificado.

    :param nombre_archivo: el nombre del archivo CSV a procesar.
    :return: None
    """
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        # Saltar la primera línea (encabezados)
        #next(lector_csv)
        for linea in lector_csv:
            nombre = linea[0]
            apellidos = linea[1]
            control1 = float(linea[2])
            control2 = float(linea[3])
            examen_final = float(linea[4])

            # Calcular la nota final
            nota_final = 0
            if examen_final >= 5:
                nota_final = 0.1 * control1 + 0.1 * control2 + 0.8 * examen_final
            else:
                nota_final = examen_final

            # Determinar si el alumno aprobó o no
            aprobado = False
            if nota_final >= 5:
                aprobado = True

            # Imprimir la información del alumno
            print(nombre, apellidos, round(nota_final, 2), 'aprobado' if aprobado else 'suspenso')

# Ejemplo de uso
calcula_notas_finales('notas.csv')

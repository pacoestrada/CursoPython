def tipo_triangulo(a, b, c):
    """
    Definimos una función que recibe las longitudes de 3 segmentos y comprueba si se pueden formar un triángulo.
    Si se puede, la función determina si el triángulo es equilátero, isósceles o escaleno y muestra el resultado
    por pantalla.
    De lo contrario muestra un mensaje indicando que no se puede formar un triángulo.

    :parámetro a: Longitud del primer segmento.
    :parámetro b: Longitud del segundo segmento.
    :parámetro c: Longitud del tercer segmento.

    """
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("El triángulo es equilátero")
        elif a == b or b == c or a == c:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")
    else:
        print("No se puede formar un triángulo")

tipo_triangulo(1, 1, 1)
tipo_triangulo(1, 3, 3)
tipo_triangulo(2, 4, 5)
tipo_triangulo(1, 2, 3)
tipo_triangulo(2, 1, 3)
tipo_triangulo(3, 2, 1)

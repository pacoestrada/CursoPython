def tipo_triangulo(a, b, c):
    """
    Creamos una función tipo_triangulo que recibe las longitudes de 3 segmentos
    e imprime un mensaje por consola indicando si con esos segmentos se puede o no formar un triángulo.
    En caso de que sí se pueda, la función indica si forman un triángulo equilátero (3 lados iguales),
    isósceles (2 lados iguales y 1 diferente) o escaleno (3 lados distintos).

    """
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilátero")
        elif a == b or b == c or a == c:
            print("Isósceles")
        else:
            print("Escaleno")
    else:
        print("No es un triángulo")

tipo_triangulo(1, 1, 1)
tipo_triangulo(1, 3, 3)
tipo_triangulo(2, 4, 5)
tipo_triangulo(1, 2, 3)
tipo_triangulo(2, 1, 3)
tipo_triangulo(3, 2, 1)

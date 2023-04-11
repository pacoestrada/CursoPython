def tipo_triangulo(a, b, c):
    """
    Definimos una función que recibe las longitudes de 3 segmentos y comprueba si se pueden formar un triángulo. Si se puede, la función
    determina si el triángulo es equilátero , isósceles  o escaleno y delvuelve el resultado

    :parámetro a: Longitud del primer segmento.
    :tipo a: float
    :parámetro b: Longitud del segundo segmento.
    :tipo b: float
    :parámetro c: Longitud del tercer segmento.
    :tipo c: float
    :return: Una cadena de texto que indica el tipo de triángulo que se puede formar con los segmentos dados
    como parámetros o si no se puede formar un triángulo
    :tipo del return: str
    """
    if a + b > c and a + c > b and b + c > a:
        if a == b == c: #no había pensado en esta forma más simple y correcta. Gracias.
            return "Equilátero"
        elif a == b or b == c or a == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No es un triángulo"


print(tipo_triangulo(1, 1, 1))
print(tipo_triangulo(1, 3, 3))
print(tipo_triangulo(2, 4, 5))
print(tipo_triangulo(1, 2, 3))
print(tipo_triangulo(2, 1, 3))
print(tipo_triangulo(3, 2, 1))

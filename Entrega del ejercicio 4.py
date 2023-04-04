def tipo_triangulo():
    """
     Función que olicita al usuario que introduzca las longitudes de 3 lados y determina si es posible formar un triángulo con los valores introducidos.
     Si se puede, nos devuelve si es un triángulo equilátero, isósceles o escaleno, o si no es un triángulo.
    """
    a = float(input("Ingrese la longitud del primer lado: "))
    b = float(input("Ingrese la longitud del segundo lado: "))
    c = float(input("Ingrese la longitud del tercer lado: "))

    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("El triangulo definido por esos tres lados es Equilátero") #caso equilatero
        elif a == b or b == c or a == c:
            print("El triangulo definido por esos tres lados es Isósceles") #caso isóceles
        else:
            print("El triangulo definido por esos tres lados es Escaleno")  #caso escaleno
    else:
        print("El triangulo definido por esos tres lados es No es un triángulo") # No es triángulo


tipo_triangulo()


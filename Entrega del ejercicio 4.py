
#definimos la función tipo_tiángulo
def tipo_triangulo():
    """
     Función que solicita al usuario que introduzca las longitudes de 3 lados y determina si es posible formar un triángulo con los valores introducidos.
     Si se puede, nos devuelve si es un triángulo equilátero, isósceles o escaleno o, ensu caso, si no es un triángulo.
    """
    a = float(input("Ingrese la longitud del primer lado y pulse ENTER: "))
    b = float(input("Ingrese la longitud del segundo lado y pulse ENTER: "))
    c = float(input("Ingrese la longitud del tercer lado y pulse ENTER: "))

    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("\n El triangulo definido por esos tres lados es EQUILATERO") #caso equilatero
        elif a == b or b == c or a == c:
            print("\n El triangulo definido por esos tres lados es ISÓSCELES") #caso isóceles
        else:
            print("\n El triangulo definido por esos tres lados es ESCALENO")  #caso escaleno
    else:
        print("\n El triangulo definido por esos tres lados es NO ES UN TIÁNGULO") # No es triángulo

#llamamos a la función tipo_tirangulo()

tipo_triangulo()


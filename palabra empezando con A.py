#pedimos al usuario que escriba una palabra

palabra = input("Introduce una palabra: ")
palabra = palabra.lower()
contador = 1
while "a" != palabra[0]:
    contador = contador + 1
    palabra = (input("tu palabra no empieza por a escribe otra:"))

print("Tu palabra empieza por" , palabra[0] , "Para ello has usado" , contador , "palabras" )

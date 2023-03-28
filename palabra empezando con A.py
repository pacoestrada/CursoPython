#pedimos al usuario que escriba una palabra

palabra = input("Introduce una palabra: ")
contador = 1
while "a" != palabra[0]:
    contador = contador + 1
    palabra = (input("tu palabra no empieza por A o a .Escribe otra:"))

print("Tu palabra empieza por A o a. Para ello has usado" , contador , "palabras" )

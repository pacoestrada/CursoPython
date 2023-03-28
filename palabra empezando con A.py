#pedimos al usuario que escriba una palabra

palabra = input("Introduce una palabra: ")
#iniciamos un contador
contador = 1
#comparamos hasta que se cumpla, aumentando el contador a uno
while "a" != palabra[0]:
    contador = contador + 1
    palabra = (input("Tu palabra no empieza por A o a .Escribe otra:"))
#imprimimos resultado
print("Tu palabra empieza por A o a. Para ello has usado" , contador , "palabras" )

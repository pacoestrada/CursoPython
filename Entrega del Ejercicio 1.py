#Establecemos la constante valor de pi
pi = 3.14159

# Solicitamos el valor del radio al usuario
radio = float(input("Introduce el valor del radio: "))

# Calculo de la longitud de la circunferencia
longitudCircunferencia = 2 * pi * radio

# Calculo del área del círculo
areaCirculo = pi * (radio ** 2)

# Imprimimos los resultados
print("La longitud de la circunferencia es:", longitudCircunferencia)
print("El área del círculo es:", areaCirculo)
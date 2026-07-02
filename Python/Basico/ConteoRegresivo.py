
import sys


input =int(input("Ingrese un número para iniciar el conteo regresivo: "))

if input % 5 != 0:
    sys.exit("El número debe ser múltiplo de 5.")
    
while  input > 0:
    print(input)
    input -= 1
    


print("¡Despegue!")
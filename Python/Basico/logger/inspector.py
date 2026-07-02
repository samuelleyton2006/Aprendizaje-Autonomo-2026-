import os 

ruta = '.'

contenedor = os.listdir(ruta)

for elements in contenedor:
    print(f"ARCHIVO ENCONTRADO = [{elements}]")
    
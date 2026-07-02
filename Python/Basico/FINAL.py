"""""""""
import os 
import sys

print ("1. 1. Registrar estado de un servidor" )
print ("2. Ver historial completo ")
print ("3. Salir ")
ingreso = int(input("Donde va a ingresar :"))

if ingreso == 3:
    sys.exit("SALIDA EXITOSA")
if ingreso == 2:
    try:
        with open ("estados.txt","r")as f:
            for line in f:
                print (line)
    except FileNotFoundError:
        print ("Archivo no encontrado")

       # f(f"nombre del servidor {input}")
if ingreso == 1:
    online = 1
    offline = 0
    Servidor = input("Nombre Servidor :")
    Estado = int(input("Estado Del Servidor (1/0) :"))
    if Estado == 1:
        texto = "online"
    if Estado == 0:
        texto ="ofline"
    with open ("estados.txt","a")as f:
        f.write(f"[{Servidor}]-ESTADO : [{texto}]\n")
"""""""""

import os
import sys

# Usamos un bucle infinito para que el menú se repita una y otra vez
while True:
    print("\n--- MONITOR DE SERVIDORES ---")
    print("1. Registrar estado de un servidor")
    print("2. Ver historial completo")
    print("3. Salir")
    
    ingreso = int(input("Seleccione una opción: "))

    if ingreso == 3:
        print("SALIDA EXITOSA. ¡Hasta luego!")
        break  # El 'break' rompe el bucle 'while' y el programa termina limpiamente
        
    elif ingreso == 2:
        try:
            with open("estados.txt", "r") as f:
                print("\n=== HISTORIAL DE ESTADOS ===")
                for line in f:
                    # Usamos .strip() para quitar saltos de línea extra al imprimir
                    print(line.strip())
                print("============================\n")
        except FileNotFoundError:
            print("\n[AVISO] Archivo no encontrado. Registre un servidor primero.\n")

    elif ingreso == 1:
        Servidor = input("Nombre Servidor: ")
        Estado = int(input("Estado Del Servidor (1 = ONLINE / 0 = OFFLINE): "))
        
        if Estado == 1:
            texto = "ONLINE"
        elif Estado == 0:
            texto = "OFFLINE"
        else:
            texto = "DESCONOCIDO" # Por si el usuario escribe un 5 o cualquier otra cosa
            
        with open("estados.txt", "a") as f:
            f.write(f"[{Servidor}] - ESTADO: [{texto}]\n")
        
        print(f"\n[ÉXITO] Servidor {Servidor} registrado correctamente.\n")


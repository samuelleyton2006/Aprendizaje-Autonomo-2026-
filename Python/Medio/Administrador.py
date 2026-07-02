base_datos = []

IP = input("su ip es :")
ROL = input("Su rol es :")

base_datos.append({"rol" :ROL,"ip" :IP})

# 1. Creamos una sola variable (llamémosla 'elemento') por cada vuelta
for elemento in base_datos:
    # 2. Ahora usamos las claves del diccionario ("servidor" y "rol") para imprimir
    print(f"IP = [{elemento['ip']}] - ROL = [{elemento['rol']}]")
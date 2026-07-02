Disp = {
    "id": ("001", "002", "003"), 
    "tipo": ("Computador", "Celular", "Sobremesa"), 
    "Estado": (True, False, True)
}

# Como tienes 3 elementos, recorremos las posiciones 0, 1 y 2
for i in [0, 1, 2]:
    if Disp["Estado"][i]:
        print(f"El dispositivo {Disp['id'][i]} ({Disp['tipo'][i]}) está encendido.")



Disp = [{"id":["001","002","003"], "tipo": ["Computador","Celular","Sobremesa"], "Estado":[True,False,False]}]

for clave in Disp():
    print(clave)

for valor in Disp.values():
    print(valor)


"""""""""""""""""""""
Dispositivos = [{"id":["uno", "dos", "tres"], "estado":[ True, False, True ]}]

#mayores = {nombre: edad for nombre, edad in edades.items() if edad >= 18}

Verdaderos = {id: estado for id ,estado in Dispositivos.items() if estado == True }

print = (Verdaderos)

    #"tipo":["SSH", "IP", "SSH"]
"""""""""""""""
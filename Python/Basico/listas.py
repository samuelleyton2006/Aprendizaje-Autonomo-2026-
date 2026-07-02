notas = [4.5, 3.2, 2.8, 5.0, 3.9, 1.5, 4.8]
contarUNO = 0 
contarDOS = 0
""""""""""
for i in range (len(notas)):
    print(f"Nota {i + 1}: {notas[i]}")
def imprimir_Aprobados(notas):
        for i in notas:
            if i >= 3.0:
                print(f"Aprobado: {i}")

"""""""""

for i in range (len(notas)):
    if notas[i] >= 3.0:
        contarUNO += 1
print(f"Cantidad de aprobados: {contarUNO}")

for i in range (len(notas)):
    if notas [i] < 3.0:
        contarDOS += 1
print(f"Cantidad de reprobados: {contarDOS }")

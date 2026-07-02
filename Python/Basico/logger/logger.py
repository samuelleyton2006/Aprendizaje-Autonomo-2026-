import os 


"""""""""
with open ("log.txt", "a") as f:
    f.write(input("lo que quiera pa : ") + "\n")


if os.path.exists("log.txt"):
    print ("El archivo existe")
else :
    print("archivo no encontrado ")

"""""""""

with open ("log.txt", "r") as f:
    for line in f:
        print(line)
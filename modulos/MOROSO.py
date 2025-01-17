import os

def moroso(nombre):
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
    ruta_archivo = os.path.join(escritorio, "moroso.txt")
    with open(ruta_archivo, "w") as file:
        for i in range (2000000):
            file.write(f"{nombre} paga moroso vamos a por ti\n")
    exit()
#print("funciones lambda")


def saludar(nombre):
    return f"hola {nombre}"

print(saludar("Nicolas"))

#transformado en lamda

areaT = lambda nom: nom

print(areaT("Nicolas"))
#Punto 1
def clasificar(numero):
    if(numero%2==0):
        print("Par")
    else:
        print("inpar")

#lambda
clasificarp=lambda numero :numero%2

#Punto 2

def revisarlista(lista):
    for elemento in lista:
        if(elemento>10):
            print("Mayor que 10: ",)
#lambda
annotarnumero10=lambda numero:numero>10

#Punto 3 Diccionario
crearDiccionario= lambda nombre,edad,ocupacion :{'nombre':nombre,'edad':edad,'ocupacion':ocupacion}

#Punto 5
multiplicarnumero=lambda numero:numero*100

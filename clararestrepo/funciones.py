#Punto 1
def clasificarPar(numero):
    return (numero%2)

#funcion lambda
calsificar=lambda numero:numero%2

#Punto 2
def revisarLista(lista):
    for elemento in lista:
        if(elemento>10):
            print("Mayor que 10")

anotarNumero10=lambda numero:numero>10 

#Punto 3
crearDiccionario=lambda nombre, edad, ocupacion: {'nombre':nombre,'edad':edad,'ocupacion':ocupacion}

#Punto 5
multiplicarNumero=lambda numero:numero*100
#punto1
from funcion2 import multiplicarCien


def clasificarPar(numero):
    return numero%2


clasificarPar2 = lambda numero:numero%2   

#punto 2

def revisarLista(lista):
    for elemento in lista:
        if(elemento>10):
            print("Mayor que 10")

anotarNumero10=lambda numero:numero>10           

#punto 3

crearDiccionario = lambda nombre,edad,ocupacion:{'nombre':nombre,'edad':edad,'ocupacion':ocupacion}

#punto 5
multiplicarnumero = lambda numero:numero*100
def clasificarPar(numero):
    return (numero%2)
clasificarPar2= lambda numero: numero %2 


#punto 
def revisarLista(lista):
    for elemento in lista:
        if(elemento > 10):
            print("mayor que 10")

anotarNumero10= lambda numero:numero>10

#punto3

crearDiccionario = lambda nombre,edad,ocupacion: {'nombre':nombre,'edad':edad,'ocupacion':ocupacion}

#punto 5
multiplicarNumero= lambda numero:numero*100
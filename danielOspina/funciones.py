#clasificar si un número es par

def clasificarPar(numero):
    return(numero%2)

clasificarPar=lambda numero:numero%2


#punto 2

def revisarLista(lista):
    for elemento in lista:
        if(elemento>10):
            print("mayor que 10")

#no se puede hacer con lambda, se deben hacer otras cosas
anotarNumero10=lambda numero: numero>10

#punto 3

crearDiccionario=lambda nombre,edad,ocupacion: {'nombre':nombre,'edad':edad,'ocpacion':ocupacion}

#punto 5
multiplicarNumero=lambda numero:numero*100




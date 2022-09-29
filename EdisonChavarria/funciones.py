def clasificarPar(numero):
    return(numero%2)
clasificarPar=lambda numero:numero%2

def revisarLista(lista):
    for elemento in lista:
        if(elemento>10):
            print("mayor que 10")

anotarNumero=lambda numero:numero>10


crearDiccionario=lambda nombre,edad,ocupacion:{'nombre':nombre,'edad':edad,'ocupacion':ocupacion}

multiplicarNumero=lambda numero:numero*100
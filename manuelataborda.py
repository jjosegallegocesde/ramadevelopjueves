#Funciones Lambda

#Declarar
def saludar(nombre):
    return nombre

#Invocar/llamar funcion   
print (saludar("Manuela"))

#Transformando en lambda funcion

#Declarando
saludar2=lambda nombre:nombre

#Invocar/llamar funcion   
print (saludar2("Juan"))

#Funcion que clasifique par
def nmeropar(numero):
    if (numero % 2 ==0):
     print("El número es par")
    else:
        print("El número es impar")

    npar=nmeropar(8)
    print('el numero par es: ',npar)




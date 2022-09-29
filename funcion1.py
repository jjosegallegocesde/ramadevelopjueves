#funcion que sume dos numeros
def sumarNumeros(numero1,numero2):
    return numero1+numero2
suma=sumarNumeros(5,2)
print('la suma es: ',suma)

#Funcion lambda que suma dos numeros 
sumarLambda=lambda numero1,numero2:numero1+numero2
suma=sumarLambda(5,2)
print('la suma es: ',suma)
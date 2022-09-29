#funcion que sume dos numero
def sumarNumeros(numero1,numero2):
    return numero1 + numero2

suma = sumarNumeros(5,2)
print('la suma es: ', suma)

#Funcion Lambda que sume dos numeros 

sumarLambda = lambda numero1,numero2 :numero1+numero2
suma = sumarLambda(5,10)
print('la suma es: ', suma)

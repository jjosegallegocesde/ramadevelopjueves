#funcion que sume dos numeros


def sumar(numero1,numero2):
    return (numero1+numero2)

suma=sumar(5,2)
print('la suma es: ',suma)

sumar2=lambda numero1,numero2:numero1+numero2
suma=sumar2(5,2)
print(suma)
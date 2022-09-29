#funciones que sume dos numeros

def sumar(numero1,numero2):
    return numero1 + numero2

resultado = sumar(5,5)
print(f'El resultado es {resultado}')


sumarLambda = lambda numero1, numero2: numero1 + numero2

resultado2 = sumarLambda(5,5)
print(f'El resultado es {resultado2}')

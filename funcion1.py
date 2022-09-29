#función que sume dos números
def sumarNumeros(numero1, numero2):
    return numero1+numero2

suma=sumarNumeros(5,2)
print(f'la suma es: {suma}')

#función lambda que sume dos números
sumarNumeros2=lambda numero1,numero2:numero1+numero2

print(f'la suma es: {sumarNumeros2(5,2)}')
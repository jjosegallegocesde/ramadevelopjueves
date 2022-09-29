# Función que multiplique un número por 100


def multiplicar(n):
    cont = 0
    while cont < 100:
        cont = cont + 1
        print(f'{n} x {cont} = {n * cont} ')
    else:
        print('Adios :)')


print(multiplicar(2))

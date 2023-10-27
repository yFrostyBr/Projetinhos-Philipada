import random

def advinhe(x):
    numero_aleatorio = random.randint(1,x)
    advinhe = 0 
    while advinhe != numero_aleatorio:
        advinhe = int(input(f'Chute um número de 1 a {x}'))
        if advinhe < numero_aleatorio:
            print('Desculpe, Tente novamente. Muito baixo')
        elif advinhe > numero_aleatorio:
            print('Desculpe, Tente novamente. Muito Alto')

    print(f'Parabéns, você acertou o número {numero_aleatorio}')

advinhe(20)


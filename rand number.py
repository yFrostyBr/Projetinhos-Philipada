import random

def comp(x):
    min = 1
    max = x
    fb = ''
    while fb != 'c':
        if min != max:
            advinhe = random.randint(min, max)
        else:
            advinhe = min    
        fb = input(f"O número {advinhe} é muito alto (A), Baixo (B), ou correto (C)")
        if fb == 'A':
            max = advinhe - 1
        elif fb == 'B':
            min = advinhe + 1
  
    print("Parabéns, o computador conseguiu advinhar o número correto")

comp(6)
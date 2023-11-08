import random

def jogar():
    user = input("'r' para pedra, 'p' para papel e 't' para tesoura: ")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return 'Empate'
    
    if venceu(user, computer):
        return 'Você venceu!'
    
    return 'Você perdeu!'

def venceu(jogador, oponente):
    if (jogador == 'r' and oponente == 't') or (jogador == 't' and oponente == 'p') or (jogador == 'p' and oponente == 'r'):
        return True
    return False

resultado = jogar()
print(resultado)

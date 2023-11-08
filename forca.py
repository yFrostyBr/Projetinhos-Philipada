import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  
    lives = 7

   
    while len(word_letters) > 0 and lives > 0:
        
        print('Você tem', lives, 'vidas restantes e já usou essas letras : ', ' '.join(used_letters))

       
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palavra Atual: ', ' '.join(word_list))

        user_letter = input('Chute uma letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nSua Letra,', user_letter, 'não está na palavra.')

        elif user_letter in used_letters:
            print('\nVocê já usou essa letra. Tente outra letra.')

        else:
            print('\nLetra Inválida.')

   
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Você morreu e a letra era: ', word)
    else:
        print('Parabéns, você conseguiu advinhar a palavra que era: ', word, '!!')


if __name__ == '__main__':
    hangman()

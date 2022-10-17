import random
import string
from wordlist import words


def validate_word():
    word =random.choice(words)
    while "-" in word or ' ' in word:
        word =random.choice(words)
    
    return word.upper()
    
def hangman():
    word=validate_word()
    word_set=set(word)
    letter_used=set()
    alphabet=set(string.ascii_uppercase)
    lives=7


    while len(word_set) > 0 and lives > 0:
        
        # what current word is (ie W - R D)
        word_search = [letter if letter in letter_used else '-' for letter in word]
        print('Current word: ', ' '.join(word_search))
        print(f'you have {lives} lives left and you have used',' '.join(letter_used))
        
        
        user_letter = input('Enter a letter:').upper()
        if user_letter in alphabet - letter_used:
            letter_used.add(user_letter)
            if user_letter in word:
                word_set.remove(user_letter)
                print('')
            else:
                lives-=1
                print("your letter is not in the word")
        elif (user_letter in letter_used ):
            print('you have already used the letter')
        else:
            print('That is not a letter')
    if lives==0:
        print('you have died \n the word is ', word)
    else:
        print('you have gussed the word {} correctly'.format(word))
if __name__ == '__main__':
    hangman()
import random
from words import words
import string
from stage import progress


def hangman():
    word = random.choice(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
        print(progress[lives])
    if lives == 0:
        print(lives)
        print('You died. The word was', word)
    else:
        print('Correct! You guessed the word', word, '.')


while True:
    hangman()
    option = input("Do you want to continue? Yes(Y) or No(N): ").lower()
    if option == 'y':
        continue
    else:
        break

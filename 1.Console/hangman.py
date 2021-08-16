'''

Hangman Game

- This script is hangman game.
- Save secret word and guess this words.
- If you have never heard this, check here.
    https://en.wikipedia.org/wiki/Hangman_(game)

'''

import random
import string


def main():
    # choose random secret word
    secret_word_list = ["banana", "apple", "grape", "pineapple", "mgchat", "python"]
    secret_word = random.choice(secret_word_list)

    # Use list to access data and update.
    guess_list = ["-"] * len(secret_word)

    # Then, chane list into string
    guess_word = "".join(guess_list)

    # for hangman life
    error = 0

    # Use set to show the missed word without duplication
    misssed_word = set()

    while error < 6:
        

        print(guess_word)

        # display hangman state
        hangman_state(error)

        guess_letter = input("Guess: ")
        if len(guess_letter) != 1:
            print('You should input a single letter\n')
            continue
                
        elif guess_letter not in string.ascii_lowercase:
            print('Please enter a lowercase English letter\n')
            continue
        

        if guess_letter not in secret_word:
            error += 1
            misssed_word.add(guess_letter)

        else:
            for index, letter in enumerate(secret_word):
                if letter == guess_letter:
                    guess_list[index] = letter

        print("Missed words: " + ",".join(misssed_word))
        print()
        print()

        guess_word = "".join(guess_list)
        if guess_word == secret_word:
            print("Congratulations! You win.")
            exit()

    hangman_state(6)
    print("You loose!")


def hangman_state(error):
    if error == 0:
        print("   ___ ")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("  ____|_")

    elif error == 1:
        print("   ___ ")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("  ____|_")

    elif error == 2:
        print("   ___ ")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("  |   |")
        print("      |")
        print("  ____|_")

    elif error == 3:
        print("   ___ ")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("  |   |")
        print("      |")
        print("  ____|_")

    elif error == 4:
        print("   ___ ")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("  |   |")
        print("      |")
        print("  ____|_")

    elif error == 5:
        print("   ___ ")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("  |   |")
        print(" /    |")
        print("  ____|_")

    elif error == 6:
        print("   ___ ")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("  |   |")
        print(" / \  |")
        print("  ____|_")


# execute main function
if __name__ == "__main__":
    main()

# Write your code here
import random, string
secret_words = ['python', 'java', 'kotlin', 'javascript']
secret_word = random.choice(secret_words)
hint_word = ['-']*len(secret_word)

print('H A N G M A N')
while True:
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == 'exit':
        exit()

    elif option == 'play':
        age = 8
        guessed_letters = []

        while age>0:
            print()
            print(''.join(hint_word))
            
            if ''.join(hint_word) == secret_word:
                print('You guessed the word!')
                print('You survived!')
                break

            guess_letter = input('Input a letter: ')
            

            if len(guess_letter) != 1:
                print('You should input a single letter')
                continue
                
            elif guess_letter not in string.ascii_lowercase:
                print('Please enter a lowercase English letter')
                continue

            if guess_letter in guessed_letters:
                print("You've already guessed this letter")
                
            elif guess_letter not in secret_word:
                print("That letter doesn't appear in the word")
                age -= 1
                
            

            else:
                for index, letter in enumerate(secret_word):
                    if letter == guess_letter:
                        hint_word[index] = letter

            guessed_letters.append(guess_letter)          
            
        else:    
            print('You lost!')
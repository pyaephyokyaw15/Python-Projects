'''

Dice

- This script is dice game.
- Run from terminal and give number of matches.
- Example:
    python dice.py 3
    3 is no_of_matches

'''


# importing modules
import random
import sys


# charlist to configure for display
screen = [
    [" ","P","l","y","a","e","r","1","             ","P","l","a","y","e","r","2",],
    [" ", "-", "-", "-", "-", "-", "                ", "-", "-", "-", "-", "-"],
    ["|", " ", " ", " ", " ", " ", "|", "              ", "|", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", "|", "              ", "|", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", "|", "              ", "|", " ", " ", " ", " ", " ", "|"],
    [" ", "-", "-", "-", "-", "-", "                ", "-", "-", "-", "-", "-"]
]


def main():

    player1_score = 0
    player2_score = 0

    print('Dice Game!')
    no_matches = int(sys.argv[1])
    
    for i in range(no_matches):
        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)

        # update character in screen(list)
        screen_layout(player1, player2)

        # show the screen(list) as the desired format
        show_display()

        # for single match
        if player1 > player2:
            player1_score += 1

        elif player2 > player1:
            player2_score += 1

        clear_screen()
        print()

    if player1_score > player2_score:
        print("Player1 wins")
        player1_score += 1

    elif player2_score > player1_score:
        print("Player2 wins")
        player2_score += 1

    else:
        print("Draw")



#  ===========================  functions ==================================

def screen_layout(player1, player2):

    # update the character in screen(list) according to the dice no
    # Since plyaer2 is 8 index after player1.
    # formula = player1 + 8*i
    # To get i, enumerate is used.

    for i, player in enumerate([player1, player2]):
        if player == 1:
            screen[3][3 + 8 * i] = "o"

        elif player == 2:
            screen[2][1 + 8 * i] = "o"
            screen[4][5 + 8 * i] = "o"

        elif player == 3:
            screen[3][3 + 8 * i] = "o"
            screen[2][1 + 8 * i] = "o"
            screen[4][5 + 8 * i] = "o"

        elif player == 4:
            screen[2][1 + 8 * i] = "o"
            screen[2][5 + 8 * i] = "o"
            screen[4][1 + 8 * i] = "o"
            screen[4][5 + 8 * i] = "o"

        elif player == 5:
            screen[2][1 + 8 * i] = "o"
            screen[2][5 + 8 * i] = "o"
            screen[4][1 + 8 * i] = "o"
            screen[4][5 + 8 * i] = "o"
            screen[3][3 + 8 * i] = "o"

        else:
            screen[2][1 + 8 * i] = "o"
            screen[2][5 + 8 * i] = "o"
            screen[3][1 + 8 * i] = "o"
            screen[3][5 + 8 * i] = "o"
            screen[4][1 + 8 * i] = "o"
            screen[4][5 + 8 * i] = "o"


def show_display():

    # show the screen(list) as the desired format
    for line in screen:
        for char in line:
            print(char, end="")
        print()

def clear_screen():

    global screen
    screen = [
    [" ","P","l","y","a","e","r","1","             ","P","l","a","y","e","r","2",],
    [" ", "-", "-", "-", "-", "-", "                ", "-", "-", "-", "-", "-"],
    ["|", " ", " ", " ", " ", " ", "|", "              ", "|", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", "|", "              ", "|", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", "|", "              ", "|", " ", " ", " ", " ", " ", "|"],
    [" ", "-", "-", "-", "-", "-", "                ", "-", "-", "-", "-", "-"]
]


# execute main function
if __name__ == "__main__":
    main()

'''

Tic-Tac-Toe

- This script is Tic-Tac-Toe game.
- It is also known as O-X game.
- You can choose one player or two player.
- Choose between 1 and 9 as a position.
    Start at upper left grid.

'''

# importing modules
import random
import sys


def main():
    print("Welcome to Tic-Tac-Toe Game!")

    # Get user option ( 1 or 2 player)
    user_option = option()

    # intialize board
    board = [" " for i in range(10)]
    display(board)

    while True:

        # check any space is on board
        # if available, let player 1 play
        if is_space_available(board):
            player1_move(board)
            print()

        # if unavailable, break loop
        else:
            break

        # check any space is on board
        # if available, let next player play
        if is_space_available(board):

            # determine player or computer according to user_option
            if user_option == "1":
                coputer_move(board)

            else:
                player2_move(board)

            print()

        # if unavailable, break loop
        else:
            break

    # if board has no space, and no one wins, it is tie.
    print("Tie")



# ================================  Functions =================================

def display(board):
    print()
    print("     |     |      ")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  ")
    print("_____|_____|_____ ")
    print("     |     |      ")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  ")
    print("_____|_____|_____ ")
    print("     |     |      ")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  ")
    print("     |     |      ")
    print()
    print('======================================================')
    


def is_space_available(board):
    return board.count(" ") > 1


def is_winner(board, letter):

    # check the 'game' position
    return (
        (board[0] == board[1] == board[2] == letter)
        or (board[3] == board[4] == board[5] == letter)
        or (board[6] == board[7] == board[8] == letter)
        or (board[0] == board[3] == board[6] == letter)
        or (board[1] == board[4] == board[7] == letter)
        or (board[2] == board[5] == board[8] == letter)
        or (board[0] == board[4] == board[8] == letter)
        or (board[2] == board[4] == board[6] == letter)
    )


def player1_move(board):
    while True:
        try:
            player1 = int(input("Plyaer1, Enter location between 1 and 9 : "))

            if player1 > 9:
                print("Please enter between 1 and 9")

            elif board[player1 - 1] != " ":
                print("This space is occupied.")

            else:
                break

        # if input cannot be converted to integer
        except:
            print("Please enter between 1 and 9")

    board[player1 - 1] = "X"
    display(board)

    if is_winner(board, "X"):
        print("Player1 Wins")
        sys.exit()


def player2_move(board):
    while True:
        try:
            player2 = int(input("Plyaer2, Enter location between 1 and 9 : "))

            if board[player2 - 1] != " ":
                print("This space is occupied.")

            else:
                break

        # if input cannot be converted to int.
        except:
            print("Please enter between 1 and 9.")

    board[player2 - 1] = "O"
    display(board)

    if is_winner(board, "O"):
        print("Player2 Wins")
        sys.exit()


def coputer_move(board):

    # list the availabe space on board
    available_pos = [i for i in range(9) if board[i] == " "]

    # random place on the available space on board
    board[random.choice(available_pos)] = "O"
    display(board)

    if is_winner(board, "O"):
        print("Computer Wins")
        sys.exit()


def option():

    # loop until getting valid option.
    while True:
        user_option = input("Choose Option\n1 Plyaer\n2 Players : ")
        if user_option == "1":
            print('\n===================================\n')
            print("Plyaer1  : X")
            print("Computer : O")
            print()
            break

        elif user_option == "2":
            print('\n===================================\n')
            print("Plyaer1 : X")
            print("Player2 : O")
            break

        print("Invalid Choice!. Please choose 1 or 2.")

    return user_option


# execute main function
if __name__ == "__main__":
    main()

'''

Rock Paper Scissor

- This script is Rock-Paper-Scissor game.
- You can choose one player or two player.
- You can choose number of matches.
- Hide your input when typing.
   

'''

# importing modules
import random
import getpass

# set three items
items = ['rock','paper','scissor']



def main():

    # set scores
    player1_score = 0
    player2_score = 0

    print('Rock Paper Scissor Game!')

    # get user option ( 1 or 2 player)
    user_option = option()

    # get matches
    matches = int(input('No of matches: '))

    # set player name
    player1_name = input('Enter palyer1 name: ')
    player2_name = 'Computer'
    if user_option == '2':
        player2_name = input('Enter palyer2 name: ')
    
    print('==========================================================')
    print(player1_name, 'vs', player2_name)


    # loop for matches
    for i in range(matches):
        print('==========================================================')
        
        # get the player1 choice
        # hide user input
        player1_choice = getpass.getpass('{}, what do you choose ? Rock , Paper or Scissor : '\
                                .format(player1_name)).lower()

        # loop until valid choice
        while player1_choice not in items:
            player1_choice = getpass.getpass('{}, what do you choose ? Rock , Paper or Scissor : '\
                                    .format(player1_name)).lower()


        # check 2 player or 1 player
        # if two player
        if user_option == '2':
            player2_choice = getpass.getpass('{}, what do you choose ? Rock , Paper or Scissor : '\
                                    .format(player2_name)).lower()

            # loop until valid choice
            while player2_choice not in items:
                player2_choice = getpass.getpass('{}, what do you choose ? Rock , Paper or Scissor : '\
                                        .format(player2_name)).lower()

        # if one player
        else:
            player2_choice = random.choice(items).lower()

        # print choices
        print('{} : {}'.format(player1_name, player1_choice))
        print('{} : {}'.format(player2_name, player2_choice))

        # who wins for each game
        winner = who_win(player1_choice, player2_choice)

        # add scores
        if winner == 1:
            player1_score += 1

        elif winner == 2:
            player2_score += 1

    print('==========================================================')
    # announce winner:
    if player1_score > player2_score:
        print(player1_name, 'wins!')

    elif player2_score > player1_score:
        print(player2_name, 'wins!')

    else:
        print('Draw!')
    


# =======================  Functions =========================================

def option():

    # loop until getting valid option.
    while True:
        user_option = input("Choose Option\n1 Plyaer\n2 Players : ")

        if user_option == '1' or user_option == '2':
            break

        print("Invalid Choice!. Please choose 1 or 2.")
    return user_option




def who_win(player1_choice, player2_choice):

    if player1_choice == 'rock':
        if player2_choice == 'paper':
            return 2

        elif player2_choice == 'scissor':
            return 1
            

    elif player1_choice == 'paper':
        if player2_choice == 'rock':
            return 1
            
        elif player2_choice == 'scissor':
            return 2

    elif player1_choice == 'scissor':
        if player2_choice == 'paper':
            return 1
            
        elif player2_choice == 'rock':
            return 2



# execute main function
if __name__ == '__main__':
    main()
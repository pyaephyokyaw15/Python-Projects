import random

def main():

    while True:
        print()
        item = ['Rock', 'Paper', 'Scissor']
        print('Rock Paper Scissor Game!')
        name = input('Name: ')
        no_match = int(input('No of matches: '))
        print('Weclome,',name)
        print()

        score_dict = {}
        score_dict[name] = 0
        score_dict['computer'] = 0

        

        for i in range(no_match):
            player1 = input('{} , What do you choice ? Rock, Paper, Scissor: '.format(name))
            comupter = random.choice(item)
            print('Computer:', comupter)

            if player1 == comupter:
                print('Draw')

            elif player1 == 'Rock':
                if comupter == 'Paper':
                    print('Computer wins!')
                    score_dict['computer'] += 1
                
                elif comupter == 'Scissor':
                    print('You win!')
                    score_dict[name] += 1

            elif player1 == 'Paper':
                if comupter == 'Scissor':
                    print('Computer wins!')
                    score_dict['computer'] += 1
                
                elif comupter == 'Rock':
                    print('You win!')
                    score_dict[name] += 1

            elif player1 == 'Scissor':
                if comupter == 'Rock':
                    print('Computer wins!')
                    score_dict['computer'] += 1
                
                elif comupter == 'Paper':
                    print('You win!')
                    score_dict[name] += 1


            print('Match:', i+1)
            for player, score in score_dict.items():
                print('{} : {}'.format(player, score), end= '          ')
            print()
            print()

        if score_dict[name] > score_dict['computer']:
            print('Congrautulaions! You win')

        elif score_dict[name] < score_dict['computer']:
            print('Sorry! You loose')

        else:
            print('Draw!')


        next_match = input('Do you want to play another game, y /n : ')
        if next_match == 'n':
            break











if __name__ == '__main__':
    main()
'''
Credit-card Validation

- This script is used to determine whether a certain credit-card is 
  valid or not.

- It is based on Luhn’s algorithm.

- It also determines the type of Card(eg.MASTER, VISA, AMEX)


'''

def main():

    # getting number from user until it is numeric value
    while True:
        card = input("Number: ")
        if card.isnumeric():
            break

    if (is_valid(card)):

        # if card is valid, determine what card it is.
        if len(card) == 15 and (card[0:2] == '34' or card[0:2] == '37'):
            print('AMEX')

        elif len(card) == 16 and card[0:2] in ['51','52','53','54','55']:
            print('MASTERCARD')

        elif 13 <= len(card) <= 16 and card[0] == '4':
            print('VISA')

        else:
            print("INVALID")

    else:
        print("INVALID")




def is_valid(card):

    odd_pos_digit_sum = 0
    even_pos_digit_sum = 0

    # In algorithm, digit in card starting LSB

    # to get digits from the last digit by 2
    for position in range(len(card)-1, -1, -2):

        # sum each digit directly
        odd_pos_digit_sum += int(card[position])
        
    # to get digits even position started from last digit
    for position in range(len(card)-2, -1, -2 ):

        # peprocessing before sum due to algorithm
        digit = int(card[position])
        digit *= 2

        # if the result digit contains two digit separate them and sum
        if digit > 9:
            digit = (digit // 10) + (digit % 10)
        
        # sum each digit
        even_pos_digit_sum += digit

    check_sum = odd_pos_digit_sum + even_pos_digit_sum
    # if check_sum is end in 0 , valid
    if (check_sum % 10):
        return False
    return True
        
       

    

if __name__ =="__main__":
    main()




    


    


'''
Bank System

- This script is the prototype of bank system.
- Function:
    1. Create account
    2. Deposit amount
    3. Withdrawl amount 
- After bank is closed(i.e.choose 3), save all the data in csv file.

'''

# importing modules
import random
import csv

# creating database dictionary
database = {}

# main function
def main():
    status = home()

    # loop until close(choose '3')
    while status!='3': 

        # 1. create account
        if status == '1':      
            create_acc()

        # 2. account login
        elif status == '2':

            # check the account number is entered, not name.
            # If it is not account number, get input again until the account number is entered.
            while True:
                try:    
                    user_acc = int(input('Enter your account number : '))
                    break
                except:
                    print('Please enter account number.Not your name.')

            # check account and if it does not exist.
            if user_acc not in database:
                print('Your account is not registered!')
                user_option = input('1.Create an account\n2.exit\nOption : ')

                if user_option == '1':
                    create_acc()
                else:
                    pass

            # check account and if it exists.
            else :
                password = input('Enter your passowrd : ')

                # checking password until right
                while database[user_acc]['password'] != password:
                    print('Worng Password!')
                    password = input('Enter your passowrd : ')

                user_option = menu()

                # Loop until choosing 4(exit)
                while user_option!='4':

                    # 1. Balacne
                    if user_option == '1':
                        print('Balance :',database[user_acc]['amount'])


                    # 2. Deposit
                    elif user_option == '2':
                        deposit_amount = int(input (' Enter amount to deposit: '))
                        database[user_acc]['amount'] += deposit_amount
                        print('Balance :',database[user_acc]['amount'])

                    # 3. Withdrawl
                    elif user_option == '3':
                        withdraw_amount = int(input(' Enter amount to withdraw: '))

                        # make sure the withdrawl amount is not greater than the balance
                        while withdraw_amount > database[user_acc]['amount']:
                            print('Your balance is not insufficient!')
                            print('Balance :', database[user_acc]['amount'])
                            withdraw_amount = int(input(' Enter amount to withdraw: '))

                        # subtract amount from balance
                        database[user_acc]['amount'] -= withdraw_amount
                        print('Balance :', database[user_acc]['amount'])

                    print('-----------------------------------------')

                    # get user option again
                    user_option = menu()

        # if not 1 nor 2
        else:
            print('Invalid Option')


        print('-------------------------------------------------------------------------------')

        # display home screen for next user
        status = home()

    # When the service is closed, it display the bank database.
    print(database)

    # Save the data in CSV Format.
    with open('bank_database.csv','w',newline='') as file:
        database_csv = csv.writer(file)
        database_csv.writerow(['Acc no', 'Name', 'Password','Balance'])

        for acc in database:
            database_csv.writerow([acc,database[acc]['name'],database[acc]['password'],database[acc]['amount']])



# =======================================  Functions ========================================================
def home():
    print('            Welcome to Mg Chat Bank        ')
    print('        ***********************************')
    return input('1.Create account\n2.Account login\n3.Close\Option : ')


def menu():
    return input('1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit\nOption: ')


def create_acc():
    name = input('Name:')
    passowrd = input('Passowrd:')
    confirm_passsword = input('Confirm Password:')

    # confirm password
    while passowrd != confirm_passsword:
        print('Your password did not match')
        passowrd = input('Passowrd:')
        confirm_passsword = input('Confirm Password:')

    # generate random account_no
    account_no = random.randrange(100000000, 1000000000)
    while account_no in database:
        account_no = random.randrange(100000000, 1000000000)

    # creat an account
    database[account_no] = {}
    database[account_no]['name'] = name
    database[account_no]['password'] = passowrd
    database[account_no]['amount'] = 0
    print('Your account has been registered!')
    print('Account No :',account_no)
    print('##############################')



# execute main function
if __name__ == '__main__':
    main()










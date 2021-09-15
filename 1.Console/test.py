class CoffeeMachine():

    # instock
    water = 400
    milk = 540 
    coffeebeans = 120
    cups = 9
    money = 550

    # espresso
    water_per_espresso = 250
    coffeebeans_per_espresso = 16
    price_per_espresso = 4


    # latte
    water_per_latte = 350
    coffeebeans_per_latte = 20
    milk_per_latte = 75
    price_per_latte = 7

    # cappuccino
    water_per_cappuccino= 200
    coffeebeans_per_cappuccino= 12
    milk_per_cappuccino= 100 
    price_per_cappuccino= 6

    def show_instock(self):
        print()
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffeebeans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print('$'+str(self.money), 'of money')
        print() 

    def ask_action(self):
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        print()
        return action

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        flavour = input()

        if flavour == '1':
            if self.water < self.water_per_espresso:
                print('Sorry, not enough water!')   
            elif self.coffeebeans < self.coffeebeans_per_espresso:
                print('Sorry, not enough coffee beans!')
            else:
                self.water -= self.water_per_espresso
                self.coffeebeans -= self.coffeebeans_per_espresso
                self.money += self.price_per_espresso
                print('I have enough resources, making you a coffee!')
                self.cups -= 1

        elif flavour == '2':
            if self.water < self.water_per_latte:
                print('Sorry, not enough water!')
            elif self.coffeebeans < self.coffeebeans_per_latte:
                print('Sorry, not enough coffee beans!')
            elif self.milk < self.milk_per_latte:
                print('Sorry, not enough milk')
            else:
                self.water -= self.water_per_latte
                self.coffeebeans -= self.coffeebeans_per_latte
                self.money += self.price_per_latte
                self.milk -= self.milk_per_latte
                print('I have enough resources, making you a coffee!')
                self.cups -= 1

        elif flavour == '3':
            if self.water < self.water_per_cappuccino:
                print('Sorry, not enough water!')
            elif self.coffeebeans < self.coffeebeans_per_latte:
                print('Sorry, not enough coffee beans!')
            elif self.milk < self.milk_per_cappuccino:
                print('Sorry, not enough milk')
            else:
                self.water -= self.water_per_cappuccino
                self.coffeebeans -= self.coffeebeans_per_cappuccino
                self.money += self.price_per_cappuccino
                self.milk -= self.milk_per_cappuccino
                self.cups -= 1
        print()


    def fill(self):
    

        print('Write how many ml of water you want to add:')
        water_add = int(input())
        self.water += water_add 

        print('Write how many ml of milk you want to add:')
        milk_add = int(input())
        self.milk += milk_add 

        print('Write how many grams of coffee beans you want to add:')
        coffee_add = int(input())
        self.coffeebeans += coffee_add

        print('Write how many disposable coffee cups you want to add:')
        cups_add = int(input())
        self.cups += cups_add
        print()
    

    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0
        print()



coffee_machine = CoffeeMachine()
while True:
    action = coffee_machine.ask_action()

    if action == 'remaining':
        coffee_machine.show_instock()
        continue
    elif action == 'exit':
        break
    elif action == 'buy':
        coffee_machine.buy()
    elif action == 'fill':
        coffee_machine.fill()
    elif action == 'take':
        coffee_machine.take()
# def print_value(self):
# 	print(f'''The coffee machine has:
# {water} of water
# {milk} of milk
# {coffee_Bean} of coffee beans
# {cups} of disposable cups''')
# 	if money == 0:
# 		print('0 of money')
#   else:
#       print(f'${money} of money')
#
# def latte(Water, Milk, Coffee_bean):
# 	water = (Water // 350)
# 	milk = (Milk // 75)
# 	coffee_beans = (Coffee_bean // 20)
# 	return water, milk, coffee_beans
#
#
# def espresso(Water, Milk, Coffee_bean):
# 	water = (Water // 250)
# 	milk = Milk
# 	coffee_beans = (Coffee_bean // 16)
# 	return water, milk, coffee_beans
#
#
# def cappuccino(Water, Milk, Coffee_bean):
# 	water = (Water // 200)
# 	milk = (Milk // 100)
# 	coffee_beans = (Coffee_bean // 12)
# 	return water, milk, coffee_beans
#
#
# def possible(Water, Milk, Coffee_bean, coffee):
# 	waters, milks, coffee_bean = 0, 0, 0
# 	if coffee == 2:
# 		waters, milks, coffee_bean = latte(Water, Milk, Coffee_bean)
# 	elif coffee == 1:
# 		waters, milks, coffee_bean = espresso(Water, Milk, Coffee_bean)
# 	elif coffee == 3:
# 		waters, milks, coffee_bean = cappuccino(Water, Milk, Coffee_bean)
# 	cup = min(waters, milks, coffee_bean)
# 	if cup >= 1:
# 		print('I have enough resources, making you a coffee!')
# 		return True
# 	elif waters < 1:
# 		print('Sorry, not enough water!')
# 		return False
# 	elif milks < 1:
# 		print('Sorry, not enough milk!')
# 		return False
# 	else:
# 		print('Sorry, not enough coffee beans!')
# 		return False
#
#
# def buy(Water, Milk, Coffee_bean, Cups, Money):
# 	coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
# 	if coffee == 'back':
# 		return Water, Milk, Coffee_bean, Cups, Money
# 	else:
# 		coffee = int(coffee)
# 	value = possible(Water, Milk, Coffee_bean, coffee)
# 	if coffee == 1 and value:
# 		Water -= 250
# 		Coffee_bean -= 16
# 		Money += 4
# 		Cups -= 1
# 	elif coffee == 2 and value:
# 		Water -= 350
# 		Milk -= 75
# 		Coffee_bean -= 20
# 		Money += 7
# 		Cups -= 1
# 	elif coffee == 3 and value:
# 		Water -= 200
# 		Milk -= 100
# 		Coffee_bean -= 12
# 		Money += 6
# 		Cups -= 1
# 	return Water, Milk, Coffee_bean, Cups, Money
#
#
# def fill(Water, Milk, Coffee_bean, Cups, Money):
# 	water = int(input('Write how many ml of water do you want to add:\n'))
# 	Water += water
# 	milk = int(input('Write how many ml of milk do you want to add:\n'))
# 	Milk += milk
# 	coffee_beans = int(input('Write how many grams of coffee beans do you want to add:\n'))
# 	Coffee_bean += coffee_beans
# 	cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
# 	Cups += cups
# 	return Water, Milk, Coffee_bean, Cups, Money
#
#
# while True:
#
# 	action = input('Write action (buy, fill, take, remaining, exit):\n')
# 	print()
# 	if action == 'buy':
# 		Water, Milk, Coffee_bean, Cups, Money = buy(Water, Milk, Coffee_bean, Cups, Money)
# 		print()
# 	elif action == 'fill':
# 		Water, Milk, Coffee_bean, Cups, Money = fill(Water, Milk, Coffee_bean, Cups, Money)
# 		print()
# 	elif action == 'take':
# 		print(f'I gave you ${Money}\n')
# 		Money = 0
# 	elif action == 'remaining':
# 		print_value(Water, Milk, Coffee_bean, Cups, Money)
# 		print()
# 	elif action == 'exit':
# 		exit()

class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.cash = 550
        self.state = "select"

    def __str__(self):
        return f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.cash} of money"""

    @staticmethod
    def display_action():
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def choose_action(self, action):
        if action == "buy":
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 -cappuccino, back - to main menu:")
            self.state = "buy"
        elif action == "fill":
            print("")
            self.display_fill_message("water", "ml")
            self.state = "fill_water"
        elif action == "take":
            print("\nI gave you ${}".format(self.cash))
            self.cash = 0
            self.state = "select"
            self.handle()
        elif action == "remaining":
            print(self)
            self.state = "select"
            self.handle()

    def choose_coffee(self, type_of_coffee):
        self.state = "select"
        if type_of_coffee == "1":
            self.make_coffee(water=250, beans=16, cost=4)
        elif type_of_coffee == "2":
            self.make_coffee(water=350, milk=75, beans=20, cost=7)
        elif type_of_coffee == "3":
            self.make_coffee(water=200, milk=100, beans=12, cost=6)

        self.handle()

    def use_supplies(self, r_water, r_milk, r_beans, r_cups=1):
        missed_resource = None

        if self.water < r_water:
            missed_resource = "water"
        elif self.milk < r_milk:
            missed_resource = "milk"
        elif self.beans < r_beans:
            missed_resource = "beans"
        elif self.cups < r_cups:
            missed_resource = "cups"
        else:
            self.water -= r_water
            self.milk -= r_milk
            self.beans -= r_beans
            self.cups -= r_cups

        return missed_resource

    def make_coffee(self, water=0, milk=0, beans=0, cost=0):
        missed_resource = self.use_supplies(water, milk, beans)
        if missed_resource is None:
            self.cash += cost
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough {}!".format(missed_resource))

    @staticmethod
    def display_fill_message(resource, measure):
        print("Write how many {} of {} do you want to add:".format(measure, resource))

    def fill_water(self, n_water):
        self.water += int(n_water)
        self.display_fill_message("milk", "ml")
        self.state = "fill_milk"

    def fill_milk(self, n_milk):
        self.milk += int(n_milk)
        self.display_fill_message("coffee beans", "grams")
        self.state = "fill_beans"

    def fill_beans(self, n_beans):
        self.beans += int(n_beans)
        self.display_fill_message("coffee", "disposable cups")
        self.state = "fill_cups"

    def fill_cups(self, n_cups):
        self.cups += int(n_cups)
        self.state = "select"
        self.handle()

    def handle(self, data=None):
        if self.state == "action":
            self.choose_action(data)
        elif self.state == "buy":
            self.choose_coffee(data)
        elif self.state == "fill_water":
            self.fill_water(data)
        elif self.state == "fill_milk":
            self.fill_milk(data)
        elif self.state == "fill_beans":
            self.fill_beans(data)
        elif self.state == "fill_cups":
            self.fill_cups(data)
        else:
            self.display_action()
            self.state = "action"


coffee_machine = CoffeeMachine()
user_input = ""

while user_input != "exit":
    coffee_machine.handle(user_input)
    user_input = input()

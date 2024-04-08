## WEEK 9 ASSIGNMENT SmartCoffeeMachine ##

class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu
    def update_menu(self, new_coffee):
        #checks if on menu, if not adds to menu
        if new_coffee.lower() in self.coffee_menu:
            print(f"{new_coffee} is already on the menu.")
        else:
            self.coffee_menu.append(new_coffee)
            print(f"{new_coffee} added to the menu!")
    def make_coffee(self, coffee_type):
        #checks if coffee is on the menu, and makes it. If not, print list of menu.
        if coffee_type.lower() in self.coffee_menu:
            print(f"your {coffee_type} is currently being made, have a good day ☕")
        else:
            print(f"sadly, {coffee_type} is not on the menu, the menu options are:")
            for coffee in self.coffee_menu:
                print(coffee)

my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')

new_coffee_order = input('What would you like to order?: ')
my_coffee_machine.make_coffee(new_coffee_order)
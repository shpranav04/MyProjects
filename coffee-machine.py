class CoffeeMachine:
    def __init__(self):
        self.water = 1000  
        self.milk = 500    
        self.coffee_beans = 200  
        self.money = 0     

    def check_resources(self, water_needed, milk_needed, beans_needed):
        """Check if there are enough resources to make coffee."""
        if self.water < water_needed:
            print("Sorry, not enough water!")
            return False
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return False
        elif self.coffee_beans < beans_needed:
            print("Sorry, not enough coffee beans!")
            return False
        else:
            return True

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        """Make coffee and deduct resources."""
        if self.check_resources(water_needed, milk_needed, beans_needed):
            print("Making coffee...")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= beans_needed
            self.money += cost
            print("Here's your coffee ☕ Enjoy!")

    def buy_coffee(self):
        """Buy coffee based on user's choice."""
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice == "espresso":
            self.make_coffee(250, 0, 16, 4)
        elif choice == "latte":
            self.make_coffee(350, 75, 20, 7)
        elif choice == "cappuccino":
            self.make_coffee(200, 100, 12, 6)
        else:
            print("Sorry, we don't have that option.")

    def show_resources(self):
        """Display the available resources."""
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Money: ${self.money}")

    def run(self):
        """Start the coffee machine."""
        while True:
            action = input("What would you like to do? (buy/show/exit): ").strip().lower()
            if action == "buy":
                self.buy_coffee()
            elif action == "show":
                self.show_resources()
            elif action == "exit":
                print("Exiting... Thank you for using the coffee machine!")
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate and run the coffee machine
coffee_machine = CoffeeMachine()
coffee_machine.run()
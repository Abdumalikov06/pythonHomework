class Animals:
    def __init__(self, species, age, weight):
        self.species = species
        self.age = age
        self.weight = weight
    
    def eat(self):
        print(f"The {self.species} species are eating.")
    
    def sleep(self):
        print(f"The {self.species} species are sleeping.")
    
    def sound(self):
        print(f"The {self.species} are making sound.")
    

class Cow(Animals):
    def __init__(self, species, age, weight):
        super().__init__(species, age, weight)
        # Handle user input with try-except to ensure valid float input
        while True:
            try:
                self.milk_production = float(input("Enter amount of milk produced by cow (in liters): "))
                if self.milk_production < 0:
                    print("Milk production can't be negative. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for milk production.")
    
    def eat(self):
        print(f"The {self.species} are eating grass.")
    
    def produce_milk(self):
        print(f"The {self.species} species are producing {self.milk_production} liters of milk per day.")
    
    def make_sound(self):
        print(f"The {self.species} species says 'Moo!'")
    
    def calculate(self):
        while True:
            try:
                self.price = float(input("Enter the price of 1 liter of milk: "))
                if self.price < 0:
                    print("Price can't be negative. Please enter a valid price.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the price of milk.")
        
        sum_earned = self.milk_production * self.price
        print(f"You get ${sum_earned} amount of money from cows today.")


# Hens class
class Hens(Animals):
    def __init__(self, species, age, weight):
        super().__init__(species, age, weight)
        while True:
            try:
                self.eggs = int(input("Enter number of eggs you get from hens today: "))
                if self.eggs < 0: #number of eggs can not be negative
                    print("Egg count can't be negative. Please enter a valid number of eggs.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the number of eggs.")
    
    def eat(self):
        print(f"The {self.species} are pecking at seeds and grains.")
    
    def lay_eggs(self):
        print(f"The {self.species} has laid {self.eggs} eggs today.")
    
    def make_sound(self):
        print(f"The {self.species} says 'Cluck!'")
    
    def count(self):
        while True:
            try:
                self.price=float(input("Enter the price of 1 egg: "))
                if self.price<0:
                    print("price can't be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the price of wool.")

        sum_earned=self.price*self.eggs
        print(f"Today, you get ${sum_earned} amount of money from the {self.species} species of hens")


# Sheep class
class Sheep(Animals):
    def __init__(self, species, age, weight):
        super().__init__(species, age, weight)
        while True:
            try:
                self.wool_weight = float(input("Enter the weight of wool produced by sheep (in kg): "))
                if self.wool_weight < 0: #wool can't be negative
                    print("Wool weight can't be negative. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for wool weight.")
    
    def eat(self):
        print(f"The {self.species} are grazing on grass.")
    
    def produce_wool(self):
        print(f"The {self.species} produces {self.wool_weight} kg of wool.")
    
    def make_sound(self):
        print(f"The {self.species} species says 'Baa!'")
    
    def calculate_wool_value(self):
        while True:
            try:
                wool_price = float(input("Enter the price of wool per kg: "))
                if wool_price < 0:
                    print("Price can't be negative. Please enter a valid price.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the price of wool.")
        
        total_value = self.wool_weight * wool_price
        print(f"You get ${total_value} amount of money from wool today.")


# Example Usage
def main():
    print("Welcome to our farm!")
    # Create a Cow instance
    cow = Cow(species="Holstein", age=4, weight=600)
    cow.eat()
    cow.sleep()
    cow.make_sound()
    cow.produce_milk()
    cow.calculate()

    # Create a Hens instance
    hens = Hens(species="Rhode Island Red", age=2, weight=3.5)
    hens.eat()
    hens.sleep()
    hens.make_sound()
    hens.lay_eggs()
    hens.count()

    # Create a Sheep instance
    sheep = Sheep(species="Merino", age=3, weight=90)
    sheep.eat()
    sheep.sleep()
    sheep.make_sound()
    sheep.produce_wool()
    sheep.calculate_wool_value()

if __name__ == "__main__":
    main()

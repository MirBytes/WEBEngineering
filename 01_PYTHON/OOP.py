class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


ahmed = person("Ahmed", 22)
ahmed.greet()

class FLIGHT():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            print(f"{name} has been added to the flight.")
        else:
            print("Sorry, the flight is full.")

PIA = FLIGHT(5)
PIA.add_passenger("Ahmed")
PIA.add_passenger("Ali")
PIA.add_passenger("Mir")
PIA.add_passenger("Ibrahim")
PIA.add_passenger("Jilani")
PIA.add_passenger("RANA")


class AnotherFlight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
MyFlight = AnotherFlight(3)

people = ["Ahmed", "Irtaza", "Jilani", "Rana", "Teymur"]

for person in people:
    if MyFlight.add_passenger(person):
        print(f"Added {person} to flight Successfully")
    else:
        print(f"Sorry, {person} could not be added to the flight.")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

amount = BankAccount(45000)
amount.deposit(40000)
print(f"Current Bank Balance is: {amount.get_balance()}")

class Animal:
    def __init__(self, type):
        self._type = type

    def speak(self):
        print(f"Animal Speaks and is of type {self._type}")

class Dog(Animal):
    def speak(self):
        print(f"Dog Barks but in parent class animal it was {self._type}")

a = Animal("domestic")
b = Dog("wild")

a.speak()
b.speak()

class Bird:
    def sound(self):
        print("Chirp")
    
class Cat:
    def sound(self):
        print("Meow")

def animal_sound(animal):
    animal.sound()

b = Bird()
c = Cat()

animal_sound(b)
animal_sound(c)
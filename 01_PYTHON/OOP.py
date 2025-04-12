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

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


ahmed = person("Ahmed", 22)
ahmed.greet()
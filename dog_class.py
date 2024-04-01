class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is sitting!")

    def roll(self):
        print(f"{self.name.title()} is rolling over!")

my_dog = Dog('jimmy', 5)
print(f"My dog's name is {my_dog.name.title()} and he is {my_dog.age} years old!")
my_dog.sit()
my_dog.roll()
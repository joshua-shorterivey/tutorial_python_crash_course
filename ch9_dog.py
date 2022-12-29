#creating classes
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age) -> None:
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """ Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate roling over in response to a command"""
        print(f"{self.name} rolled over!")

#making instance from a class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#calling methods on class
my_dog.sit()
my_dog.roll_over()

#creating additional instances of class
your_dog = Dog('Lucy', 3)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
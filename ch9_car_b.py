#working with clases and instances

class Car:
    """A Simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """initialize attributes to descrivbe a car"""
        self.make = make
        self.model = model
        self.year = year
        #setting defualt value for attritube
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    #adding method to use new attribute --> odometer reading
    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    #modifying an attribute's value through a method
    def update_odometer(self, mileage):
        """
        set the odometer reading to the given value.
        reject the change if it attempts to roll the odometer back.
        """
        #code to check if attempt is to set odometer back
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    #incrementing an attribute's value through a method
    def increment_odometer(self, miles):
        """add the given a mount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#modifying an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#using method to update attribute
my_new_car.update_odometer(25)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

#using method to increment attribute
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
#"""a class that can be used to represent a car."""
"""a set of classes used to represent gas and electric cars."""

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

class Battery:
    """a simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    #adds more detail to batter class w/o needing to involved electric car
    def get_range(self):
        """print a satement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """
        initialize attributes of the parent class
        then initializes attributes specific to an electric car"""
        super().__init__(make, model, year)
        #self.battery_size = 75
        self.battery = Battery()

    #overriding hypothetical method from parent class
    def fill_gas_tank(self):
        """electric cars don't have gas tanks"""
        print("this car doesn't need a gas tank!")
    
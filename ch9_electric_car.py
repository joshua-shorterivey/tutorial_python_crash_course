"""a set of classes that can be used to represent electric cars."""
#import Car class from module because electric car is child of it
from ch9_car import Car

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

class ElectricCar_b(Car):
    """represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """
        initialize attributes of the parent class
        then initializes attributes specific to an electric car"""
        super().__init__(make, model, year)
        #self.battery_size = 75
        self.battery = Battery()
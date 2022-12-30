# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.
print('\n---\n9-1\n---\n')
class Restaurant:
    """Modeling a basic restaurant"""
    def __init__(self, name, cuisine):
        self.restuarant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        """prints information about restaurant"""
        print(f"{self.restuarant_name.title()} serves {self.cuisine_type.title  ()} food.")
    def open_restaurant(self):
        """prints status of restuarant"""
        print(f"{self.restuarant_name.title()} is open and ready to serve.")

chubby_rice = Restaurant('chubby rice', 'chinese')
chubby_rice.describe_restaurant()
chubby_rice.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
print('\n---\n9-2\n---\n')
golden_crown = Restaurant('golden crown', 'chinese')
golden_crown.describe_restaurant()

mountain_rockies = Restaurant('mountain rockies', 'french bistro')
mountain_rockies.describe_restaurant()

thai_flower = Restaurant('thai flower', 'thai fusion')
thai_flower.describe_restaurant()


# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that prints a
# summary of the user’s information. Make another method called greet_user()
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
print('\n---\n9-3\n---\n')
class User:
    """models user profile information"""
    def __init__(
            self, first_name, last_name, age, favorite_color):
        '''initialize attritubes'''
        self.first_name = first_name
        self.last_name = last_name
        self.name = first_name + ' ' + last_name
        self.age = age
        self.favorite_color = favorite_color

    def describe_user(self):
        """describes attribrutes of user"""
        print(f"{self.first_name.title()} {self.last_name.title()} is"
              f" {self.age} years old, and their favorite color is "
              f"{self.favorite_color}.")

    def greet_user(self):
        """prints greeting to user"""
        print(f"Hello, {self.name.title()}. Welcome to our site.")

first_user = User('kevin', 'williams', 28, 'yellow')
first_user.describe_user()
first_user.greet_user()

second_user = User('eleonora', 'lakshi', 29, 'pink')
second_user.describe_user()
second_user.greet_user()

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add
# an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment the
# number of customers who’ve been served. Call this method with any num- ber
# you like that could represent how many customers were served in, say, a day
# of business.
print('\n---\n9-4\n---')
class Diner:
    """Modeling a basic restaurant"""
    def __init__(self, name, cuisine):
        self.restuarant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """prints information about restaurant"""
        print(f"{self.restuarant_name.title()} serves {self.cuisine_type.title  ()} food.")

    def open_restaurant(self):
        """prints status of restuarant"""
        print(f"{self.restuarant_name.title()} is open and ready to serve.")

    def set_number_served(self, patrons):
        """sets number of patrons served"""
        self.number_served = patrons
    
    def increment_number_served(self, new_patrons):
        """incrememnts number of patrons by new value"""
        self.number_served += new_patrons



restaurant = Diner('chubby crown', 'chinese fusion')
print(restaurant.number_served)
restaurant.number_served = 17
print(restaurant.number_served)
restaurant.set_number_served(28)
print(restaurant.number_served)
restaurant.increment_number_served(53)
print(restaurant.number_served)


# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.

print('\n---\n9-5\n---')
#use PascalCase when naming classes
class UserB:
    """models user profile information"""
    def __init__(
            self, first_name, last_name, age, favorite_color):
        '''initialize attritubes'''
        self.first_name = first_name
        self.last_name = last_name
        self.name = first_name + ' ' + last_name
        self.age = age
        self.favorite_color = favorite_color
        self.login_attempts = 0

    def describe_user(self):
        """describes attribrutes of user"""
        print(f"{self.first_name.title()} {self.last_name.title()} is"
              f" {self.age} years old, and their favorite color is "
              f"{self.favorite_color}.")

    def greet_user(self):
        """prints greeting to user"""
        print(f"Hello, {self.name.title()}. Welcome to our site.")
    
    def increment_login_attempts(self):
        """increments a users login attempts"""
        self.login_attempts +=1
    
    def reset_login_attmpets(self):
        """resets a user's number of login attempts"""
        self.login_attempts = 0

third_user = UserB('python', 'sunray', 41, 'orange')

third_user.increment_login_attempts()
third_user.increment_login_attempts()
third_user.increment_login_attempts()
print(third_user.login_attempts)
third_user.reset_login_attmpets()
print(third_user.login_attempts)

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either
# version of the class will work; just pick the one you like better. Add an
# attribute called flavors that stores a list of ice cream flavors. Write a
# method that displays these flavors. Create an instance of IceCreamStand, and
# call this method.
print('\n---\n9-6\n---\n')
class IceCreamStand(Diner):
    """attempt to model an ice cream stand based on diner class"""
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['strawberry', 'coffee', 'pralines and cream']

    def show_flavors(self):
        """prints list of flavors available"""
        for flavor in self.flavors:
            print(flavor)

coldstone = IceCreamStand('coldstone', 'ice cream')
coldstone.show_flavors()


# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise
# 9-7. Move the show_privileges() method to this class. Make a Privileges
# instance as an attribute in the Admin class. Create a new instance of Admin
# and use your method to show its privileges.
print('\n---\n9-8\n---\n')
class Privileges:
    """creates class to hold admin privileges"""
    def __init__(self):
       self.privileges = [
                'can add post', 'can delete post', 'can ban user',
                'can reset passwords', 'can change username'
        ]
 
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.
print('\n---\n9-7\n---\n')
class Admin(UserB):
    def __init__(self, first_name, last_name, age, favorite_color):
        super().__init__(first_name, last_name, age, favorite_color)
        self.privileges = [
                'can add post', 'can delete post', 'can ban user',
                'can reset passwords', 'can change username'
        ]
        self.privileges_b = Privileges()

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

drake = Admin('aubrey', 'graham', '34', 'blue')
drake.show_privileges()

megan = Admin('megan', 'stallion', '23', 'purple')
megan.privileges_b.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this
# section. Add a method to the Battery class called upgrade_battery(). This
# method should check the battery size and set the capacity to 100 if it isn’t
# already. Make an electric car with a default battery size, call get_range()
# once, and then call get_range() a second time after upgrading the battery.
# You should see an increase in the car’s range.
print('\n---\n9-9\n---\n')
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

    def upgrade_battery(self):
        """checks for size of battery and amends if needed"""
        if self.battery_size != 100:
            self.battery_size = 100
        
class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """
        initialize attributes of the parent class
        then initializes attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery()

    #overriding hypothetical method from parent class
    def fill_gas_tank(self):
        """electric cars don't have gas tanks"""
        print("this car doesn't need a gas tank!")

kia_soul = ElectricCar('kia', 'soul', 2023)
kia_soul.battery.get_range()
kia_soul.battery.upgrade_battery()
kia_soul.battery.get_range()


# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a
# module. Make a separate file that imports Restaurant. Make a Restaurant
# instance, and call one of Restaurant’s methods to show that the import
# statement is working properly.
print('\n---\n9-10\n---\n')
from ch9_restaurant_module import Restaurant as R

vegan = R('hash vegan eats', 'vegan bistro')
vegan.describe_restaurant()

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges, and Admin in one module. Create a sepa-
# rate file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.
print('\n---\n9-11\n---\n')
from ch9_combined_users_module import User as U, Admin as A
gunna = A('daveon', 'smart', 23, 'green')
gunna.show_privileges()

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.
print('\n---\n9-12\n---\n')
from ch9_admin_module import Admin as Moderator
terry = Moderator('terry', 'bogart', 30, 'yellow')
terry.privileges.show_privileges()

# 9-13. Dice: Make a class Die with one attribute called sides, which has a 
# default value of 6. Write a method called roll_die() that prints a random 
# number between 1 and the number of sides the die has. Make a 6-sided die and 
# roll it 10 times.
print('\n---\n9-13\n---\n')
from random import randint
class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

six_sided = Die()
for i in range(1,11):
    six_sided.roll_die()

# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
print('\n---\n10-Sided\n---')
ten_sided = Die(10)
for i in range(1,11):
    ten_sided.roll_die()

print('\n---\n20-Sided\n---')
twenty_sided = Die(20)
for i in range(1,11):
    twenty_sided.roll_die()

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
# five letters. Randomly select four numbers or letters from the list and print 
# a message saying that any ticket matching these four numbers or letters wins 
# a prize.
print('\n---\n9-14\n---\n')
from random import choice

lottery_numbers = []
for i in range(1,11):
    lottery_numbers.append(randint(1,100))
for i in range(1,6):
    lottery_numbers.append(choice(list('abcdefghijklmnopqrstuvwxyz')))
print(lottery_numbers)

winning_numbers = []
for i in range(1,5):
    winning_numbers.append(choice(lottery_numbers))
print(winning_numbers)

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
# the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. Print a 
# message reporting how many times the loop had to run to give you a winning 
# ticket.
print('\n---\n9-15\n---\n')
my_ticket = [18,36,24,45]
count = 0
while my_ticket != winning_numbers:
    winning_numbers = []
    for i in range(1,5):
        winning_numbers.append(choice(lottery_numbers))
    print(count)
    count +=1
    if sorted(str(my_ticket)) ==  sorted(str(winning_numbers)):
        break

print(count)
# 9-16. Python Module of the Week: One excellent resource for exploring the 
# Python standard library is a site called Python Module of the Week. Go to 
# https://pymotw.com/ and look at the table of contents. Find a module that 
# looks interesting to you and read about it, perhaps starting with the random 
# module.
print('\n---\n9-16\n---\n')
print('completed')
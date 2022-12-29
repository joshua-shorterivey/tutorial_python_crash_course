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
print('\n---\n9-3\n---\n')
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

print('\n---\n9-3\n---\n')
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

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise

# 9-7. Move the show_privileges() method to this class. Make a Privileges
# instance as an attribute in the Admin class. Create a new instance of Admin
# and use your method to show its privileges.
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
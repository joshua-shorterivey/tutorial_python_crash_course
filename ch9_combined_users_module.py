"""classes use to represent members of online forum and permissions"""
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

class Admin(User):
    """creates child class of User with privileges"""
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
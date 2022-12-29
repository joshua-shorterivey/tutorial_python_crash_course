"""creates admin child class of users"""
from ch9_combined_users_module import User

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
        self.privileges = Privileges()

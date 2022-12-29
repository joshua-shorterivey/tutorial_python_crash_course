"""a class that can be used to represent a restaurant"""

class Restaurant:
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
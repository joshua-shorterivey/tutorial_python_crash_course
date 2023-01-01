class Employee:
    """class modeling an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """store name and salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + '' + last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5_000):
        """adds amount to base annual salary"""
        self.annual_salary += amount
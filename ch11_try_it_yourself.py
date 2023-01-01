"""module to hold answers for try it yourself excercises"""
# 11-1. City, Country: Write a function that accepts two parameters: a city
# name and a country name. The function should return a single string of the
# form City, Country, such as Santiago, Chile. Store the function in a module
# called city _functions.py.
# Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to
# test). Write a method called test_city_country() to verify that calling your
# function with values such as 'santiago' and 'chile' results in the correct
# string. Run test_cities.py, and make sure test_city_country() passes.
print("\n---\n11-1\n---")
def city_country(city, country):
    """returns string featuring proper place name"""
    combination = f"{city.title()}, {country.title()}"
    return combination

#test functions for 11-1
import unittest
from ch11_city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """tests for 'ch11_city_functions.py'. """

    def test_city_country(self):
        """"do cities like 'santiago, chile' work?"""
        place_name = city_country('santiago', 'chile')
        self.assertEqual(place_name, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()

# 11-2. Population: Modify your function so it requires a third parameter,
# population. It should now return a single string of the form City, Country –
# population xxx, such as Santiago, Chile – population 5000000. Run test_cities.
# py again. Make sure test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run test _cities
# py again, and make sure test_city_country() passes again
# Write a second test called test_city_country_population() that veri- fies you
# can call your function with the values 'santiago', 'chile', and
# 'population=5000000'. Run test_cities.py again, and make sure this new test
# passes.
print("\n---\n11-2\n---")
class CityCountryTestCaseB(unittest.TestCase):
    """tests for 'ch11_city_functions.py'. """

    def test_city_country(self):
        """"do cities like 'santiago, chile' work?"""
        place_name = city_country('santiago', 'chile')
        self.assertEqual(place_name, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """
        do city, country, population combinations like 'santiago, chile, population=5000000' work?
        """
        place_name = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(place_name, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()

# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of
# these as attributes. Write a method called give_raise() that adds $5,000 to
# the annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, 
# test_give_default_raise() and test_give_custom_raise(). Use the setUp()
# method so you don’t have to create a new employee instance in each test method.
# Run your test case, and make sure both tests pass.
print("\n---\n11-3\n---")
import unittest
from ch11_employee_class import Employee

class EmployeeTestCase(unittest.TestCase):
    """tests for 'Employee' class"""
    
    def setUp(self):
        self.first_employee = Employee('jim', 'boylen', 60000)

    def test_give_default_raise(self):
        """does the default raise of 5_000 add correct amount?"""
        self.first_employee.give_raise()
        self.assertEqual(65_000, self.first_employee.annual_salary)

    def test_give_custom_raise(self):
        """does the default raise of 5_000 add correct amount?"""
        self.first_employee.give_raise(25_000)
        self.assertEqual(85_000, self.first_employee.annual_salary)

if __name__ == '__main__':
    unittest.main()

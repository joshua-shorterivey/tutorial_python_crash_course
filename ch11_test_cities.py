"""module to test function in ch11_city_functions.py"""
import unittest
from ch11_city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
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

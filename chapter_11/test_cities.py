import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        object = city_country('santiago', 'chile')
        self.assertEqual(object, 'Santiago, Chile')

    def test_city_country_population(self):
        object = city_country('santiago', 'chile', 5000000)
        self.assertEqual(object, 'Santiago, Chile - population 5000000')

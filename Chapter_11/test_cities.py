import unittest

from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Тесты для 'city_functions.py'."""

    def test_city_country(self):
        """Название города, страны вида 'Moscow, Russia' работают правильно?"""
        formatted_city_country = city_country('moscow', 'russia')
        self.assertEqual(formatted_city_country, 'Moscow, Russia')
    
    def test_city_country_population(self):
        """Название города, страны и населения работают правильно?"""
        population = city_country('moscow', 'russia', 5000000)
        self.assertEqual(population, 'Moscow, Russia - Population 5000000')

if __name__ == '__main__':
    unittest.main()

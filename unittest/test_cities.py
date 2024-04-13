import unittest
from city_functions import format_city_country

class TestFormatCityCountry(unittest.TestCase):
    def test_format_city_country(self):
        # Тестирование для различных входных данных
        self.assertEqual(format_city_country("paris", "france"), "Paris, France")
        self.assertEqual(format_city_country("moscow", "russia"), "Moscow, Russia")
        self.assertEqual(format_city_country("london", "united kingdom"), "London, United Kingdom")
        self.assertEqual(format_city_country("new york", "united states"), "New York, United States")
        
    def test_format_city_country_with_population(self):
        # Тестирование с указанием населения
        self.assertEqual(format_city_country("paris", "france", 2_148_000), "Paris, France - population 2148000")
        self.assertEqual(format_city_country("moscow", "russia", 12_537_000), "Moscow, Russia - population 12537000")
        self.assertEqual(format_city_country("london", "united kingdom", 8_982_000), "London, United Kingdom - population 8982000")
        self.assertEqual(format_city_country("new york", "united states", 8_336_817), "New York, United States - population 8336817")        

if __name__ == '__main__':
    unittest.main()
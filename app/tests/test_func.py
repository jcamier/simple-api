import unittest

from app.models.utils import kelvin_to_fahrenheit  # Adjust the import path as needed

class TestUtils(unittest.TestCase):
    def test_kelvin_to_fahrenheit_freezing_point(self):
        # Test the conversion of the freezing point of water from Kelvin to Fahrenheit
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32, places=2)

    def test_kelvin_to_fahrenheit_boiling_point(self):
        # Test the conversion of the boiling point of water from Kelvin to Fahrenheit
        self.assertAlmostEqual(kelvin_to_fahrenheit(373.15), 212, places=2)

    def test_kelvin_to_fahrenheit_random_value(self):
        # Test conversion of a random Kelvin value to Fahrenheit
        self.assertAlmostEqual(kelvin_to_fahrenheit(300), 80.33, places=2)

if __name__ == '__main__':
    unittest.main()

import unittest

from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

from conversions_refactored import (
    convert,
    ConversionNotPossibleException
)


class TestTemperatureConversions(unittest.TestCase):

    def test_celsius_to_kelvin(self):
        test_cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-40.0, 233.15),
            (25.0, 298.15),
            (300.0, 573.15)
        ]

        for celsius, expected in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print("Celsius to Kelvin:", celsius, "->", result)
            self.assertAlmostEqual(result, expected, places=2)

    def test_celsius_to_fahrenheit(self):
        test_cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (25.0, 77.0),
            (300.0, 572.0)
        ]

        for celsius, expected in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print("Celsius to Fahrenheit:", celsius, "->", result)
            self.assertAlmostEqual(result, expected, places=2)

    def test_fahrenheit_to_celsius(self):
        test_cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (77.0, 25.0),
            (572.0, 300.0)
        ]

        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            print("Fahrenheit to Celsius:", fahrenheit, "->", result)
            self.assertAlmostEqual(result, expected, places=2)

    def test_fahrenheit_to_kelvin(self):
        test_cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (77.0, 298.15),
            (572.0, 573.15)
        ]

        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            print("Fahrenheit to Kelvin:", fahrenheit, "->", result)
            self.assertAlmostEqual(result, expected, places=2)

    def test_kelvin_to_celsius(self):
        test_cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (233.15, -40.0),
            (298.15, 25.0),
            (573.15, 300.0)
        ]

        for kelvin, expected in test_cases:
            result = convertKelvinToCelsius(kelvin)
            print("Kelvin to Celsius:", kelvin, "->", result)
            self.assertAlmostEqual(result, expected, places=2)

    def test_kelvin_to_fahrenheit(self):
        test_cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (233.15, -40.0),
            (298.15, 77.0),
            (573.15, 572.0)
        ]

        for kelvin, expected in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            print("Kelvin to Fahrenheit:", kelvin, "->", result)
            self.assertAlmostEqual(result, expected, places=2)


class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertAlmostEqual(convert("C", "F", 300), 572.0, places=2)
        self.assertAlmostEqual(convert("C", "K", 300), 573.15, places=2)
        self.assertAlmostEqual(convert("F", "C", 572), 300.0, places=2)
        self.assertAlmostEqual(convert("F", "K", 572), 573.15, places=2)
        self.assertAlmostEqual(convert("K", "C", 573.15), 300.0, places=2)
        self.assertAlmostEqual(convert("K", "F", 573.15), 572.0, places=2)

    def test_distance_conversions(self):
        self.assertAlmostEqual(convert("MI", "Y", 1), 1760.0, places=2)
        self.assertAlmostEqual(convert("Y", "MI", 1760), 1.0, places=2)
        self.assertAlmostEqual(convert("MI", "M", 1), 1609.344, places=2)
        self.assertAlmostEqual(convert("M", "MI", 1609.344), 1.0, places=2)
        self.assertAlmostEqual(convert("Y", "M", 1), 0.9144, places=4)
        self.assertAlmostEqual(convert("M", "Y", 0.9144), 1.0, places=2)

    def test_same_unit_conversions(self):
        self.assertEqual(convert("C", "C", 25), 25.0)
        self.assertEqual(convert("F", "F", 75), 75.0)
        self.assertEqual(convert("K", "K", 300), 300.0)
        self.assertEqual(convert("MI", "MI", 5), 5.0)
        self.assertEqual(convert("Y", "Y", 10), 10.0)
        self.assertEqual(convert("M", "M", 20), 20.0)

    def test_incompatible_conversions(self):
        with self.assertRaises(ConversionNotPossibleException):
            convert("C", "M", 25)

        with self.assertRaises(ConversionNotPossibleException):
            convert("MI", "C", 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
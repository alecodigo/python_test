import unittest
import src.calculator as calc

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert calc.sum(2, 3) == 5 ; 'Prueba fallida'

    def test_subtract(self):
        assert calc.subtract(5, 3) == 2; 'Prueba fallida'

    def test_multiply(self):
        assert calc.multiply(5, 3) == 15; 'Prueba fallida'

    def test_divide(self):
        expected = 1
        result = calc.divide(5, 5)
        print('result ', result)
        assert  result == expected; 'Prueba fallida'

    def test_divide_por_zero(self):
        with self.assertRaises(ValueError):
            calc.divide(5, 0)
            
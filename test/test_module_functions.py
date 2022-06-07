import unittest
from calculator import main


def button_press_simulated(*args):
    for value in args:
        try:
            main.button_press(value)
        except AttributeError:
            pass


class TestModuleFunctions(unittest.TestCase):

    def tearDown(self):
        main.equation_calculation = ''
        main.equation_text = ''

    def test_function_button_press_1(self):
        """Testing the button_press function"""
        button_press_simulated('2', '**', '3')

        self.assertEqual(main.equation_text, '2^3')
        self.assertEqual(main.equation_calculation, '2**3')

    def test_function_button_press_2(self):
        """Testing the button_press function"""
        button_press_simulated('2', '*', '3')

        self.assertEqual(main.equation_text, '2x3')
        self.assertEqual(main.equation_calculation, '2*3')

    def test_function_clear(self):
        """Testing the clear function"""
        button_press_simulated('2', '*', '3')

        try:
            main.clear()
        except AttributeError:
            pass
        self.assertEqual(main.equation_text, '')
        self.assertEqual(main.equation_calculation, '')

    def test_function_equal_1(self):
        """Testing the equal function if it returns the correct expected output"""
        button_press_simulated('2', '*', '3')

        try:
            main.equal()
        except AttributeError:
            pass
        self.assertEqual(main.equation_calculation, '6')

    def test_function_equal_2(self):
        """Testing the equal function when there's a syntax error in the input"""
        button_press_simulated('/', '*', '+')

        try:
            main.equal()
        except AttributeError:
            pass
        self.assertEqual(main.equation_calculation, '/*+')

    def test_function_equal_3(self):
        """Testing the equal function when the input includes dividing by 0"""
        button_press_simulated('3', '/', '0')

        try:
            main.equal()
        except AttributeError:
            pass
        self.assertEqual(main.equation_calculation, '3/0')

    def test_function_backspace(self):
        """Testing the backspace function"""
        button_press_simulated('2', '**', '3')

        try:
            main.backspace()
        except AttributeError:
            pass
        self.assertTrue(main.equation_calculation, '2**')

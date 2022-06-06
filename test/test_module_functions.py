import unittest
from calculator import main


class TestModuleFunctions(unittest.TestCase):

    def tearDown(self):
        main.equation_calculation = ''
        main.equation_text = ''

    def test_button_press_1(self):
        try:
            main.button_press('2')
        except AttributeError:
            pass

        try:
            main.button_press('**')
        except AttributeError:
            pass

        try:
            main.button_press('3')
        except AttributeError:
            pass

        self.assertEqual(main.equation_text, '2^3')
        self.assertEqual(main.equation_calculation, '2**3')

    def test_button_press_2(self):
        try:
            main.button_press('2')
        except AttributeError:
            pass

        try:
            main.button_press('*')
        except AttributeError:
            pass

        try:
            main.button_press('3')
        except AttributeError:
            pass

        self.assertEqual(main.equation_text, '2x3')
        self.assertEqual(main.equation_calculation, '2*3')

    def test_button_clear(self):
        try:
            main.button_press('2')
        except AttributeError:
            pass

        try:
            main.button_press('*')
        except AttributeError:
            pass

        try:
            main.button_press('3')
        except AttributeError:
            pass

        try:
            main.clear()
        except AttributeError:
            pass
        self.assertEqual(main.equation_text, '')
        self.assertEqual(main.equation_calculation, '')

    def test_function_equal(self):
        try:
            main.button_press('2')
        except AttributeError:
            pass

        try:
            main.button_press('*')
        except AttributeError:
            pass

        try:
            main.button_press('3')
        except AttributeError:
            pass

        try:
            main.equal()
        except AttributeError:
            pass
        self.assertEqual(main.equation_calculation, '6')

    def test_function_backspace(self):
        try:
            main.button_press('2')
        except AttributeError:
            pass

        try:
            main.button_press('**')
        except AttributeError:
            pass

        try:
            main.button_press('3')
        except AttributeError:
            pass

        try:
            main.backspace()
        except AttributeError:
            pass
        self.assertTrue(main.equation_calculation, '2**')

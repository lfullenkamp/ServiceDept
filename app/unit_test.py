from random import choice
from string import ascii_letters, digits
from unittest import TestCase

# Strings to test input
random_string = ''.join(choice(ascii_letters) for x in range(10))
random_numbers = ''.join(choice(digits) for y in range(10))
random_digit = ''.join(choice(digits) for z in range(1))


# Prevents inputs that only contain spaces from being entered into the database
def check_input(test_input):
    if not test_input or len(test_input) == 0 or test_input.isspace():
        return False
    else:
        return True


class IndexTest(TestCase):
    # Tests the check_input function
    def test_check_input(self):
        # Assert that normal input will be entered into the database
        self.assertTrue(check_input(random_string))
        self.assertTrue(check_input(random_digit))
        self.assertTrue(check_input(random_numbers))
        print('check_input() TRUE test -> PASSED' + '\n')
        # Assert that null or empty spaces alone will not be entered into the database
        self.assertFalse(check_input(''))
        print('check_input() Empty Input test -> PASSED' + '\n')
        self.assertFalse(check_input(' '))
        print('check_input() Space Input test -> PASSED' + '\n')

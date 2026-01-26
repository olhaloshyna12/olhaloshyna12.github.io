#Module 10 exercise was completed during an in-class seminar
#Test-Driven Development (TDD) – Calculator and String Processing Examples
#Test-Driven Development Examples
# Creating a simple calculator

# Red: failing test
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(a=2, b=3), 5)

# Green: write minimal code for implementation
class Calculator:
    def add(self, a, b):
        return a + b
#Two numbers comma-separated returns sum
# Red:
def test_two_numbers(self):
    calc = StringCalculator()
    self.assertEqual(calc.add("1,2"), 3)
    self.assertEqual(calc.add("10,20"), 30)

# Green:
class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0

        if "," in numbers:
            num1, num2 = numbers.split(",")
            return int(num1) + int(num2)

        return int(numbers)

# Refactor:
class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0

        if "," in numbers:
            num1, num2 = numbers.split(",")
            return int(num1) + int(num2)

        return int(numbers)
#Handle unknown amount of numbers
# Red
def test_unknown_amount_of_numbers_returns_sum(self):
    calc = StringCalculator()
    self.assertEqual(calc.add("1,2,3"), 6)
    self.assertEqual(calc.add("1,2,3,4,5"), 15)

# Green
class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0

        numbers_list = numbers.split(",")
        total = 0
        for num in numbers_list:
            total += int(num)

        return total

# Refactor
class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0

        numbers_list = numbers.split(",")
        return sum(int(num) for num in numbers_list)
#Testing a simple function in isolation
def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(a=2, b=3) == 5
    assert add_numbers(a=-1, b=1) == 0
    assert add_numbers(a=0, b=0) == 0
#Basic Calculator Application with unittest
import unittest
from Seminar_6_py_calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        calc = Calculator()
        result = calc.add(a=2, b=3)
        self.assertEqual(result, 5)

class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == "__main__":
    unittest.main()
import unittest
from task4 import calculate

class TesterClass(unittest.TestCase):
	def test_arguments(self):
		result = calculate(5, 1, 7)
		self.assertEqual(result, 13)

	def test_diff_arguments(self):
		result = calculate(1, 'two', 3, 'four', 5)
		self.assertEqual(result, 9)

	def test_diff_arguments_2(self):
		input_data = [(5, 3, 1), 5.7, 'thirteen', 10, {1: 10}]
		result = calculate(*input_data)
		self.assertEqual(result, 15.7)

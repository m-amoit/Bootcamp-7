
'''test suite for super_sum'''
from unittest import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):
	'''Test Case for super_sum'''
	
	def test_empty_input(self):
		'''Test empty input.'''
		self.assertEqual(super_sum(), 0)

	def test_sum_of_integers(self):
		''' '''
		self.assertEqual(super_sum(2, 3), 5)
		self.assertEqual(super_sum(-1, 1), 0)

	def test_string_in_input_returns(self):
		''''''
		self.assertEqual(super_sum('string', 1, 4), 0)

	def test_sum_of_items_in_one_list(self):
		'''Test sum of items in a single list'''
		self.assertEqual(super_sum([1, 2, 3]), 6)



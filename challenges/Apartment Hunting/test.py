import unittest
from solution_1 import apartmentHunting as solution_1_apartmentHunting
from solution_2 import apartmentHunting as solution_2_apartmentHunting

class TestApartmentHunting(unittest.TestCase):
    def test_solution_1(self):
        # Test case for solution 1
        blocks = [
            {'gym': False, 'school': True, 'store': False},
            {'gym': True, 'school': False, 'store': False},
            {'gym': True, 'school': True, 'store': False},
            {'gym': False, 'school': True, 'store': False},
            {'gym': False, 'school': True, 'store': True},
        ]
        reqs = ['gym', 'school', 'store']

        result = solution_1_apartmentHunting(blocks, reqs)
        expected_result = 3
        self.assertEqual(result, expected_result)

    def test_solution_2(self):
        # Test case for somution 2
        blocks = [
            {'gym': False, 'school': True, 'store': False},
            {'gym': True, 'school': False, 'store': False},
            {'gym': True, 'school': True, 'store': False},
            {'gym': False, 'school': True, 'store': False},
            {'gym': False, 'school': True, 'store': True},
        ]
        reqs = ['gym', 'school', 'store']

        result = solution_2_apartmentHunting(blocks, reqs)
        expected_result = 3
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
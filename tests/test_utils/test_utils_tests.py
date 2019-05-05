import unittest
import tests.test_utils.utils_tests as utils


class TestUtilsTest(unittest.TestCase):

    def test_utils_compare_two_dicts_returns_False_when_lists_are_different(self):
        dict1 = {'dogs': ['Dachshund', 'Alsacian'],
                 'cats': ["Egyptian"],
                 'hamsters': ['big', 'small']}
        dict2 = {'dogs': ['Dachshund', 'Alsacian']}
        response = utils.compare_two_lists(dict1, dict2)
        self.assertFalse(response)

    def test_utils_compare_two_dicts_are_the_same_despite_different_order_of_keys_and_values(self):
        dict1 = {'dogs': ['Alsacian', 'Dachshund'],
                 'hamsters': ['small', 'big'],
                 'cats': ["Egyptian"]}
        dict2 = {'hamsters': ['big', 'small'],
                 'cats': ["Egyptian"],
                 'dogs': ['Dachshund', 'Alsacian']}
        response = utils.compare_two_lists(dict1, dict2)
        self.assertTrue(response)

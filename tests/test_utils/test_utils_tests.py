import unittest
import tests.test_utils.utils_tests as utils


class TestUtilsTest(unittest.TestCase):

    def test_utils_compare_two_dicts_returns_False_when_lists_are_different(self):
        dict1 = {'dogs': ['Dachshund', 'Alsacian'],
                 'cats': ["Egyptian"],
                 'hamsters': ['big', 'small']}
        dict2 = {'dogs': ['Dachshund', 'Alsacian']}
        response = utils.compare_two_dicts(dict1, dict2)
        self.assertFalse(response)

    def test_utils_compare_two_dicts_are_the_same_despite_different_order_of_keys_and_values(self):
        dict1 = {'dogs': ['Alsacian', 'Dachshund'],
                 'hamsters': ['small', 'big'],
                 'cats': ["Egyptian"]}
        dict2 = {'hamsters': ['big', 'small'],
                 'cats': ["Egyptian"],
                 'dogs': ['Dachshund', 'Alsacian']}
        response = utils.compare_two_dicts(dict1, dict2)
        self.assertTrue(response)

    def test_utils_strings_are_turned_into_a_list_and_stripped_of_escape_expressions(self):
        content1 = "      , Beth, Stuart\n Beth, Chris\nPaul, Chris, Beth\n\t\t           , Chris"
        content2 = "\t\tPhil, Edward, Liz\nLiz, \tEdward\n\tEdward, Stephen, Phil"
        content1_as_list = utils.turn_string_into_list_stripped_off_escape_expressions_and_commas(content1)
        content2_as_list = utils.turn_string_into_list_stripped_off_escape_expressions_and_commas(content2)
        expected_content1 = ['', 'Beth', 'Stuart', 'Beth', 'Chris', 'Paul', 'Chris', 'Beth', '', 'Chris']
        expected_content2 = ['Phil', 'Edward', 'Liz', 'Liz', 'Edward', 'Edward', 'Stephen', 'Phil']
        self.assertEqual(content1_as_list, expected_content1)
        self.assertEqual(content2_as_list, expected_content2)

    def test_utils_strings_can_be_turned_into_an_appropriate_dict_with_players_and_other_players_they_can_see(self):
        content = "\t\tPhil, Edward, Liz\nLiz, \tEdward, James, Adam\n\tEdward, Stephen, Phil\nAdam, James"
        expected_dict = {
                        "Phil": ["Edward", "Liz"],
                        "Liz": ["Edward", "James", "Adam"],
                        "Edward": ["Stephen", "Phil"],
                        "Adam": ["James"]
                        }
        result = utils.turn_string_into_dict_stripped_off_excape_expressions_and_commas(content)
        result_of_comparing_two_dicts = utils.compare_two_dicts(expected_dict, result)
        self.assertTrue(result_of_comparing_two_dicts)

import unittest
from src.format_validator import FormatValidator
from src.player_file_reader import PlayersFileReader
from tests.test_utils.utils_tests import turn_string_into_list_stripped_off_escape_expressions_and_commas, \
    clear_the_content_of_the_desired_file, write_some_content_in_the_desired_file


class LineFormatValidatorTest(unittest.TestCase):

    def setUp(self):
        self.format_validator = FormatValidator()
        self.file_reader = PlayersFileReader()
        self.path_to_players_files = '../resources/players_files/'
        self.players_file = self.path_to_players_files + 'players.txt'
        self.content_to_write = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"

    def test_file_reader_identifies_the_names_of_the_main_players_are_blank(self):
        content = "      , Beth, Stuart\n Beth, Chris\nPaul, Chris, Beth\n\t\t           , Chris"
        content_as_list = turn_string_into_list_stripped_off_escape_expressions_and_commas(content)
        exp_result = '\n................................................................................'\
                     '\nTHE NAME OF PLAYERS CANNOT BE BLANK! PLEASE REPLACE THE BLANK SPACES BEFORE THE FIRST COMMA' \
                     '\nWITH A NAME TYPED IN ALPHANUMERICS e.g. StuartTheLittle, Jess1 or Phoebe112' \
                     '\n................................................................................'
        with self.assertRaises(ValueError) as error:
            self.format_validator.check_the_line_does_not_have_intentional_empty_entries(content_as_list)
        self.assertEqual(str(error.exception), exp_result)

    def test_file_reader_identifies_the_names_of_the_name_players_are_ok(self):
        content = "\t\tPhil, Edward, Liz\nLiz, \tEdward\n\tEdward, Stephen, Phil"
        content_as_list = turn_string_into_list_stripped_off_escape_expressions_and_commas(content)
        result = self.format_validator.check_the_line_does_not_have_intentional_empty_entries(content_as_list)
        self.assertEqual(result, True)

    def test_there_cannot_be_two_or_more_players_defined_with_the_same_names(self):
        content = "Chris, Beth, Stuart\n Beth, Chris\nBeth, Chris, Steph\n\t\tStuart, Chris"
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content)
        gained_dict = self.file_reader.turn_the_file_into_dict(self.players_file)
        exp_result = '\n................................................................................'\
                     '\nTHERE CANNOT BE TWO PLAYERS WITH THE SAME NAMES' \
                     '\nCHANGE THE NAMES OF DUPLICATED PLAYERS' \
                     '\n................................................................................'
        with self.assertRaises(ValueError) as error:
            self.format_validator.check_the_file_does_not_contain_the_same_player_names(content, gained_dict)
        self.assertEqual(str(error.exception), exp_result)

    def test_the_validator_recognizes_if_a_dict_does_not_consist_of_players_with_similar_names(self):
        content = "Chris, Beth, Stuart\n Becky, Chris\nBeth, Chris, Beth\n\t\tStuart, Chris\nIsis, Chris, Stuart"
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content)
        gained_dict = self.file_reader.turn_the_file_into_dict(self.players_file)
        result = self.format_validator.check_the_file_does_not_contain_the_same_player_names(content, gained_dict)
        self.assertEqual(result, True)
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, self.content_to_write)

    # #the names of players can't contain non alphanumeric characters
    # content3 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"
    # #only commas act as separators
    # content4 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"
    # #other escaping commands are ignored and trigger errors - only \n is accepted
    # content5 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"

if __name__ == '__main__':
    unittest.main()

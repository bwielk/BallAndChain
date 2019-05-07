import unittest
from src.max_number_of_players_calculator import CalculatorMaxNumOfPlayersTouchingABall
from src.format_validator import FormatValidator
from src.player_file_reader import PlayersFileReader
from tests.test_utils.utils_tests import write_some_content_in_the_desired_file, clear_the_content_of_the_desired_file


class MaxNumberOfPlayersCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorMaxNumOfPlayersTouchingABall()
        self.file_reader = PlayersFileReader()
        self.format_validator = FormatValidator()
        self.path_to_players_files = '../resources/players_files/'
        self.players_file = self.path_to_players_files + 'players.txt'
        self.content_to_write = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"

    def test_max_players_calculator_works_for_standard_entries_when_processing_single_file_with_result_3(self):
        content_to_write = 'George, Beth,  Sue\nRick, Anne\nAnne, Beth\nBeth, Anne, George\nSue, Beth'
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content_to_write)
        result = self.calculator.calculate_max_number_of_players_touching_a_ball(file=self.players_file)
        self.assertEqual(3, result)

    def test_max_players_calculator_works_for_standard_entries_when_processing_single_file_with_result_5(self):
        content_to_write = 'Adam, \t\tDominic,  Rob,\tIsla' \
                           '\nIsla, Adam' \
                           '\nDominic, \t       Tessy, Rob' \
                           '\nRob,         Adam,   \tDominic' \
                           '\nTessy,           Dominic' \
                           '\nBlaise, Adam'
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content_to_write)
        result = self.calculator.calculate_max_number_of_players_touching_a_ball(file=self.players_file)
        self.assertEqual(5, result)

    def test_max_players_calculator_works_for_standard_entries_when_processing_single_file_with_result_6(self):
        content_to_write = 'Harry,            Hermione,  Cedric' \
                           '\nHermione, Cedric           , Malfoy' \
                           '\nCedric,   Harry, \t Lily' \
                           '\nMalfoy,         Cedric,\t\tPeter' \
                           '\nLily,           Cedric' \
                           '\nPeter, Hermione, Malfoy,Queenie' \
                           '\nQueenie,         Peter, Malfoy'
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content_to_write)
        result = self.calculator.calculate_max_number_of_players_touching_a_ball(file=self.players_file)
        self.assertEqual(6, result)

    def test_max_players_calculator_returns_an_error_when_there_are_players_with_two_similar_names(self):
        content_to_write = 'Malfoy,            Hermione,  Cedric' \
                           '\nHermione, Cedric           , Malfoy' \
                           '\nCedric,   Harry, \t Lily' \
                           '\nMalfoy,         Cedric,\t\tPeter' \
                           '\nLily,           Cedric' \
                           '\nCedric, Hermione, Malfoy,Queenie' \
                           '\nQueenie,         Peter, Malfoy'
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content_to_write)
        exp_result = '\n................................................................................' \
                     '\nTHERE CANNOT BE TWO PLAYERS WITH THE SAME NAMES' \
                     '\nCHANGE THE NAMES OF DUPLICATED PLAYERS' \
                     '\n................................................................................'
        with self.assertRaises(ValueError) as error:
            self.calculator.calculate_max_number_of_players_touching_a_ball(file=self.players_file)
        self.assertEqual(str(error.exception), exp_result)

    def test_max_players_calculator_returns_an_error_when_there_are_empty_spaces_instead_of_names_in_the_file(self):
        content_to_write = ' ,            Hermione,  Cedric' \
                           '\nHermione, Cedric           , Malfoy' \
                           '\nCedric,   Harry, \t Lily' \
                           '\n      ,         Cedric,\t\tPeter' \
                           '\n      ,           Cedric' \
                           '\n     , Hermione, Malfoy,Queenie' \
                           '\nQueenie,         Peter, Malfoy'
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content_to_write)
        exp_result = '\n................................................................................' \
                     '\nTHE NAME OF PLAYERS CANNOT BE BLANK! PLEASE REPLACE THE BLANK SPACES ' \
                     'BEFORE THE FIRST COMMA' \
                     '\nWITH A NAME TYPED IN ALPHANUMERICS e.g. StuartTheLittle, Jess1 or Phoebe112' \
                     '\n................................................................................'
        with self.assertRaises(ValueError) as error:
            self.calculator.calculate_max_number_of_players_touching_a_ball(file=self.players_file)
        self.assertEqual(str(error.exception), exp_result)

    def test_max_players_calculator_returns_an_error_when_the_players_file_is_empty(self):
        content_to_write = ''
        clear_the_content_of_the_desired_file(self.players_file)
        write_some_content_in_the_desired_file(self.players_file, content_to_write)
        exp_result = '................................................................................' \
                     '\nTHE DESIRED FILE IS EMPTY. POPULATE IT WITH DATA AND TRY AGAIN.' \
                     '\nTO POPULATE THE FILE, USE THIS FORMAT: YourPlayer, OtherPlayer1, OtherPlayer2' \
                     '\nUSE ALPHANUMERIC CHARACTERS ONLY!' \
                     '\n...............................................................................'
        with self.assertRaises(ValueError) as error:
            self.calculator.calculate_max_number_of_players_touching_a_ball(file=self.players_file)
        self.assertEqual(str(error.exception), exp_result)


if __name__ == '__main__':
    unittest.main()

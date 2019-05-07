import unittest
import tests.test_utils.utils_tests as utils
from src.player_file_reader import PlayersFileReader
import os

class PlayerFileReaderTest(unittest.TestCase):

    def setUp(self):
        self.file_reader = PlayersFileReader()
        self.path_to_players_files = '../resources/players_files/'
        self.players_file = self.path_to_players_files + 'players.txt'
        self.content_to_write = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"

    def test_program_returns_an_error_message_when_players_file_exists_but_its_empty(self):
        utils.clear_the_content_of_the_desired_file(self.players_file)
        exp_message = '................................................................................' \
                      '\nMAKE SURE THE FILES IN THE /resources/players_file DIRECTORY have any data in them'\
                      '\nFollow the following format for putting data in the files'\
                      '\nMyPlayer, OtherPlayer1, OtherPlayer2, OtherPlayer3 - names should be in'\
                      ' alphanumerics only'\
                      '\n...............................................................................'
        with self.assertRaises(ValueError) as error:
            self.file_reader.read_the_content_of_the_file_and_return_it_as_list(self.players_file)
        self.assertEqual(str(error.exception), exp_message)
        utils.write_some_content_in_the_desired_file(self.players_file, self.content_to_write)

    def test_file_reader_detects_an_existing_text_file_with_players_config(self):
        result = self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        self.assertTrue(result)

    def test_file_reader_detects_that_in_the_dir_are_files_that_are_not_named_correctly(self):
        utils.create_num_of_random_files(10, self.path_to_players_files)
        #result = self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        exp_message =  '................................................................................' \
                       '\nPLEASE, DOUBLE CHECK THE NAMES AND EXTENSIONS IN THE RESOURCES DIRECTORY.' \
                       '\nThe required documents with players details should have thee word "player" in their names' \
                       '\nand be of .txt extension. Please correct the mistakes and rerun the program' \
                       '\n...............................................................................'
        with self.assertRaises(ValueError) as error:
            self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        self.assertEqual(str(error.exception), exp_message)
        utils.delete_num_of_randomly_create_files(10, self.path_to_players_files)

    def test_file_reader_detects_that_in_the_players_files_dir_are_files_with_incorrect_extensions(self):
        desired_format = "csv"
        temp_file_name = "players_setup"
        utils.create_num_of_random_files(5, self.path_to_players_files,
                                         desired_extension=desired_format, file_name=temp_file_name)
        exp_message = '................................................................................'\
                      '\nPLEASE, DOUBLE CHECK THE NAMES AND EXTENSIONS IN THE RESOURCES DIRECTORY.'\
                      '\nThe required documents with players details should have thee word "player" in their names'\
                      '\nand be of .txt extension. Please correct the mistakes and rerun the program'\
                      '\n...............................................................................'
        with self.assertRaises(ValueError) as error:
            self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        self.assertEqual(str(error.exception), exp_message)
        utils.delete_num_of_randomly_create_files(5, self.path_to_players_files, desired_extension=desired_format,
                                                  file_name=temp_file_name)

    def test_file_reader_realises_the_players_file_is_empty_and_returns_appropriate_message(self):
        players_txt_file = self.path_to_players_files + 'players.txt'
        utils.clear_the_content_of_the_desired_file(players_txt_file)
        len_of_content_in_the_players_file = os.stat(players_txt_file).st_size
        self.assertEqual(0, len_of_content_in_the_players_file)
        exp_message = '................................................................................'\
                      '\nTHE DESIRED FILE IS EMPTY. POPULATE IT WITH DATA AND TRY AGAIN.'\
                      '\nTO POPULATE THE FILE, USE THIS FORMAT: YourPlayer, OtherPlayer1, OtherPlayer2'\
                      '\nUSE ALPHANUMERIC CHARACTERS ONLY!'\
                      '\n...............................................................................'
        with self.assertRaises(ValueError) as error:
            self.file_reader.turn_the_file_into_dict(players_txt_file)
        self.assertEqual(str(error.exception), exp_message)
        utils.write_some_content_in_the_desired_file(players_txt_file, self.content_to_write)

    def test_file_reader_does_not_return_the_error_message_when_the_file_is_populated(self):
        players_txt_file = self.path_to_players_files + 'players.txt'
        response = self.file_reader.turn_the_file_into_dict(players_txt_file)
        self.assertTrue(type(response) == dict)

    def test_file_is_correctly_read_by_player_filer_reader(self):
        players_txt_file = self.path_to_players_files + 'players.txt'
        utils.clear_the_content_of_the_desired_file(players_txt_file)
        utils.write_some_content_in_the_desired_file(players_txt_file, self.content_to_write)
        read_content_of_the_desired_file = \
            self.file_reader.read_the_content_of_the_file_and_return_it_as_list(players_txt_file)
        found_content = ''.join(read_content_of_the_desired_file)
        self.assertEqual(found_content, self.content_to_write)

    def test_file_reader_turns_content_into_the_dictionary(self):
        players_txt_file = self.path_to_players_files + 'players.txt'
        utils.clear_the_content_of_the_desired_file(players_txt_file)
        utils.write_some_content_in_the_desired_file(players_txt_file, self.content_to_write)
        dict_of_players = self.file_reader.turn_the_file_into_dict(players_txt_file)
        expected_dict = {
                            'George': ['Anne', 'Beth'],
                            'Rick': ['Anne', 'Steph'],
                            'Anne': ['Beth'],
                            'Steph': ['George', 'Rick'],
                            'Alex': ['Bob']
                        }
        comparison_result = utils.compare_two_dicts(dict_of_players, expected_dict)
        self.assertTrue(comparison_result)

    def test_file_reader_ignores_empty_lines_in_a_file(self):
        #ignoring empty lines in a file ensures the clarity of the finally returned dict file
        content_with_empty_lines = "\tGeorge, Beth,    Anne\n      \n           \nRick, Anne, Steph        \n     \n" \
                                   "\tAnne, Beth\nSteph, George, Rick\n        \t              \t\t\nAlex, Bob"
        players_txt_file = self.path_to_players_files + 'players.txt'
        utils.clear_the_content_of_the_desired_file(players_txt_file)
        utils.write_some_content_in_the_desired_file(players_txt_file, content_with_empty_lines)
        dict_of_players = self.file_reader.turn_the_file_into_dict(players_txt_file)
        expected_dict = {
            'George': ['Anne', 'Beth'],
            'Rick': ['Anne', 'Steph'],
            'Anne': ['Beth'],
            'Steph': ['George', 'Rick'],
            'Alex': ['Bob']
        }
        comparison_result = utils.compare_two_dicts(dict_of_players, expected_dict)
        self.assertTrue(comparison_result)

    def test_escaping_sequences_are_ignored_by_file_reader(self):
        content_with_empty_lines = "\tGeorge, Beth, \f  \f Anne" \
                                   "\n      " \
                                   "\n           " \
                                   "\nRick, Anne,    \v Steph        " \
                                   "\n     " \
                                   "\n\tAnne,     Beth\r" \
                                   "\nSteph, George, Rick" \
                                   "\n        \t              \t\t\nAlex, \vBob"
        players_txt_file = self.path_to_players_files + 'players.txt'
        utils.clear_the_content_of_the_desired_file(players_txt_file)
        utils.write_some_content_in_the_desired_file(players_txt_file, content_with_empty_lines)
        dict_of_players = self.file_reader.turn_the_file_into_dict(players_txt_file)
        print(dict_of_players)
        expected_dict = {
            'George': ['Anne', 'Beth'],
            'Rick': ['Anne', 'Steph'],
            'Anne': ['Beth'],
            'Steph': ['George', 'Rick'],
            'Alex': ['Bob']
        }
        comparison_result = utils.compare_two_dicts(dict_of_players, expected_dict)
        self.assertTrue(comparison_result)

    def test_appropriate_message_is_returned_when_desired_file_is_not_found(self):
        absolute_path = os.path.abspath('../resources/players_files/players.txt')
        os.remove(absolute_path)
        exp_result = '................................................................................'\
                     '\nTHERE ARE NO FILES IN THE DESIRED DIRECTORY %s' \
                     '\nCREATE A FILE e.g. players.txt' % self.path_to_players_files
        with self.assertRaises(ValueError) as error:
            self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        self.assertEqual(str(error.exception), exp_result)
        utils.write_some_content_in_the_desired_file(self.players_file, self.content_to_write)


if __name__ == '__main__':
    unittest.main()

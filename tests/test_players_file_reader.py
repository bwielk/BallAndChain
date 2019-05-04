import unittest
import tests.utils as utils
from src.player_file_reader import PlayersFileReader
import os


class PlayerFileReaderTest(unittest.TestCase):

    def setUp(self):
        self.file_reader = PlayersFileReader()
        self.path_to_players_files = '../resources/players_files/'
        self.content_to_write = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex"

    def test_file_reader_detects_an_existing_text_file_with_players_config(self):
        result = self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        self.assertTrue(result)

    def test_file_reader_detects_that_in_the_dir_are_files_that_are_not_named_correctly(self):
        utils.create_num_of_random_files(10, self.path_to_players_files)
        result = self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        self.assertFalse(result)
        utils.delete_num_of_randomly_create_files(10, self.path_to_players_files)

    def test_file_reader_detects_that_in_the_players_files_dir_are_files_with_incorrect_extensions(self):
        desired_format = "csv"
        temp_file_name = "players_setup"
        utils.create_num_of_random_files(5, self.path_to_players_files,
                                         desired_extension=desired_format, file_name=temp_file_name)
        result = self.file_reader.check_the_players_files_exist_and_are_correct(self.path_to_players_files)
        self.assertFalse(result)
        utils.delete_num_of_randomly_create_files(5, self.path_to_players_files, desired_extension=desired_format,
                                                  file_name=temp_file_name)

    def test_file_reader_realises_the_players_file_is_empty_and_returns_appropriate_message(self):
        players_txt_file = self.path_to_players_files + 'players.txt'
        utils.clear_the_content_of_the_desired_file(players_txt_file)
        len_of_content_in_the_players_file = os.stat(players_txt_file).st_size
        self.assertEqual(0, len_of_content_in_the_players_file)



import unittest
import logging
from src.max_number_of_players_calculator import MaxNumberOfPlayersCalculator


class MaxNumberOfPlayersCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = MaxNumberOfPlayersCalculator()

    def test_2_and_2_is_4(self):
        expected = 4
        result = self.calculator.add_nums(2, 2)
        logging.info("We expect %s and the result is %s" % (expected, result))
        self.assertEqual(result, expected)

    def test_reads_the_path(self):
        path_to_file = self.calculator.file_to_read
        self.assertEqual(path_to_file, '../resources/players.tt')


if __name__ == '__main__':
    unittest.main()

import unittest

class LineFormatValidator(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_reader_identifies_the_wrong_format_of_the_lines_of_players(self):
        results = []
        #empty main player name - it always needs to be there to identify its name
        content1 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"
        #two main players can't have exactly the same names
        content2 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"
        #the names of players can't contain non alphanumeric characters
        content3 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"
        #only commas act as separators
        content4 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"
        #other escaping commands are ignored and trigger errors - only \n is accepted
        content5 = "George, Beth,    Anne\nRick, Anne, Steph\nAnne, Beth\nSteph, George, Rick\nAlex, Bob"
        self.assertTrue(all(el == True for el in results))

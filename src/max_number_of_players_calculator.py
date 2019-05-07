from src.player_file_reader import PlayersFileReader
from src.format_validator import FormatValidator

class CalculatorMaxNumOfPlayersTouchingABall:

    file_to_read = None

    def __init__(self):
        self.file_to_read = './/resources//players_files//players.txt'


    def calculate_max_number_of_players_touching_a_ball(self, file=file_to_read):
        results = []
        file_reader = PlayersFileReader()
        format_validator = FormatValidator()
        dict_of_players = file_reader.turn_the_file_into_dict(file)
        content = None
        with open(self.file_to_read, 'r') as f:
            content = f.read()
        format_validator.check_the_file_does_not_contain_the_same_player_names(content, dict_of_players)
        for k in dict_of_players.keys():
            for value in dict_of_players[k]:
                try:
                    if k in dict_of_players[value]:
                        results.append(k)
                except KeyError:
                    pass
        results = set(results)
        print("FOUND NAMES: %s" % str(results))
        return len(results)





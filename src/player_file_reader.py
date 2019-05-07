import os
from src.format_validator import FormatValidator

class PlayersFileReader:

    def __init__(self):
        self.format_validator = FormatValidator()

    def turn_the_file_into_dict(self, path_to_file):

        try:
            if os.stat(path_to_file).st_size == 0:
                raise ValueError('................................................................................'
                                 '\nTHE DESIRED FILE IS EMPTY. POPULATE IT WITH DATA AND TRY AGAIN.'
                                 '\nTO POPULATE THE FILE, USE THIS FORMAT: YourPlayer, OtherPlayer1, OtherPlayer2'
                                 '\nUSE ALPHANUMERIC CHARACTERS ONLY!'
                                 '\n...............................................................................')
        except IOError as e:
            print(e)
        found_content = self.read_the_content_of_the_file_and_return_it_as_list(path_to_file)
        dict_to_process = {}
        for line in found_content:
            if line.strip() == '':
                continue
            else:
                line_content = line.split(',')
                edited_line_content = [el.strip() for el in line_content]
                self.format_validator.check_the_line_does_not_have_intentional_empty_entries(edited_line_content)
                dict_to_process[edited_line_content[0]] = edited_line_content[1:len(edited_line_content)]
        return dict_to_process

    def read_the_content_of_the_file_and_return_it_as_list(self, path_to_file):
        results = []
        with open(path_to_file, 'r') as f:
            for line in f:
                results.append(line)
        if len(results) == 0:
            raise ValueError('................................................................................'
                             '\nMAKE SURE THE FILES IN THE /resources/players_file DIRECTORY have any data in them'
                             '\nFollow the following format for putting data in the files'
                             '\nMyPlayer, OtherPlayer1, OtherPlayer2, OtherPlayer3 - names should be in'
                             ' alphanumerics only'
                             '\n...............................................................................')
        return results

    def check_the_players_files_exist_and_are_correct(self, directory):
        if len(os.listdir(directory)) == 0:
            raise ValueError('................................................................................'
                             '\nTHERE ARE NO FILES IN THE DESIRED DIRECTORY %s'
                             '\nCREATE A FILE e.g. players.txt' % directory)
        result = True
        for file in os.listdir(directory):
            if 'player' in file and file.endswith('.txt'):
                continue
            else:
                raise ValueError('................................................................................'
                                 '\nPLEASE, DOUBLE CHECK THE NAMES AND EXTENSIONS IN THE RESOURCES DIRECTORY.'
                                 '\nThe required documents with players details '
                                 'should have thee word "player" in their names'
                                 '\nand be of .txt extension. Please correct the mistakes and rerun the program'
                                 '\n...............................................................................')
        return result

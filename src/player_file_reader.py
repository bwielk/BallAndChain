import os


class PlayersFileReader:

    def turn_the_file_into_dict(self, path_to_file):
        try:
            if os.stat(path_to_file).st_size == 0:
                print('................................................................................'
                      'THE DESIRED FILE IS EMPTY. POPULATE IT WITH DATA AND TRY AGAIN\n.'
                      'TO POPULATE THE FILE, USE THIS FORMAT: YourPlayer, OtherPlayer1, OtherPlayer2\n'
                      'USE ALPHANUMERIC CHARACTERS ONLY!\n'
                      '...............................................................................')
        except IOError as e:
            print(e)

    def check_the_players_files_exist_and_are_correct(self, directory):
        result = True
        for file in os.listdir(directory):
            if 'player' in file and file.endswith('.txt'):
                continue
            else:
                result = False
                break
        return result



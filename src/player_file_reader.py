import os


class PlayersFileReader:

    def turn_the_file_into_dict(self, path_to_file):
        try:
            if os.stat(path_to_file).st_size == 0:
                return('................................................................................'
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
                key_el = line_content.pop(0).strip()
                edited_line_content = [el.strip() for el in line_content]
                dict_to_process[key_el] = edited_line_content
        return dict_to_process

    def read_the_content_of_the_file_and_return_it_as_list(self, path_to_file):
        results = []
        with open(path_to_file, 'r') as f:
            for line in f:
                results.append(line)
        return results

    def check_the_players_files_exist_and_are_correct(self, directory):
        result = True
        for file in os.listdir(directory):
            if 'player' in file and file.endswith('.txt'):
                continue
            else:
                result = False
                break
        return result

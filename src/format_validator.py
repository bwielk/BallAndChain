class FormatValidator:

    def check_the_line_does_not_have_intentional_empty_entries(self, line_as_list):
        if all(line != '' for line in line_as_list) is True:
            return True
        else:
            raise ValueError('\n................................................................................' 
                             '\nTHE NAME OF PLAYERS CANNOT BE BLANK! PLEASE REPLACE THE BLANK SPACES '
                             'BEFORE THE FIRST COMMA' 
                             '\nWITH A NAME TYPED IN ALPHANUMERICS e.g. StuartTheLittle, Jess1 or Phoebe112' 
                             '\n................................................................................')

    def check_the_file_does_not_contain_the_same_player_names(self, content,  dict_of_players):
        number_of_expected_lines = len(content.split('\n'))
        number_of_individual_players = len(dict_of_players.keys())
        if number_of_individual_players == number_of_expected_lines:
            return True
        else:
            raise ValueError('\n................................................................................'
                             '\nTHERE CANNOT BE TWO PLAYERS WITH THE SAME NAMES'
                             '\nCHANGE THE NAMES OF DUPLICATED PLAYERS'
                             '\n................................................................................')



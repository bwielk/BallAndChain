from src.max_number_of_players_calculator import CalculatorMaxNumOfPlayersTouchingABall

calculator = CalculatorMaxNumOfPlayersTouchingABall()
path = './resources/players_files/players.txt'

print("THE READ FILE: ")
with open(path, 'r') as f:
    for line in f:
        print(line)

print("\n\nThe result for the file %s is %s" %
      (path, calculator.calculate_max_number_of_players_touching_a_ball(file=path)))

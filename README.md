Some players are standing in a field playing a game. If two players can see each other then
they can throw a ball between them.

Write a program to calculate the maximum number of players that can touch a single ball.
The ball can be given to any player at the start, and each player can touch the ball an unlimited number of times.
You are given an input file containing details of the players, as follows:

Each line of the file contains a comma-separated set of fields. The first field on each line is
the name of a player (as a string), and the remaining fields are the names of the players that
that player can see.
Your program should read the input file and print the answer to standard out.
For example, given the following input:

'George, Beth,  Sue
\nRick, Anne
\nAnne, Beth
\nBeth, Anne, George
\nSue, Beth'


The program should print 3. This is because George can see Beth and Beth can see George.
Additionally, Beth can see Anne, and Anne can see Beth. However, despite Rick being able to
see Anne, Anne cannot see Rick, and despite George being able to see Sue, Sue cannot see
George

**RUNNING THE PROGRAM**

To run the program, you need to first go to the resources/players_files/players.txt file and enter some player
name e.g.

Sarah, Stewart \nJessica, Stewart \n   Stewart, Sarah

Then go to the runner.py file and run it - it will read the input and 
return the appropriate error messages or final result.

**RUNNING THE TESTS**

To run the tests, please run them from the ./tests directory (i.e. in Pycharm, 
just right click on the directory and click "Run")
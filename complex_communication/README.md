## Advanced Three Node Communication - Tic-Tac-Toe game via ROS Services
Create a ROS package in your catkin workspace. The package must be named complex_communication and should include three ROS nodes named server, player_1 and player_2. In this task you will simulate a tic-tac-toe game. Server has the table (1x9) stored in memory and the plays of each player. You should: 
Create a custom message which includes the table. This will be published by the server and will be retrieved by the players, by using ROS Services.
The players will change the board by playing (of course the play must be valid) and will send it back to the server, which stores their move and prints the board.
If the game ends, server informs the two players by a different message in order to terminate.
Finally, server prints the result and shuts himself down.
The overall system must initialize with a ROS launcher file

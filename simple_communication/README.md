##  Simple Two Node Message Communication

Create a ROS package in your catkin workspace. The package must be named simple communication and should include two ROS nodes named streamer and manipulator. Streamer must publish a random number of type 
std_msgs::Int16 each second at the /task1/numbers topic. The manipulator node must retrieve the numbers and print their squares.



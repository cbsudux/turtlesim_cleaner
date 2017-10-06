# Turtlesim_cleaner

Hi, this package contains 4 nodes + 2 launch files + 1 shell script that runs the two launch files consecutively. 

# Circle :

1. move_circle_server : ROS Server that makes turtlesim move in a circle.
2. move_circle_client : ROS Client that requests the Server with arguments for speed and radius of Circle.

# Square :

1. move_square_server : ROS Server that makes turtlesim draw squares.
2. move_square_client : ROS Client that request the server with arguments for side lenght and number of rotations.

# Launch Files

1. move_circle.launch : Launches turtlesim + server + client
2. move_square.launch : Launches turtlesim + server + client

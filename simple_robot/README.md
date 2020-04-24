##  A More Realistic Task

We assume that a USAR (Urban Search and Rescue) robot exists in a 10x10 grid, at a random position [x,y]. Our robot contains a thermal sensor which measures the current cell’s temperature at each time (thus the temperature is related to the robot’s pose). In order to simulate the sensor we assume that it provides random measurements, uniformly scattered in the [20,40] C range. These measurements are filtered by a ROS node, assuming a threshold for the existence of human presence (e.g. 37 C). When this threshold is surpassed a victim alert is emitted. You should:

    Create a ROS package for specifying the custom communications, named simple_robot_msgs. The following messages should crafted:
        TemperatureReading.msg: Contains a temperature measurement
        VictimFound.msg: Includes a string with the sensor which identified the victim (“thermal” in our case)
        GetRobotPose.action: Action to retrieve the robot pose at any given time. The goal field will be empty, whereas the result must include two fields (x,y), being the robot’s coordinates. The feedback will also be empty.
    Create a second ROS package in the same catkin workspace named simple_robot. Remember to declare the necessary dependencies (in the package.xml and CMakeLists.txt files), which essentially are the simple_robot_msgs package and the ROS libraries you will utilize (e.g. roscpp, actionlib etc.).

You must create four ROS nodes:

    The ROS node that simulates the thermal sensor. This node must include a ros::publisher that will send messages of type TemperatureReading.msg in the /sensors/temperature topic. This node will create a random value between [20,40] each second and post it in the corresponding topic.
    The ROS node that will filter the information (data_fusion). This node must include a subscriber in the /sensors/temperature topic and a publisher that will send messages of the victim_found.msg type at the /data_fusion/victim_found topic. The subscriber’s callback will check the temperature value and when it surpasses the threshold it will post a message of type victim_found via the publisher, which will include the word “thermal”.
    The ROS node that will provide the pose determination service via a ROS action. The node must include an action_server of type GetRobotPose.action at the /slam/get_robot_pose topic. Its execute callback will fill the action’s result with two random integer values (x,y) in the range [0,9], pointing to the robot’s pose at the moment the action was invoked.
    The ROS node that includes a subscriber at the /victim_found topic and an action_client of GetRobotPose.action type at the /slam/get_robot_pose topic. The respective callback will ask for the robot’s pose each time a victim is found. When the pose is retrieved, the node must print “Victim found! Robot Pose = (<x>, <y>). Sensor used for identification = <sensor>”.

Node: You will have four nodes. This means (for the C++ case) that you must declare four executables in the CMakeLists.txt file.

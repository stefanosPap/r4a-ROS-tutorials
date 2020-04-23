#! /usr/bin/env python3
import rospy
from simple_robot_msgs.msg import GetRobotPoseResult, GetRobotPoseAction
from simple_robot_msgs.msg import VictimFound
import actionlib
def callback(data):
    print(data.victim_sensor)
    if "thermal" in data.victim_sensor: 
        result = pose_client()
        print(result.x)
        print(result.y)
def pose_client():
    client = actionlib.SimpleActionClient('/slam/get_robot_pose', GetRobotPoseAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = 1
    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

def listener():
        rospy.Subscriber("/data_fusion/victim_found", VictimFound, callback)
        rospy.spin()
if __name__ == '__main__':
    try:
        rospy.init_node('pose_client')
        listener()
    except rospy.ROSInterruptException:
        print("program interrupted before completion")
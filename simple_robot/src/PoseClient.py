#! /usr/bin/env python3
import rospy
from simple_robot_msgs.msg import GetRobotPoseResult, GetRobotPoseAction, GetRobotPoseGoal
from simple_robot_msgs.msg import VictimFound
from termcolor import colored

import actionlib

def callback(data):
    # if ypu are in the callback that means that there are data in topic /data_fusion/victim_found, therefore we create an action client object in order to take robot's position 
    pose_client(data)
        
def pose_client(data):
    client = actionlib.SimpleActionClient('/slam/get_robot_pose', GetRobotPoseAction)

    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goal = GetRobotPoseGoal()
    
    # Sends the goal to the action server.
    client.send_goal(goal = goal)

    # Waits for the server to finish performing the action.
    if client.wait_for_result():
        print(colored('Victim found! Robot Pose = (<{}>, <{}>). Sensor used for identification = <{}>'.format(client.get_result().x, client.get_result().y, data.victim_sensor), 'green'))
    
    # Prints out the result of executing the action
    return client.get_result()  

if __name__ == '__main__':
    try:
        rospy.init_node('pose_client')
        rospy.Subscriber("/data_fusion/victim_found", VictimFound, callback)
        rospy.spin()
        
    except rospy.ROSInterruptException:
        print("program interrupted before completion")
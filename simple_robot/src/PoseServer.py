#! /usr/bin/env python3

import rospy
import random 
import actionlib
from simple_robot_msgs.msg import GetRobotPoseResult, GetRobotPoseAction

class PoseServer(object):
    
    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, GetRobotPoseAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
        self._result = GetRobotPoseResult()
      
    def execute_cb(self, goal):
        self._result.x = random.randint(0,9)
        self._result.y = random.randint(0,9)
        return self._result
if __name__ == '__main__':
    rospy.init_node('pose_server')
    server = PoseServer('pose_server')
    rospy.spin()
#! /usr/bin/env python3

import rospy
import random 
import actionlib
from simple_robot_msgs.msg import GetRobotPoseResult, GetRobotPoseAction

class PoseServer(object):
    
    def __init__(self):
        self._as = actionlib.SimpleActionServer('/slam/get_robot_pose', GetRobotPoseAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
        self._result = GetRobotPoseResult()
      
    def execute_cb(self, goal):
        
        self._result.x = random.randint(0,9)
        self._result.y = random.randint(0,9)
        
        self._as.set_succeeded(self._result) # update the result 
        
if __name__ == '__main__':
    
    rospy.init_node('pose_server')
    server = PoseServer()
    rospy.spin()
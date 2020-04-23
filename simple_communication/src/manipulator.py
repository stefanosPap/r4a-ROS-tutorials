#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Int16

def  callback(data):
    print("Squared number of {} is {}".format(data.data, data.data ** 2))
    
def manipulator():
    rospy.init_node('manipulator', anonymous=True)
    rospy.Subscriber('task1/number', Int16, callback)
    rospy.spin()
    
if __name__ == '__main__':
    manipulator()
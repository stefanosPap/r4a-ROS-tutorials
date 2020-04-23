#!/usr/bin/env python3

import rospy
import random
from simple_robot_msgs.msg import TemperatureReading

def thermal_sensor():
    pub = rospy.Publisher('/sensors/temperature', TemperatureReading , queue_size=10)
    rospy.init_node('thermal_sensor')
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        temperature = random.uniform(20,40)
        rospy.loginfo(temperature)
        pub.publish(temperature)
        rate.sleep()

if __name__ == '__main__':
    try:
        thermal_sensor()
    except rospy.ROSInterruptException:
        pass
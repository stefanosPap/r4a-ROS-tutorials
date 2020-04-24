#!/usr/bin/env python3
import rospy
from simple_robot_msgs.msg import TemperatureReading
from simple_robot_msgs.msg import VictimFound
from termcolor import colored



def victim_check(temperature):
    pub = rospy.Publisher('/data_fusion/victim_found', VictimFound, queue_size=10)
    msg = VictimFound()
    msg.victim_sensor = "thermal"
    rospy.loginfo(colored(msg.victim_sensor + " at " + str(temperature.temperature), 'yellow'))
    pub.publish(msg)


def callback(temperature):
    if temperature.temperature > 34:
        try:
            victim_check(temperature)
        except rospy.ROSInterruptException:
            pass      
    
    
def detector():
    rospy.init_node('victim_detector')
    rospy.Subscriber("/sensors/temperature", TemperatureReading, callback)
    rospy.spin()

if __name__ == '__main__':
    detector()
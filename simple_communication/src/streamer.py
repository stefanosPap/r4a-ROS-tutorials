#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Int16
import random
 
def streamer():
    pub = rospy.Publisher('task1/number', Int16, queue_size=10)
    rospy.init_node('streamer', anonymous=True)
    rate = rospy.Rate(1) # 1 message per second 
    while not rospy.is_shutdown():
        msg = random.randint(0,100)
        print("Number sent:" + str(msg))
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        streamer()
    except rospy.ROSInterruptException:
        pass 
        
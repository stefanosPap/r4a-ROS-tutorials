#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Int16
from simple_communication_param.cfg import SimpleComParamsConfig
from dynamic_reconfigure.server import Server


class Manipulator():
    def __init__(self):
        self.subscriber = rospy.Subscriber('task1/number', Int16, self.callback)
        self.server = Server(SimpleComParamsConfig,self.callback_dyn)
        
    def callback_dyn(self,config, level):
        self.power = config["power"]
        return config 

    def  callback(self,data):
        self.print_result(data)
        
    def print_result(self, data):
        print( "{} power of {} is {}".format(self.power, data.data, data.data ** self.power)) 
       
    
if __name__ == '__main__':
    rospy.init_node('manipulator', anonymous=True)
    Manipulator()
    rospy.spin()
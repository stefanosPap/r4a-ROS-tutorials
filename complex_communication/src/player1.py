#!/usr/bin/env python

import sys
import rospy
import random 
from complex_communication.srv import *

def player1(move,turn):
    rospy.wait_for_service('play')
    try:
        play = rospy.ServiceProxy('play', TicTacToe)
        print(play(move, turn))
    except rospy.ServiceException, e:
        print e

if __name__ == "__main__":
    move = random.randint(0,8)
    print("Player 1 requesting move:{}".format(move))
    a = player1(move,turn = 1)
    
#!/usr/bin/env python3

import sys
import rospy
from complex_communication.srv import *

def player2(move,turn):
    rospy.wait_for_service('play')
    try:
        play = rospy.ServiceProxy('play', TicTacToe)
        play(move, turn) 
    except rospy.ServiceException:
        print("Service call failed")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        move = int(sys.argv[1])
    else:
        print("Give me a move")
        sys.exit(1)
    print("Requesting move:{}".format(move))
    player2(move,turn = 2)
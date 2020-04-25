#!/usr/bin/env python

import sys
import rospy
import random
from time import sleep  
from complex_communication.srv import TicTacToe

def player1(move,turn):
    
    try:
        play = rospy.ServiceProxy('play', TicTacToe)
        resp = play(move, turn)
        return resp
     
    except rospy.ServiceException:
        return 0 

if __name__ == "__main__":
    rospy.init_node('player1')
     
    while True:
        while True:
            rospy.wait_for_service('play') 
            move = random.randint(0,8)
            print("Player 1 requesting move:{}".format(move))
            resp = player1(move, turn = 1)
            if resp == 0:
                break
            if resp.validation == True or resp.status == False:
                break
            else:
                print("Invalid move, please request new move")  
        sleep(2)
        if resp == 0:
            break
        if resp.status == False:
            break

     
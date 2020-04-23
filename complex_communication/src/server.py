#!/usr/bin/env python3

from complex_communication.srv import TicTacToe,TicTacToeResponse, TicTacToeRequest
from std_msgs.msg import Int16MultiArray
import rospy

def handle(req):
    if req.turn == 1:
        if TicTacToeResponse.table[req.move] == ' ':
            TicTacToeResponse.table[req.move] = 'O'
    elif req.turn == 2:
        if TicTacToeResponse.table[req.move] == ' ':
            TicTacToeResponse.table[req.move] = 'X'
    return  
def server():
    rospy.init_node('server')
    s = rospy.Service('play', TicTacToe, handle)
    print("Game starts")
    rospy.spin()

if __name__ == "__main__":
    server()
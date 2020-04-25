#!/usr/bin/env python3
import rospy
import numpy as np 
from complex_communication.srv import TicTacToe,TicTacToeResponse, TicTacToeRequest
from std_msgs.msg import Int16MultiArray, MultiArrayLayout, MultiArrayDimension
from time import sleep
import random
import sys 
from termcolor import colored

class Server():
    def __init__(self):
        s = rospy.Service('play', TicTacToe, self.handle)
        self.table = [0,0,0,0,0,0,0,0,0]
        self.status = True
        s.spin()
   
    
    def shutdown(self):
        winner = self.evaluate(self.convert())
        if winner != -1: 
            print(colored("The winner player is {}!".format(winner), 'green'))    
        else:
            print(colored("Tie", 'yellow'))
        rospy.signal_shutdown(' ')
        
            
    def handle(self,req):
        valid = self.validation(req.move)
        if not self.status:
            self.shutdown()
        if valid:
            self.table = self.play_game(req)
            self.status = not all(self.table)
            if self.evaluate(self.convert()):
                self.status = False 
            return  TicTacToeResponse(self.table, self.status, valid)
        else:
            self.status = not all(self.table)
            return TicTacToeResponse(self.table,self.status, valid)
            
    def validation(self, move):
        if self.table[move] == 0:
            return True
        else:
            return False
             
    def convert(self):
        table = np.array(self.table)
        table = table.reshape(3,3)
        return table

    def iconvert(self, table):
        table = table.reshape(1,-1)
        table = table.tolist()
        table = table[0] # in order to remove double brackets 
        return table
    
    def row_win(self,board, player): 
        for x in range(len(board)): 
            win = True
            
            for y in range(len(board)): 
                if board[x, y] != player: 
                    win = False
                    continue
                    
            if win == True: 
                return(win) 
        return(win) 
    
    # Checks whether the player has three 
    # of their marks in a vertical row 
    def col_win(self,board, player): 
        for x in range(len(board)): 
            win = True
            
            for y in range(len(board)): 
                if board[y][x] != player: 
                    win = False
                    continue
                    
            if win == True: 
                return(win) 
        return(win) 
    
    # Checks whether the player has three 
    # of their marks in a diagonal row 
    def diag_win(self,board, player): 
        win = True
        y = 0
        for x in range(len(board)): 
            if board[x, x] != player: 
                win = False
        win = True
        if win: 
            for x in range(len(board)): 
                y = len(board) - 1 - x 
                if board[x, y] != player: 
                    win = False
        return win
    
    def evaluate(self, board): 
        winner = 0
        
        for player in [1, 2]: 
            if (self.row_win(board, player) or
                self.col_win(board,player) or 
                self.diag_win(board,player)): 
                    
                winner = player 
                
        if np.all(board != 0) and winner == 0: 
            winner = -1
        return winner
 
  
    def place(self,board, player, move): 
        board[move] = player 
        return(board)
    
    def play_game(self,req):
        board = self.table   
        board = self.place(board, req.turn, req.move)
        board = self.convert() 
        print(board) 
        
        board = self.iconvert(board)  
        return(board)
 
if __name__ == "__main__":
    rospy.init_node('server')
    Server()


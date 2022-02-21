# -*- coding: utf-8 -*-
    
from random import sample



#Start----------------------------------------------
#create a random fully solved board
def makeBoard():   
    #base soloution
    board = [
     [1, 2, 3, 4, 5, 6, 7, 8, 9], 
     [4, 5, 6, 7, 8, 9, 1, 2, 3], 
     [7, 8, 9, 1, 2, 3, 4, 5, 6], 
     [2, 3, 4, 5, 6, 7, 8, 9, 1], 
     [5, 6, 7, 8, 9, 1, 2, 3, 4], 
     [8, 9, 1, 2, 3, 4, 5, 6, 7], 
     [3, 4, 5, 6, 7, 8, 9, 1, 2], 
     [6, 7, 8, 9, 1, 2, 3, 4, 5], 
     [9, 1, 2, 3, 4, 5, 6, 7, 8]
     ]
    
    
    block1 = [board[0],board[1],board[2]]
    block2 = [board[3],board[4],board[5]]
    block3 = [board[6],board[7],board[8]]
    
    #randomization
    
    def shuf(block): return sample(block,len(block))
    #row shuffle                        
    block1 = shuf(block1);
    block2 = shuf(block2);
    block3 = shuf(block3);
    
    
    #unblock rows
    def unblock(one,two,three):
        newboard = []
        for x in one: newboard.append(x) 
        for x in two: newboard.append(x) 
        for x in three: newboard.append(x) 
        return newboard
    
    
    board = unblock(block1,block2,block3)
    
    #col blocks/flipped
    block1.clear()
    col = []
    for c in range(3):
        for x in board: col.append(x[c])
        block1.append(col)
        col = []
    block2.clear()    
    for c in range(3,6):
        for x in board: col.append(x[c])
        block2.append(col)
        col = []
    block3.clear()  
    for c in range(6,9):
        for x in board: col.append(x[c])
        block3.append(col)
        col = []
    
    
    #col shuffle/flipped row suffle
    block1 = shuf(block1);
    block2 = shuf(block2);
    block3 = shuf(block3);
    
    
    #unblock
    board = unblock(block1,block2,block3)
    
    return board
#end----------------------------------------------



#start--------------------------------------------
#create board with filled amount
def unslovedBoard(filled):
    board =  makeBoard()
    remove = sample(range(81), 81-filled)
    for x in remove:
        board[x//9][x%9] = 0
    return board
#end----------------------------------------------


#start--------------------------------------------
#check if given board solution is valid
def checkSolved(board):
    def check(row):
        if (all(x in row for x in [9,8,7,6,5,4,3,2,1])):
            return True
        else:
            return False
        
    #check rows    
    for row in board:
        if not (check(row)): return False
    
    #check 3x3 cubes
    for r in range(3): 
        for c in range(3):
            myset = {board[r*3][c*3],board[r*3][c*3+1],board[r*3][c*3+2],
                     board[r*3+1][c*3],board[r*3+1][c*3+1],board[r*3+1][c*3+2],
                     board[r*3+2][c*3],board[r*3+2][c*3+1],board[r*3+2][c*3+2]
                     }
            if not (check(myset)): return False
    
    #check cols
    col = []
    for c in range(9):
        for x in board: col.append(x[c])
        if not (check(col)): return False
        col = []
        
    #checks passed
    return True
#end---------------------------------------------


    
    



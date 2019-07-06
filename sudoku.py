
# https://stackoverflow.com/questions/717725/understanding-recursion
"""
    Sudoku solver in Python. Your code gets a Sudoku puzzle from the input (i.e., a file) 
    and returns the output in an output file.
    Algorithm: use backtracking with forward checking and "degree" and "MRV" heuristics. 

"""

import math
from operator import itemgetter, attrgetter
import sys
import time

def isValid(row,col,num,board):
    # Check row
    for i in range(len(board)):
        if num == board[row][i]:
            return False

    # Check Column
    for i in range(len(board)):
        if num == board[i][col]:
            return False
    
    # Check sub-boards
    curr_row = math.floor (row / 3)
    curr_col = math.floor (col / 3)

    curr_row *= 3
    curr_col *= 3

    for i in range (3):
        for j in range (3):
            if num == board[i+curr_row][j+curr_col]:
                return False

    return True

# Get the potential values for each row and column
def getPotentialValuesForEachSquare(board):
    """
        rtype: list[set]
        
    """
    squares = []
    for i in enumerate(range(81)):
        squares.append([0])
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                for num in range (1,10):
                    if (isValid(row,col,num,board)):
                        squares[col+row*9].append(num)

    return squares


def getRemainingSquares(board):
    """
        rtype: list of tupples  
        Get target squares.
    """
    squares = []
    for row in range(len(board)):
        for  col in range(len(board)):
            if board[row][col] == 0:
                squares.append((row,col))
    
    return squares

def getDegree(board, row, col, values):

    """
        rtype: int
        Get heuristic degree for each square
        This degree will be using to break the tie of 2 or more MRV variables. 
    """
    # check Column:
    degree = 0
    for i in range (len(board)):
        for val in values[col+row*9]:
            if val == board[row][i]:
                degree+=1

            if val == board[i][col]:
                degree+=1
            

    # Check sub-boards
    curr_row = math.floor (row / 3)
    curr_col = math.floor (col / 3)

    curr_row *= 3
    curr_col *= 3

    for i in range (3):
        for j in range (3):
            for val in values[col+row*9]:
                if val == board[i+curr_row][j+curr_col]:
                    degree+=1

    return degree


def sudokuSolver(board):

    empty_squares = getRemainingSquares(board)
    if (not len(empty_squares)):
        # When there is no more empty square to solve, then it means we solved the whole board
        return True
    

    potentialValues = getPotentialValuesForEachSquare(board) # Run arc-consistency function. 

    mrv = []
    minimum = sys.maxsize
    # Find the most restricted variable.
    for square in empty_squares:
        curr_len = len(potentialValues[square[1]+square[0]*9])
        if curr_len < minimum:
            minimum =  curr_len
        mrv.append ([len(potentialValues[square[1]+square[0]*9]), (square[0],square[1])])

    # TODO: use the heuristic to break tie.
    # When there are more than 1 Minimum remaining values, then we get the one with highest degree
     
    max_degree = 0
    for mrv_square in mrv:
        if mrv_square[0] == minimum:
            curr_degree = getDegree(board,mrv_square[1][0], mrv_square[1][1], potentialValues)
            if curr_degree > max_degree:
                (row,col) = (mrv_square[1][0], mrv_square[1][1])
            
    values = potentialValues[col+row*9] 

    # Backtracking.
    for num in values:
        if not isValid(row,col,num,board):
            continue
        board[row][col] = num
        if (sudokuSolver(board)):
            return True

        board[row][col] = 0
    
    return False

                  
def run():

    if len(sys.argv) < 2:
        print("Usage: python sudoku.py <#sudoku puzlle>")
        exit()

    grid = []

    with open(sys.argv[1]) as f:
        for line in f:  
            temp = []
            for ch in line:
                if (ch != '\n'):
                    temp.append(int(ch))

            grid.append(temp)

    print (' >  ')
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in grid]))


    if (sudokuSolver(grid)):
        print (" > Result: ")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in grid]))
    else:
        print("can't find the solution")



run()

    
                    
                        




            


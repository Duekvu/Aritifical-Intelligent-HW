"""
    Author: Duc Vu
    NQueens Problem using backtracking algorithm
"""

import sys

def solveNQueens(n):
    """
    :type n: int
    :return type: List[List[int]] // the y position place the queen labeled 1. 

    """
    res, y_col, left_diag, right_diag = [], [], [], []

    def dfs(x=0):
        if x == n:
            # Painting every row y_col
            res.append([e for e in y_col])
            return
        for y in range(n):
            # The y position in the row (x+1) should not be in the same y column, x-y position, or x+y position
            if y not in y_col and x+y not in right_diag and x-y not in left_diag:
                y_col.append(y)
                right_diag.append(x+y)
                left_diag.append(x-y)
                dfs(x+1)  # painting row x+1

                # backtracking
                y_col.pop()
                right_diag.pop()
                left_diag.pop()
    dfs()  # explore more possible solutions
    return res

def displayBoards(board:list, n):
    for pos in board:
        print ("Board ", board.index(pos))
        Matrix = [[0 for x in range(n)] for y in range(n)] 
        for y in range(n):
            Matrix[y][pos[y]] = 1
            print(Matrix[y])
            print()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int (sys.argv[1])
        rs = solveNQueens(n)
        print("Result after run backtracking algorithm for ",sys.argv[1], " queens problem:  \n", rs)
        print('\n------------------Display in the ' ,sys.argv[1] ,'*', sys.argv[1], ' chessboard------------------ ')
        displayBoards(rs, n)
     
    else:
        print("Usage: py Nqueen.py <#numberOfQueens>")
        

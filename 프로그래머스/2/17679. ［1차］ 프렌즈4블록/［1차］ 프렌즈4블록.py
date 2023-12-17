import sys
from collections import Counter
import copy

def check(m, n, board):
    x = 0
    y = 0
    result = 0
    temp = copy.deepcopy(board)
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i+1][j] and board[i+1][j] == board[i][j+1] and board[i][j+1] == board[i+1][j+1]:
                if temp[i][j] != 0:
                    temp[i][j] = 0
                    result += 1
                if temp[i+1][j] != 0:
                    temp[i+1][j] = 0
                    result += 1
                if temp[i][j+1] != 0:
                    temp[i][j+1] = 0
                    result += 1
                if temp[i+1][j+1] != 0:
                    temp[i+1][j+1] = 0
                    result += 1
    board = temp
    return result, board

def move(m, n, board):
    result = [[0 for i in range(n)] for j in range(m)]
    
    for col in range(n):
        temp = list()
        for row in range(m-1, -1, -1):
            if board[row][col] != 0:
                temp.append(board[row][col])
        for i in range(len(temp)):
            result[m-1-i][col] = temp[i]
            
    return result
                
def solution(m, n, board):
    answer = 0
    board = [list(data) for data in board]
    
    while True:
        cnt, board = check(m, n, board)
        
        if cnt == 0:
            break
        else:
            answer += cnt
            
        board = move(m, n, board)
    return answer
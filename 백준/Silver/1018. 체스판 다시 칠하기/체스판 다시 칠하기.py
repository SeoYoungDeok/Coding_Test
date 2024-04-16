import sys

input = sys.stdin.readline

N, M = map(int, input().split())

w_filter = list()
b_filter = list()

for i in range(4):
    w_filter.append('WB' * 4)
    w_filter.append('BW' * 4)
    b_filter.append('BW' * 4)
    b_filter.append('WB' * 4)
    
board = list()

for __ in range(N):
    board.append(input())

answer_list = list()

for i in range(M-7):
    for j in range(N-7):
        answer_list.append(sum([1 for x in range(8) for y in range(8) if w_filter[y][x] != board[j+y][i+x]]))
        answer_list.append(sum([1 for x in range(8) for y in range(8) if b_filter[y][x] != board[j+y][i+x]]))

print(min(answer_list))
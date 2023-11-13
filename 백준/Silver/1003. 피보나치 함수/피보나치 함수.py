import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    answer = [(1,0), (0,1)]
    n = int(input())
    
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        for i in range(2, n+1):
            answer.append((answer[i-1][0] + answer[i-2][0], answer[i-1][1] + answer[i-2][1]))
        print("{} {}".format(answer[-1][0], answer[-1][1]))
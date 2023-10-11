import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    answer = [1,1,1,2,2,3]
    if n <= 6:
        print(answer[n-1])
    else:
        for i in range(6, n+1):
            answer.append(answer[i-1] + answer[i-5])
        print(answer[n-1])
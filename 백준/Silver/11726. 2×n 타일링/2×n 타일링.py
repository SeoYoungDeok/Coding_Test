import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    answer = [1,2]
    for i in range(2, N+1):
        answer.append(answer[i-1] + answer[i-2])
    print(answer[N-1]%10007)
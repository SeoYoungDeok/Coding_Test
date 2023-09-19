import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    answer = [1,3]
    for i in range(2, N+1):
        temp = answer[i-1] + (2 * answer[i-2])
        answer.append(temp)
    print(answer[N-1]%10007)
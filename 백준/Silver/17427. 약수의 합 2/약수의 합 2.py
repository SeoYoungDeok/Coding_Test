import sys

input = sys.stdin.readline
N = int(input().rstrip())

answer = 0
for i in range(1, N+1):
    answer += i * (N//i)

print(answer)
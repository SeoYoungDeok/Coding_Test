import sys

input = sys.stdin.readline

N = int(input())

answer = 0
for i in range(1, N+1):
    if i % 5 == 0:
        answer += 1
    if i % 25 == 0:
        answer += 1
    if i % 125 == 0:
        answer += 1

print(answer)
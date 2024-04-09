import sys

n = list()
for i in range(1, 46):
    for j in range(i):
        n.append(i)

N, M = map(int, input().split())

answer = list()
for i in range(N-1, M):
    answer.append(n[i])

print(sum(answer))
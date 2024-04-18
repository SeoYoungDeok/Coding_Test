from sys import stdin as s

N, M = map(int, s.readline().rstrip().split())

S = {s.readline().rstrip() : 0 for i in range(N)}

answer = 0
for i in range(M):
    if s.readline().rstrip() in S:
        answer += 1

print(answer)
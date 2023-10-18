from sys import stdin as s
from collections import deque

N, M = map(int, s.readline().rstrip().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, s.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0, 999999]
for i in range(1, N + 1):
    queue = deque([graph[i]])
    visited = [False] * (N + 1)

    score = [-1] * N
    level = 1
    while queue[0]:
        temp = []
        pop = queue.popleft()
        for n in pop:
            if not visited[n]:
                visited[n] = True
                temp += graph[n]
                if score[n - 1] == -1:
                    score[n - 1] = level
        level += 1
        queue.append(temp)

    if answer[1] > sum(score) - score[i - 1]:
        answer[0] = i
        answer[1] = sum(score) - score[i - 1]

print(answer[0])

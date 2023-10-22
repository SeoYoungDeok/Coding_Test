from sys import stdin as s
from collections import deque

N, M = map(int, s.readline().rstrip().split())

array = []
visited = []
for i in range(N):
    array.append(s.readline().rstrip())
    visited.append([False] * M)

x, y = 0, 0
for i in range(N):
    for j in range(M):
        if array[i][j] == "I":
            x, y = i, j


def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = True

    cnt = 0
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx, ny = dx[idx] + x, dy[idx] + y
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if array[nx][ny] != "X":
                    if array[nx][ny] == "P":
                        cnt += 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    return cnt


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = bfs(x, y)
if answer:
    print(answer)
else:
    print("TT")
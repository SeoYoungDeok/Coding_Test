from sys import stdin as s
from collections import deque

N, M = map(int, s.readline().rstrip().split())

array = []
visited = []
for _ in range(N):
    array.append(list(map(int, s.readline().rstrip())))
    visited.append([-1] * M)


def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if array[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

bfs(0, 0)
print(visited[N - 1][M - 1])

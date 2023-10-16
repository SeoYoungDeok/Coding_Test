from sys import stdin as s
from collections import deque

N, M = map(int, s.readline().rstrip().split())

array = []
visited = []
for i in range(N):
    array.append(list(map(int, s.readline().rstrip().split())))
    visited.append([-1] * M)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 0
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < M and 0 <= ny and ny < N and visited[ny][nx] == -1:
                if array[ny][nx] == 0:
                    visited[ny][nx] = 0
                elif array[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))


for i in range(N):
    for j in range(M):
        if array[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()

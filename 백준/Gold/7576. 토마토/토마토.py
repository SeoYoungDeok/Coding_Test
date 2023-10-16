from sys import stdin as s
from collections import deque

M, N = map(int, s.readline().rstrip().split())

array = []
for i in range(N):
    array.append(list(map(int, s.readline().rstrip().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque([])

for i in range(N):
    for j in range(M):
        if array[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                queue.append([nx, ny])


bfs()
answer = 0
for row in array:
    for col in row:
        if col == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(row))
print(answer - 1)
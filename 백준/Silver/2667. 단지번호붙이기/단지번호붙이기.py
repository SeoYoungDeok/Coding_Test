from sys import stdin as s
from collections import deque

N = int(s.readline().rstrip())

array = []
for i in range(N):
    array.append(list(map(int, s.readline().rstrip())))

visited = [[-1] * N for i in range(N)]


def bfs(i, j, n):
    if array[i][j] == 0:
        return 0

    queue = deque([[i, j]])
    visited[i][j] = n
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if array[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = n
                    queue.append([nx, ny])

    return cnt


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

block = 1
answer = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == -1:
            cnt = bfs(i, j, block)
            if cnt != 0:
                answer.append(cnt)
                block += 1
answer.sort()
print(block - 1)
for i in answer:
    print(i)

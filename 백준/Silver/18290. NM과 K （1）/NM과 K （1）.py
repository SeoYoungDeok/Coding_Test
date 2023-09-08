from sys import stdin as s

N, M, K = map(int, s.readline().strip().split())

array = []
for i in range(N):
    array.append(list(map(int, s.readline().strip().split())))

visited = [[False] * M for _ in range(N)]
answer = -999999


def dfs(x, y, cnt, s):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if cnt == K:
        global answer
        answer = max(answer, s)
        return

    for i in range(x, N):
        for j in range(y if i == x else 0, M):
            if visited[i][j]:
                continue
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                    break
            else:
                visited[i][j] = True
                dfs(i, j, cnt + 1, s + array[i][j])
                visited[i][j] = False


dfs(0, 0, 0, 0)
print(answer)
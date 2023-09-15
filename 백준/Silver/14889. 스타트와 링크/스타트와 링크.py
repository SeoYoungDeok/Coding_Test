from sys import stdin as s

N = int(s.readline().strip())

array = []
for i in range(N):
    array.append(list(map(int, s.readline().strip().split())))

visited = [False] * N
answer = 9999999

def DFS(L, idx):
    global answer
    if L == N // 2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += array[i][j]
                elif not visited[i] and not visited[j]:
                    B += array[i][j]
        answer = min(answer, abs(A - B))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(L + 1, i + 1)
            visited[i] = False


DFS(0, 0)
print(answer)
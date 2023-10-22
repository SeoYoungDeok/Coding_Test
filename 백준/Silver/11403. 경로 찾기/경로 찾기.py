from sys import stdin as s

N = int(s.readline().rstrip())

graph = []
for i in range(N):
    graph.append(list(map(int, s.readline().rstrip().split())))


for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = max(graph[a][b], graph[a][k] * graph[k][b])

for i in range(N):
    print(*graph[i])
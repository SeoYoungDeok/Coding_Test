import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
queue = deque()

answer = 0
for i in range(1, N+1):
    if visited[i] == False:
        answer += 1
        queue.append(i)
        
        while queue:
            v = queue.popleft()
            if visited[v] == False:
                visited[v] = True
                for j in graph[v]:
                    queue.append(j)
print(answer)
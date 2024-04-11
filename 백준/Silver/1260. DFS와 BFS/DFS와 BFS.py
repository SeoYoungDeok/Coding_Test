import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
stack = []
stack.append(V)

while stack:
    v = stack.pop()
    if visited[v] == False:
        visited[v] = True
        print(v, end=' ')
        graph[v].sort(reverse=True)
        for i in graph[v]:
            stack.append(i)
print()


visited = [False] * (N+1)
queue = deque()
queue.append(V)

while queue:
    v = queue.popleft()
    if visited[v] == False:
        visited[v] = True
        print(v, end=' ')
        graph[v].reverse()
        for i in graph[v]:
            queue.append(i)
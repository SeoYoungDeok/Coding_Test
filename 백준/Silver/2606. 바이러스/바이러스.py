import sys
from collections import deque

input = sys.stdin.readline

HOST = int(input())
CONN = int(input())

graph = [[] for _ in range(HOST+1)]

for i in range(CONN):
    host, con = map(int, input().split())
    graph[host].append(con)
    graph[con].append(host)

visited = [False] * (HOST+1)

queue = deque([1])
visited[1] = True

while queue:
    v = queue.popleft()
    
    for j in graph[v]:
        if not visited[j]:
            queue.append(j)
            visited[j] = True
            
print(sum(visited)-1)
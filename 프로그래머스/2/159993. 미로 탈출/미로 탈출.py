from collections import deque
import copy

def bfs(graph, visited, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([[x, y]])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if 0 <= nx and 0 <= ny and nx < len(graph) and ny < len(graph[0]) and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
    return graph
    
def solution(maps):
    answer = 0
    
    visited = [[False for j in i] for i in maps]
    graph = [[0 for j in i] for i in maps]
    
    for i, row in enumerate(maps):
        for j, s in enumerate(row):
            if s == "S":
                start = (i, j)
            elif s == "L":
                lever = (i, j)
            elif s == "E":
                exit = (i, j)
            elif s == "X":
                visited[i][j] = True
    
    graph = bfs(graph, copy.deepcopy(visited), start[0], start[1])
    
    if graph[lever[0]][lever[1]] == 0:
        return -1
    else:
        graph = bfs(graph, visited, lever[0], lever[1])
        if graph[exit[0]][exit[1]] == 0:
            return -1
        else:
            return graph[exit[0]][exit[1]]

from sys import stdin as s
from collections import deque

X, Y = map(int, s.readline().strip().split())


def bfs(x, y, visited):
    queue = deque([[x]])
    cnt = 0
    visited[x] = 1
    while queue[0]:
        pop = queue.popleft()
        queue_list = []
        for i in pop:
            if i == y:
                return cnt
            for num in [i - 1, i + 1, i * 2]:
                if num >= 0 and num <= 100_000 and not visited[num]:
                    visited[num] = 1
                    queue_list.append(num)
        queue.append(queue_list)
        cnt += 1


visited = [0] * 100_001
print(bfs(X, Y, visited))
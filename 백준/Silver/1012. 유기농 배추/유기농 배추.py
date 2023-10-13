import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    
    array = [[0]*M for i in range(N)]
    
    for j in range(K):
        x, y = map(int, input().rstrip().split())
        array[y][x] = 1
    
    if M*N == K:
        print(1)
    else:
        s = 0
        for row in range(N):
            for col in range(M):
                if array[row][col] == 1:
                    queue = deque()
                    queue.append([row, col])

                    while queue:
                        v = queue.popleft()
                        array[v[0]][v[1]] = 0

                        if v[0]-1 >= 0 and array[v[0]-1][v[1]] == 1:
                            queue.append((v[0]-1, v[1]))

                        if v[1]-1 >= 0 and array[v[0]][v[1]-1] == 1:
                            queue.append((v[0], v[1]-1))

                        if v[0]+1 <= N-1 and array[v[0]+1][v[1]] == 1:
                            queue.append((v[0]+1, v[1]))

                        if v[1]+1 <= M-1 and array[v[0]][v[1]+1] == 1:
                            queue.append((v[0], v[1]+1))
                    s += 1

        print(s)
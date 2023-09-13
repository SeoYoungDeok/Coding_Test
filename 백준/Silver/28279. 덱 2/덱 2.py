from sys import stdin as s
from collections import deque


N = int(s.readline().strip())

queue = deque([])

for i in range(N):
    op = list(map(int, s.readline().strip().split()))

    if op[0] == 1:
        queue.appendleft(op[1])
    elif op[0] == 2:
        queue.append(op[1])
    elif op[0] == 3:
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif op[0] == 4:
        if len(queue):
            print(queue.pop())
        else:
            print(-1)
    elif op[0] == 5:
        print(len(queue))
    elif op[0] == 6:
        if len(queue):
            print(0)
        else:
            print(1)
    elif op[0] == 7:
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif op[0] == 8:
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
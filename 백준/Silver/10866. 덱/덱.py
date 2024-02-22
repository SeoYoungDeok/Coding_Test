import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    S = list(input().rstrip().split())
    
    if S[0] == 'push_front':
        queue.appendleft(int(S[1]))
        
    elif S[0] == 'push_back':
        queue.append(int(S[1]))
        
    elif S[0] == 'pop_front':
        if queue:
            pop = queue.popleft()
            print(pop)
        else:
            print(-1)
        
    elif S[0] == 'pop_back':
        if queue:
            pop = queue.pop()
            print(pop)
        else:
            print(-1)
        
    elif S[0] == 'size':
        print(queue.__len__())
        
    elif S[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
            
    elif S[0] == 'front':
        if queue:
            pop = queue.popleft()
            print(pop)
            queue.appendleft(pop)
        else:
            print(-1)
            
    elif S[0] == 'back':
        if queue:
            pop = queue.pop()
            print(pop)
            queue.append(pop)
        else:
            print(-1)
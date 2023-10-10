import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()
for i in range(N):
    n = int(input())
    
    if n != 0:
        queue.append(n)
    else:
        queue.pop()
    
print(sum(queue))
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([x+1 for x in range(N)])

answer = list()
while len(answer) != N:
    for i in range(K-1):
        pop = queue.popleft()
        queue.append(pop)
    answer.append(queue.popleft())
    
print("<" + answer.__str__()[1:-1] + ">")
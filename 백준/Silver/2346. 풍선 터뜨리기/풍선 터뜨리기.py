from sys import stdin as s
from collections import deque

N = int(s.readline().rstrip())
balloon = deque(zip(range(1, N+1), list(map(int, s.readline().rstrip().split()))))

answer = []

while balloon:
    n, i = balloon.popleft()
    i = i-1 if i > 0 else i
    balloon.rotate(-i)
    answer.append(n)

print(*answer)
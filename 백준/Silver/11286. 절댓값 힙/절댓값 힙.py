from sys import stdin as s
import heapq

N = int(s.readline().rstrip())

heapqueue = []
for i in range(N):
    x = int(s.readline().rstrip())

    if 0 < x:
        heapq.heappush(heapqueue, [abs(x), 1])
    elif 0 > x:
        heapq.heappush(heapqueue, [abs(x), -1])
    elif x == 0:
        if heapqueue:
            n, sign = heapq.heappop(heapqueue)
            print(n * sign)
        else:
            print(0)

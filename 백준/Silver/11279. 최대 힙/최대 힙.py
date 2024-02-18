import sys
import heapq

input = sys.stdin.readline

N = int(input())
array = list()

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(array) != 0:
            print(-(heapq.heappop(array)))
        else:
            print(0)
    else:
        heapq.heappush(array, -(x))
import sys
import heapq

n_jewelry, n_backpack = map(int, sys.stdin.readline().split())

jewelry_list = list()
for i in range(n_jewelry):
    jewelry_list.append(list(map(int, sys.stdin.readline().split())))

backpack_list = list()
for i in range(n_backpack):
    backpack_list.append(int(input()))

jewelry_list = sorted(jewelry_list, key = lambda x : (x[0]))

answer = 0
backpack_list.sort()

i = 0
heap = list()
for back in backpack_list:
    while i < n_jewelry and back >= jewelry_list[i][0]:
        heapq.heappush(heap, -jewelry_list[i][1])
        i += 1
    if heap:
        answer += heapq.heappop(heap)
    
print(-answer)
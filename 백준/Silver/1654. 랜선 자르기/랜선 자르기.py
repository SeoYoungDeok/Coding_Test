import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
lan_cables = list()

for _ in range(N):
    lan_cables.append(int(input()))

max_val = max(lan_cables)
min_val = 1

while min_val <= max_val:
    mid = (min_val + max_val) // 2
    cnt = 0 
    for l in lan_cables:
        cnt += l // mid
    
    if cnt >= K:
        min_val = mid + 1
    else:
        max_val = mid - 1

print(max_val)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

min_val = 1
max_val = max(tree_list)
while min_val <= max_val:
    mid = (min_val+max_val) // 2
    
    tree = 0
    for i in tree_list:
        if i > mid:
            tree = tree + (i - mid)
    
    if tree >= M:
        min_val = mid + 1
    else:
        max_val = mid - 1

print(max_val)
from sys import stdin as s
from collections import defaultdict

N = list(s.readline().strip())
array = list(s.readline().strip().split())

num_dict = defaultdict(int)
for i in array:
    num_dict[str(i)] = 1

M = list(s.readline().strip())
array = list(s.readline().strip().split())

for i in array:
    if num_dict[str(i)]:
        print(1, end=" ")
    else:
        print(0, end=" ")

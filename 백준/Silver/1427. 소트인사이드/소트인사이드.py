from sys import stdin as s
from collections import defaultdict

array = list(s.readline().strip())

num_dict = defaultdict(int)

for i in array:
    num_dict[i] += 1

print("".join([str(i) * num_dict[str(i)] for i in range(9, -1, -1)]))
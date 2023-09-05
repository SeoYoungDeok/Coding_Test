from sys import stdin as s
from collections import defaultdict

array = list(s.readline().strip())

array.sort(reverse=True)
print("".join(array))
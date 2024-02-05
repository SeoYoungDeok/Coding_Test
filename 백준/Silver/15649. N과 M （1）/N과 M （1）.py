from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

for i in list(permutations(range(1, N + 1), M)):
    print(*i)
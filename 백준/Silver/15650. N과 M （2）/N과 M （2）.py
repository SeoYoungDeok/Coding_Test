from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

for i in list(combinations(range(1, N + 1), M)):
    print(*i)
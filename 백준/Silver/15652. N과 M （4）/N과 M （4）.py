from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

for i in list(combinations_with_replacement(range(1, N + 1), M)):
    print(*i)
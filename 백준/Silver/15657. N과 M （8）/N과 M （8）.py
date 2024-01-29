from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in list(combinations_with_replacement(arr, M)):
    print(*i)
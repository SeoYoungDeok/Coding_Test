from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in list(combinations(arr, M)):
    print(*i)
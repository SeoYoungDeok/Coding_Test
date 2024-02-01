from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in list(permutations(arr, M)):
    print(*i)
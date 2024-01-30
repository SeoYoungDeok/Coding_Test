from itertools import product
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in list(product(arr, repeat=M)):
    print(*i)

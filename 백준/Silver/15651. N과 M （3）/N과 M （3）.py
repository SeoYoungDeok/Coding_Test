from itertools import product
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

for i in list(product(range(1, N + 1), repeat=M)):
    print(*i)
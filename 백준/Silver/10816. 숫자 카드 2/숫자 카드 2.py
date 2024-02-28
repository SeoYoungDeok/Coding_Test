import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

cnt = Counter(N_list)

for m in M_list:
    print(cnt[m], end=' ')
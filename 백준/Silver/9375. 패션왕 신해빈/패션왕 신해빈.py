import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        _ = input()
        print(1)
    else:
        fashion_list = list()
        for __ in range(n):
            fashion_list.append(input().rstrip().split()[1])

        cnt = Counter(fashion_list)
        values = list(cnt.values())
        tmp = 1
        for i in values:
            tmp *= (i+1)
        
        print(tmp-1)
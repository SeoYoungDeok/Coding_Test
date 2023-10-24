import sys

input = sys.stdin.readline

N = int(input())

X = list(map(int, input().split()))

temp = list(set(X))
temp.sort()

new_x = dict()

for i, x in enumerate(temp):
    new_x[x] = i

for j in X:
    print(new_x[j], end=' ')
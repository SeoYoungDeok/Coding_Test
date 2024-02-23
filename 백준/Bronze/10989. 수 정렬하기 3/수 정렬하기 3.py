import sys

input = sys.stdin.readline

N = int(input())
n_list = [0] * 10001
for _ in range(N):
    M = int(input())
    n_list[M] += 1

for i, n in enumerate(n_list):
    for j in range(n):
        sys.stdout.write("%s\n" %i)
import sys

input = sys.stdin.readline

N = int(input())

member_list = list()
for _ in range(N):
    age, name = input().rstrip().split()
    member_list.append([int(age), name])

member_list.sort(key=lambda x : x[0])

for r in member_list:
    print("{} {}".format(r[0], r[1]))
import sys

N, M = map(int, input().split())

poket_dict = dict()

for i in range(N):
    poketmon = input()
    poket_dict[poketmon] = i + 1
    poket_dict[str(i + 1)] = poketmon

for i in range(M):
    print(poket_dict[input()])
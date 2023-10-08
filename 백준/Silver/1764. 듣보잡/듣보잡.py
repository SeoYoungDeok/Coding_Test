import sys

N, M = map(int, input().split())

N_list = dict()
for i in range(N):
    N_list[input()] = 1

answer = list()
for j in range(M):
    M_name = input()
    if M_name in N_list:
        answer.append(M_name)

answer.sort()

print(len(answer))
for name in answer:
    print(name)
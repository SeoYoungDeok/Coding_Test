import sys

N, M = map(int, sys.stdin.readline().split())

N_list = dict()
for i in range(N):
    N_list[sys.stdin.readline().rstrip()] = 1

answer = list()
for j in range(M):
    M_name = sys.stdin.readline().rstrip()
    if M_name in N_list:
        answer.append(M_name)

answer.sort()

print(len(answer))
for name in answer:
    print(name)
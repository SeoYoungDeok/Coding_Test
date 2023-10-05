import sys

input = sys.stdin.readline

N = int(input())

answer = set()
for i in range(N):
    S = input().rstrip()
    answer.add(S)

answer = list(answer)
answer.sort()
answer = sorted(answer, key = lambda x : len(x))

for j in answer:
    print(j)
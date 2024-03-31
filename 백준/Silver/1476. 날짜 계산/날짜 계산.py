import sys

input = sys.stdin.readline

E, S, M = map(int, input().rstrip().split())

i = j = k = 1
answer = 1
while True:
    if i == E and j == S and k == M:
        print(answer)
        break
    else:
        i = (i % 15) + 1
        j = (j % 28) + 1
        k = (k % 19) + 1
        answer += 1
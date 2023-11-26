import sys

input = sys.stdin.readline

N = int(input())
x_y_list = list()
answer = [1]*N
for _ in range(N):
    x_y_list.append(list(map(int, input().split())))

n = 0
for i in x_y_list:
    for j in x_y_list:
        if i[0] < j[0] and i[1] < j[1]:
            answer[n] += 1
    n += 1
for r in answer:
    print(r, end=' ')

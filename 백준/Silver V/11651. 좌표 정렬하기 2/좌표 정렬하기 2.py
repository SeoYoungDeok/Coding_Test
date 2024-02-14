import sys

input = sys.stdin.readline

N = int(input())
x_y_list = list()
for _ in range(N):
    x_y_list.append(list(map(int, input().split())))

x_y_list.sort(key=lambda x: (x[1], x[0]))
for x, y in x_y_list:
    print("{} {}".format(x, y))
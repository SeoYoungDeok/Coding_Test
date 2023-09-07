from sys import stdin as s

N = int(s.readline().strip())

array = [[0 for i in range(100)] for j in range(100)]

for i in range(N):
    X, Y = map(int, s.readline().strip().split())
    for x in range(X, X + 10):
        for y in range(Y, Y + 10):
            array[y][x] = 1

answer = 0
for row in array:
    answer += sum(row)
print(answer)
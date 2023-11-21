import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
N_M_list = list()

for _ in range(N):
    N_M_list.append(list(map(int, input().split())))

max_val = max(map(max, N_M_list))
min_val = min(map(min, N_M_list))

answer = list()
for i in range(max_val+1, min_val-2, -1):
    time = 0
    b = B
    for row in N_M_list:
        for col in row:
            if 0 > col - i:
                time += abs(col - i)
                b -= abs(col - i)
            if 0 <= col - i:
                time += abs(col - i) * 2
                b += abs(col - i)
    
    if b < 0:
        pass
    else:
        answer.append([time, i])

answer.sort(key=lambda x: (x[0], -x[1]))

t = answer[0][0]
h = answer[0][1]
for i in answer:
    if answer[0][0] == i[0]:
        if i[1] > h:
            t = i[0]
            h = i[1]

print(t, h)
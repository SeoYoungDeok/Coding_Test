import sys

N = int(input())

if N < 10:
    if (N / 2).is_integer():
        print(int(N / 2))
    else:
        print(0)
else:
    answer_list = list()
    for j in range(N, N-100, -1):
        S = j
        if j < 1:
            break
            
        for c in str(j):
            S += int(c)

        if S == N:
            answer_list.append(j)

    if answer_list:
        print(min(answer_list))
    else:
        print(0)
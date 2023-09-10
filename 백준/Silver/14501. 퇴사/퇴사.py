from sys import stdin as s

N = int(s.readline().strip())

T = []
P = []
for i in range(N):
    t, p = map(int, s.readline().strip().split())
    T.append(t)
    P.append(p)


def go(k, num):
    global answer

    for i in range(k, N):
        if i + T[i] <= N:
            go(i + T[i], num + P[i])

    if answer < num:
        answer = num
    return


answer = 0
go(0, 0)
print(answer)

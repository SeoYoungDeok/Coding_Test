from sys import stdin as s

N = list(s.readline().strip())


if len(N) == 1:
    print(N[0])
else:
    answer = (int("".join(N)) - int("9" * (len(N) - 1))) * len(N)

    for i in range(len(N) - 1, 0, -1):
        answer += 9 * (10 ** (i - 1)) * i

    print(answer)

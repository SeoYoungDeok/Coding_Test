from sys import stdin as s


T = int(s.readline().strip())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


for i in range(T):
    answer = -1
    a, b, c, d = map(int, s.readline().strip().split())
    for idx, j in enumerate(range(c, lcm(a, b) + 1, a)):
        if j % b == d or (b == d and j % b == 0):
            answer = j
            break
    print(answer)

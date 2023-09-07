from sys import stdin as s

a1, a0 = map(int, s.readline().strip().split())
c = int(s.readline().strip())
n0 = int(s.readline().strip())

if a1 * n0 + a0 <= c * n0:
    if a1 <= c:
        print(1)
    else:
        print(0)
else:
    print(0)

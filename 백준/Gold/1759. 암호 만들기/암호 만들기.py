from sys import stdin as s


L, C = map(int, s.readline().strip().split())
C_list = s.readline().strip().split()
C_list.sort()


def check(s):
    mo = ["a", "e", "i", "o", "u"]
    mo_cnt = 0
    ja_cnt = 0

    for c in s:
        if c in mo:
            mo_cnt += 1
        else:
            ja_cnt += 1

    if mo_cnt >= 1 and ja_cnt >= 2:
        return True
    else:
        return False


def go(s, k):
    if len(s) == L:
        if check(s):
            print(s)
        return

    for i in range(k, C):
        go(s + C_list[i], i + 1)


go("", 0)
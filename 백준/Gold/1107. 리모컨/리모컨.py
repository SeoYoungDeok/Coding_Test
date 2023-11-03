import sys

input = sys.stdin.readline

target_ch = int(input())
N = int(input())
if N:
    broken_btn = list(map(int, input().split()))
else:
    broken_btn = list()

if target_ch == 100:
    print(0)
elif N == 10:
    print(abs(target_ch-100))
else:
    min_ch = 9999999
    move_ch = 0
    for i in range(1000001):
        flag = 1
        for c in str(i):
            if int(c) in broken_btn:
                flag = 0

        if flag and abs(target_ch - i) < min_ch:
            min_ch = abs(target_ch - i)
            move_ch = i

    answer = abs(target_ch - move_ch) + len(str(move_ch))

    print(min(answer, abs(target_ch-100)))
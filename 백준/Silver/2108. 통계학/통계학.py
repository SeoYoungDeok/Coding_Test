import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

if N == 1:
    answer = int(input())
    print(answer)
    print(answer)
    print(answer)
    print(0)
else:
    N_list = list()
    for _ in range(N):
        N_list.append(int(input()))

    N_list.sort()

    print(round(sum(N_list) / N))
    print(N_list[N // 2])
    cnt = Counter(N_list)
    cnt = cnt.most_common()
    cnt.sort(key=lambda x: (-x[1], x[0]))
    if len(cnt) == 1:
        print(cnt[0][0])
    elif len(cnt) >= 2:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    print(N_list[-1] - N_list[0])
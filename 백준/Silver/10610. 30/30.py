num = list(x for x in input())

num.sort(reverse=True)

if (sum(list(map(int, num))) % 3) == 0:
    if num[-1] != '0':
        print(-1)
    else:
        print(''.join(num))
else:
    print(-1)
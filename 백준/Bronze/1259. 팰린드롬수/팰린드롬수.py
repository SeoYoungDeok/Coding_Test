import sys

N = input()

while N != '0':
    if int(N) >= 1 and int(N) <= 9:
        print("yes")
    elif int(N) >= 10 and int(N) <= 999:
        if N[0] == N[-1]:
            print("yes")
        else:
            print("no")
    else:
        n = len(N) // 2
        flag = 0
        for i in range(0, n):
            if N[i] == N[-(i+1)]:
                pass
            else:
                flag = 1
                break
        if flag:
            print("no")
        else:
            print("yes")

    N = input()
import sys

input = sys.stdin.readline

while True :
    try :
        N = int(input().rstrip())
    except :
        break

    answer = 0
    i = 1
    while True:
        answer = (answer * 10) + 1
        answer %= N
        if answer == 0:
            print(i)
            break
        i += 1
import sys

N = int(input())

n = 0
cnt = 0
while True:
    if str(n).find('666') != -1:
        cnt += 1
    if cnt == N:
        print(n)
        break
    n += 1
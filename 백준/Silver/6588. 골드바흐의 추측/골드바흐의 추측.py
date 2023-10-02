import sys
import math

input = sys.stdin.readline
prime = [False] * 1_000_001
prime[2] = True

for i in range(3, 1_000_000+1):
    flag = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        prime[i] = True
    else:
        prime[i] = False

n = int(input().rstrip())

while n != 0:
    i = 3
    flag = False
    while i <= len(prime)//2:
        if prime[i] and (prime[n-i]):
            print(f'{n} = {i} + {n-i}')
            flag = True
            break
        i += 1
    if not flag:
        print("Goldbach's conjecture is wrong.")

    n = int(input().rstrip())
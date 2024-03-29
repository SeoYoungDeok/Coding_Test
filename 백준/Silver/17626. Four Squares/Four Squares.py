import sys
import math

input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
dp[1] = 1

if N == int(math.sqrt(N)) ** 2:
    print(1)
else:
    for i in range(2, N+1):
        if i == int(math.sqrt(i)) ** 2:
            dp[i] = 1
        else:
            tmp=[]
            for j in range(1, math.floor(math.sqrt(i))+1):
                tmp.append(dp[i-(j**2)]+1)
            dp[i] = min(tmp)
    print(dp[N])
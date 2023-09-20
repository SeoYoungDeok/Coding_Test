import sys

dp = [0 for i in range(1_000_000+1)]
for i in range(1, 1_000_000+1):
    j = 1
    while i*j <= 1_000_000:
        dp[i*j] += i
        j += 1
    dp[i] += dp[i-1]

input = sys.stdin.readline
n = int(input().rstrip())

for i in range(n):
    N = int(input().rstrip())
    print(dp[N])
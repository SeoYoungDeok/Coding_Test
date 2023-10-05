import sys

input = sys.stdin.readline

N = int(input())

step = list()

for _ in range(N):
    step.append(int(input()))

if N <= 2:
    print(sum(step))
else:
    dp = [0] * 301

    dp[0] = step[0]
    dp[1] = max(dp[0] + step[1], step[1])
    dp[2] = max(dp[0] + step[2], step[1] + step[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i])

    print(dp[N-1])
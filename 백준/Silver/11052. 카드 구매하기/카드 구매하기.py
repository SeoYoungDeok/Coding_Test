import sys

input = sys.stdin.readline

N = int(input().rstrip())
p = [0] + list(map(int, input().rstrip().split()))
dp = [0] * (N + 1)

for i in range(N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j])

print(dp[N])
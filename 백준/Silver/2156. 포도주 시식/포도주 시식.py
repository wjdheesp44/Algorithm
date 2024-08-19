import sys
input = sys.stdin.readline

n = int(input())
wines = [0] + list(int(input()) for _ in range(n))

dp = [0] * (n+1)

if n >= 1:
    dp[1] = wines[1]
if n >= 2:
    dp[2] = wines[1] + wines[2]

for i in range(3, n+1):
    dp[i] = max(wines[i] + wines[i-1] + dp[i-3], wines[i] + dp[i-2], dp[i-1])

print(dp[n])
import sys
input = sys.stdin.readline

dp = [0] * 5001
dp[0] = 1

for n in range(2, 5001, 2):
    for k in range(0, n, 2):
        dp[n] = (dp[n] + dp[k] * dp[n - 2 - k]) % 1000000007

T = int(input())
for _ in range(T):
    L = int(input())
    print(dp[L])
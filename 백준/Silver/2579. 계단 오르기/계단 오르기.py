import sys
input = sys.stdin.readline

n = int(input())
steps = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)

if n >= 1:
    dp[1] = steps[1]
if n >= 2:
    dp[2] = steps[1] + steps[2]
# dp[3] = max(steps[1] + steps[2], steps[1] + steps[3])

# print(dp, steps)

for i in range(3, n+1):
    dp[i] = max(steps[i] + steps[i-1] + dp[i-3], steps[i] + dp[i-2])
# print(dp)
print(dp[n])
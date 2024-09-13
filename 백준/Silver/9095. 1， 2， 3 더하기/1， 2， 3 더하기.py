import sys
input = sys.stdin.readline

T = int(input())

def count(n):
    if n == 1:  # 1
        return 1
    elif n == 2:    # 1+1, 2
        return 2

    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

for i in range(T):
    n = int(input())
    print(count(n))
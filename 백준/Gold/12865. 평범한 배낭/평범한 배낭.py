import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = [0 for _ in range(n+1)]
v = [0 for _ in range(n+1)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())

for i in range(1, n+1): # 배낭들
    for j in range(1, k+1): # 무게
        if j - w[i] >= 0:   # i번째 배낭을 선택한 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:   # 선택하지 않은 경우
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
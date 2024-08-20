import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())    # 공사 중인 도로의 개수

blocked = set()
for _ in range(K):
    a, b, c, d = map(int, input().split())
    blocked.add((a, b, c, d))
    blocked.add((c, d, a, b))

dp = [[0] * (N+1) for _ in range(M+1)]
dp[0][0] = 1

for i in range(1, N+1):
    if (i-1, 0, i, 0) not in blocked:
        dp[0][i] = dp[0][i-1]
    else:
        break

for j in range(1, M+1):
    if (0, j-1, 0, j) not in blocked:
        dp[j][0] = dp[j-1][0]
    else:
        break

for i in range(1, M+1):
    for j in range(1, N+1):
        if (j-1, i, j, i) not in blocked:
            dp[i][j] += dp[i][j-1]
        if (j, i-1, j, i) not in blocked:
            dp[i][j] += dp[i-1][j]

print(dp[M][N])

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

def count(N, M):
    for i in range(N):
        for j in range(M):
            dp[i][j] = graph[i+1][j+1] + max(dp[i-1][j], dp[i][j-1])
    return dp[N-1][M-1]

print(count(N, M))
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
answer = sum(cost)

dp = [[0]*(sum(cost)+1) for _ in range(n+1)]

for i in range(1, n+1): # 메모리량
    for j in range(0, sum(cost)+1): # 비용
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]]+memory[i])
        if dp[i][j] >= m:
            answer = min(j, answer)
        
print(answer)
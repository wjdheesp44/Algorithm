import sys
input = sys.stdin.readline

def dfs(x, y, lst):
    if len(lst) == 6:
        result.add(lst)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, lst + graph[nx][ny])

graph = [input().split() for _ in range(5)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(result))

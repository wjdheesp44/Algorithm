import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
                if graph[nx][ny] == '#':
                    q.append((nx, ny))
                    visited[nx][ny] = 1

T = int(input())

for t in range(T):
    H, W = map(int, input().split())
    graph = [list(input().strip()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)
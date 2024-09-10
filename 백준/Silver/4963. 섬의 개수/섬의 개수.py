import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    island_cnt = 0

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        while q:
            x, y = q.popleft()
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]:
                bfs(i, j)
                island_cnt += 1

    print(island_cnt)
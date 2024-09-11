import sys, math
from collections import deque

input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(x, y):
    global m, check

    q = deque([(x, y)])
    cnt = 1
    farm[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and farm[nr][nc] == 0:
                farm[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))

    m -= math.ceil(cnt / k)

n, m, k = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]
check = 0

for i in range(n):
    for j in range(n):
        if farm[i][j] == 0:
            check += 1
            bfs(i, j)

print(f'POSSIBLE\n{m}' if m >= 0 and check > 0 else 'IMPOSSIBLE')

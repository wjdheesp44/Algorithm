import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
house_cnt = []
cnt = 0

def bfs(x, y):
    h_cnt = 1
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                h_cnt += 1
                q.append((nx, ny))
    return h_cnt

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j] == 0:
            house_cnt.append(bfs(i, j))
            cnt += 1

house_cnt.sort()
print(cnt)

for i in house_cnt:
    print(i)
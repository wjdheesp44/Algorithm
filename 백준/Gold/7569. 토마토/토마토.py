import sys
from collections import deque
input = sys.stdin.readline

col, row, h = map(int, input().split())

board = []
for _ in range(h):
    board.append([list(map(int, input().split())) for _ in range(row)])

visited = [[[0] * col for _ in range(row)] for _ in range(h)]
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()

for k in range(h):
    for i in range(row):
        for j in range(col):
            if board[k][i][j] == 1:
                q.append((i, j, k))
                visited[k][i][j] = 1

while q:
    x, y, z = q.popleft()

    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < row and 0 <= ny < col and 0 <= nz < h and visited[nz][nx][ny] == 0 and board[nz][nx][ny] == 0:
            q.append((nx, ny, nz))
            visited[nz][nx][ny] = visited[z][x][y] + 1



min_date = 0
flag = False
for k in range(h):
    for i in range(row):
        for j in range(col):
            if visited[k][i][j] == 0 and board[k][i][j] == 0:
                flag = True
            else:
                min_date = max(min_date, visited[k][i][j])

if flag:
    print(-1)
else:
    print(min_date-1)
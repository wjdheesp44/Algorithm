import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
dist = []
result = 0
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))

result = max(max(row) for row in board)
print(result - 1)
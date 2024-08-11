import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

    return cnt


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
totalHouse = []
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if board[i][j] and not visited[i][j]:
            totalHouse.append(bfs(i, j))

totalHouse.sort()
print(len(totalHouse))
for i in range(len(totalHouse)):
    print(totalHouse[i])
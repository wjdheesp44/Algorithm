import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

T = int(input())

for test_case in range(T):
    def bfs(x, y):
        visited[x][y] = 1
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    m, n, k = map(int, input().split()) # 가로(열), 세로(행), 배추 개수
    result = 0
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1
        
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)
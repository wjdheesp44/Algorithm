import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    fish = []
    length = 0

    while q:
        x, y = q.popleft()
        if length == visited[x][y]: # q에서 x, y꺼냈을 때, length랑 같으면 그 구역을 다 탐색했다는 의미
            return fish, length-1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and shark_size >= board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

                if shark_size > board[nx][ny] and board[nx][ny] != 0:
                    fish.append((nx, ny))
                    length = visited[nx][ny]

    return fish, length-1

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            x, y = i, j

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
shark_size = 2
eat_cnt = 0
ans = 0

while True:

    fish, length = bfs(x, y)
    fish.sort(key = lambda x : (x[0], x[1]))

    if len(fish) == 0:
        print(ans)
        break

    x, y = fish[0]
    board[x][y] = 0
    eat_cnt += 1
    ans += length

    if eat_cnt == shark_size:
        eat_cnt = 0
        shark_size += 1
    


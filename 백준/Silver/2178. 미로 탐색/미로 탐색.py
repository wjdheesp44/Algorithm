from collections import deque

row, col = map(int, input().split())
grid = []

for i in range(row):
    grid.append(list(map(int, input().strip())))

visited = [[False] * col for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0, 1))
visited[0][0] = True

while q:
    cur_x, cur_y, cur_len = q.popleft()
    if cur_x == row - 1 and cur_y == col - 1:
        print(cur_len)
        break;

    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        if next_x >= 0 and next_x < row and next_y >=0 and next_y < col:
            if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                q.append((next_x, next_y, cur_len + 1))
                
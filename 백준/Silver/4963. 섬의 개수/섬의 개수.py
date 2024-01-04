from collections import deque

while(True):
    col, row = map(int, input().split())

    if col == 0 and row == 0:
        break

    grid = []

    for i in range(row):
        grid.append(list(map(int, input().split())))


    Islands_count = 0
    row = len(grid)
    col = len(grid[0])
    visited = [[False] * col for _ in range(row)]


    def bfs(x, y):
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        visited[x][y] = True
        q = deque()
        q.append((x, y))

        while q:
            cur_x, cur_y = q.popleft()
            for i in range(8):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                    if grid[next_x][next_y] != 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                Islands_count += 1

    print(Islands_count)




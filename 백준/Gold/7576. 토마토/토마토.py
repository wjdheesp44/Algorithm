from collections import deque

col, row = map(int, input().split())
grid = []
q = deque()

for i in range(row):
    grid.append(list(map(int, input().split())))

visited = [[0] * col for _ in range(row)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
min_date = 0       


for i in range(row):
    for j in range(col):
        if grid[i][j] == 1:
            q.append((i, j))

while q:
    cur_x, cur_y = q.popleft()
    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
            if grid[next_x][next_y] == 0:
                q.append((next_x, next_y))
                grid[next_x][next_y] = 1
                visited[next_x][next_y] = visited[cur_x][cur_y] + 1

for i in range(row):
        for j in range(col):
            if visited[i][j] > min_date:
                min_date = visited[i][j]

for i in range(row):
    for j in range(col):
        if grid[i][j] == 0:
            min_date = -1;
            
        
print(min_date)
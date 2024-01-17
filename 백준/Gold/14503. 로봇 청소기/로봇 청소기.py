row, col = map(int, input().split())
x, y, d = map(int, input().split())

room = []
for i in range(row):
    room.append(list(map(int, input().split())))

clear_room = 0
dirty = False
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while(True):
    if room[x][y] == 0:
        clear_room += 1
        room[x][y] = 2
    for i in range(4): 
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < row and ny >= 0 and ny < col:
            if room[nx][ny] == 0:
                dirty = True
                break
    
    if dirty == False:
        if room[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x -= dx[d]
            y -= dy[d]
            continue

    if dirty == True:
        d = (d + 3) % 4
        if  room[x+dx[d]][y+dy[d]] == 0:
            x += dx[d]
            y += dy[d]
        dirty = False

print(clear_room)

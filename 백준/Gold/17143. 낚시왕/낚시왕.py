import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

if M == 0:
    print(0)
    exit(0)

board = [[[] for i in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1].append([s, d, z])
opp = {1:2, 2:1, 3:4, 4:3}
w = 2*C-2
h = 2*R-2

wtbl = [n for n in range(C)] + [n for n in range(C-2, 0, -1)]
htbl = [n for n in range(R)] + [n for n in range(R-2, 0, -1)]
result = 0

speed = 0
dir = 1
shark_size = 2

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def shark_move(x, y, s, d):
    if d >= 3:  # 좌우
        if d == 3:
            dr = 1  #우
        else:
            dr = -1 #좌
        y = (y + s*dr) % w 
        if y >= C:
            y = wtbl[y] # 좌표 변환
            d = opp[d]  # 방향 반대
    else:
        if d == 2:  # 밑
            dr = 1
        else:
            dr = -1
        x = (x + s*dr) % h
        if x >= R:
            x = htbl[x]
            d = opp[d]

    return x, y, d

# 낚시왕 이동
for cnt in range(C):   # 낚시왕의 열 위치 C
    
    for i in range(R): # 2번
        if len(board[i][cnt]) > 0:
            result += board[i][cnt][0][shark_size]
            board[i][cnt].pop()
            break   # 상어 잡아서 나옴

    # 3. 상어 이동
    move = [[[] for i in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if len(board[i][j]) > 0:
                now_speed = board[i][j][0][speed]
                now_dir = board[i][j][0][dir]
                now_size = board[i][j][0][shark_size]
                nx, ny, next_dir = shark_move(i, j, now_speed, now_dir)
                tlst = [now_speed, next_dir, now_size]
                
                move[nx][ny].append(tlst)

    board = move
    
    for i in range(R):
        for j in range(C):
            if len(board[i][j]) > 1:
                shark_cnt = len(board[i][j])
                tlst = board[i][j]
                max_shark = max(tlst, key = lambda x: x[shark_size])
                board[i][j] = [max_shark]

print(result)

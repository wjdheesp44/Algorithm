import sys
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

x = y = n//2
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

ax=[[-2,-1,-1,-1, 0, 1, 1, 1, 2, 0],
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1],
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0],
    [ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1]]
ay=[[ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1],
    [-2,-1,-1,-1, 0, 1, 1, 1, 2, 0],
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1],
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0]]

mul = [2, 10, 7, 1, 5, 10, 7, 1, 2, 0]

result = dir = flag = cnt = 0
cnt_max = 1
arr = [[0] * n for _ in range(n)]


while (x, y) != (0, 0):
    x, y = x + dx[dir], y + dy[dir]
    cnt += 1

    val = board[x][y]
    board[x][y] = 0
    dust_total = 0

    for i in range(10):
        nx = x + ax[dir][i]
        ny = y + ay[dir][i]
        t = (val * mul[i]) // 100

        if i == 9:
            t = val - dust_total

        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += t

        else:
            result += t
        dust_total += t


    if cnt_max == cnt:  # 방향 전환
        cnt = 0
        dir = (dir + 1) % 4
        if flag == 0:
            flag = 1
        else:
            flag = 0
            cnt_max += 1
            
print(result)
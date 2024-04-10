import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
fish = []
bottom = len(fish)-1
result_cnt = 0

fish = list(map(int, input().split()))

while True:
    min_fishbowl = min(fish)
    for i in range(n):
        if fish[i] == min_fishbowl:
            fish[i] += 1
    board = []

    for i in range(len(fish)):
        board.append([fish[i]])

    if not board:
        break
    temp = board.pop(0)
    board[0].append(temp[0])

    def fish_control(board):
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        x, y = 0, 0
        max_r = len(board)
        max_c = len(board[0])
        temp = [[0]*(max_c+2) for _ in range(max_r+2)]
        control = set()
        big = 0
        small = 0
        bx = by = sx = sy = 0

        for i in range(1, len(board)+1):
            for j in range(1, len(board[i-1])+1):
                temp[i][j] = board[i-1][j-1]

        for x in range(1, len(board) + 1):
            for y in range(1, len(board[x - 1]) + 1):
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if temp[nx][ny] != 0:
                        if temp[x][y] >= temp[nx][ny]:
                            big = temp[x][y]
                            bx, by = x, y
                            small = temp[nx][ny]
                            sx, sy = nx, ny
                        else:
                            big = temp[nx][ny]
                            bx, by = nx, ny
                            small = temp[x][y]
                            sx, sy = x, y

                        d = (big - small) // 5
                        if d > 0:
                            control.add((bx, by, sx, sy, d))

        for bx, by, sx, sy, d in control:
            board[bx-1][by-1] -= d
            board[sx-1][sy-1] += d

        return board

    while True:
        total = []
        origin = [x[:] for x in board]
        if len(board) == len(board[0]):
            break

        while board and len(board[0]) >= 2:
            total.append(board.pop(0))

        if len(total[0]) > len(board):
            board = [x[:] for x in origin]
            break

        for j in range(len(total)):
            temp = total.pop()
            for t in range(len(temp)):
                board[t].append(temp[t])




    board = fish_control(board)
    # 바닥에 놓기
    fish = []
    for i in range(len(board)):
        for j in board[i]:
            fish.append(j)

    big_temp = []
    temp = []
    for i in range(n//2-1, -1, -1):
        temp.append(fish[i])
    big_temp.append(temp)

    temp = []
    for i in range(n//2, n):
        temp.append(fish[i])
    big_temp.append(temp)
    fish = big_temp


    big_temp = []
    for j in (1, 0):
        temp = []
        for i in range(n//4-1, -1, -1):
            temp.append(fish[j][i])
        big_temp.append(temp)

    for j in (0, 1):
        temp = []
        for i in range(n//4, n//2):
            temp.append(fish[j][i])
        big_temp.append(temp)
    board = big_temp

    board = fish_control(board)


    # 바닥에 놓기
    fish = []
    for j in range(len(board[0])):
        for i in range(len(board)-1, -1, -1):
            fish.append(board[i][j])

    if max(fish) - min(fish) <= k:
        result_cnt += 1
        print(result_cnt)
        break
    else:
        result_cnt += 1

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

magic = [list(map(int, input().split())) for _ in range(m)]

result = 0
# for i in range(n):
#     print(board[i])

shark_x, shark_y = (n-1)//2, (n-1)//2
# print(shark_x, shark_y)
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

ax = [0, 1, 0, -1]
ay = [-1, 0, 1, 0]

def move():
    pos = []
    q = deque()
    temp = [[0] * n for _ in range(n)]

    # 달팽이 모양
    flag = cnt = dir = 0
    cnt_max = 1
    x, y = shark_x, shark_y
    while (0, 0) != (x, y):
        cnt += 1
        nx, ny = x + ax[dir], y + ay[dir]
        # temp[nx][ny] = temp[x][y] + 1
        if board[nx][ny] != 0:
            q.append(board[nx][ny])
            pos.append(board[nx][ny])
        if cnt_max == cnt:
            cnt = 0
            dir = (dir + 1) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                cnt_max += 1
        x, y = nx, ny

    # print()
    # print(q)

    flag = cnt = dir = 0
    cnt_max = 1
    x, y = shark_x, shark_y
    while q:
        cnt += 1
        nx, ny = x + ax[dir], y + ay[dir]
        # temp[nx][ny] = temp[x][y] + 1
        temp[nx][ny] = q.popleft()
        if cnt_max == cnt:
            cnt = 0
            dir = (dir + 1) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                cnt_max += 1
        x, y = nx, ny
    return temp, pos

for magic_cnt in range(m):  # m
    pos = []
    d, s = magic[magic_cnt][0], magic[magic_cnt][1]

    # 1. 구슬 파괴
    x, y = shark_x, shark_y
    for k in range(s):
        nx = x + dx[d]
        ny = y + dy[d]
        # print(nx, ny)
        board[nx][ny] = 0
        x, y = nx, ny

    # print("구슬파괴 후")
    # for b in range(n):
    #     print(board[b])

    # 2. 구슬 이동

    temp, pos = move()
    board = [x[:] for x in temp]
    # for t in range(n):
    #     print(board[t])

    # 3. 구슬 폭발
    # print(pos)
    i = 0
    j = 1
    bomb_cnt = 0
    bomb = []
    delete = True
    while delete:
        delete = False
        i, j = 0, 1
        while j < len(pos):
            while True:
                # print(i, j, len(pos))
                if j < len(pos) and pos[i] == pos[j]:
                    # print("same:", i, j)
                    bomb.append(i)
                    j += 1

                else:
                    if len(bomb) >= 3:
                        delete = True
                        result += (len(bomb) + 1) * pos[bomb[0]]
                        # print(pos[bomb[0]])
                        # print("result:", result)
                        for _ in range(len(bomb)+1):
                            pos.pop(bomb[0])

                        # print("pos:", pos)


                        bomb = []
                        # print(i, j)
                        j = i + 1
                        # print(i, j)
                        # print()
                    else:
                        if len(bomb) > 0:
                            j -= len(bomb)
                            bomb = []
                            # print('no:', i,j )
                        i += 1
                        j += 1
                    break
        # print("d:", delete)
    # print(pos)

    # 4. 구슬 변환

    i = 0
    j = 1
    bomb_cnt = 0
    pos_temp = []
    bomb = []
    while j < len(pos):
        cnt = 1
        while True:
            if j < len(pos) and pos[i] == pos[j]:
                # print("same:", i, j)
                cnt += 1
                # bomb.append(i)
                j += 1

            else:

                # print(cnt, pos[i], i, j)
                pos_temp.append(cnt)
                pos_temp.append(pos[i])

                j += 1
                i += cnt
                # i += 1
                # j += 1
                if j == len(pos):
                    pos_temp.append(1)
                    pos_temp.append(pos[j-1])

                break
    # print(pos_temp)



    # 판에 이동
    q = deque(pos_temp)

    temp = [[0] * n for _ in range(n)]
    flag = cnt = dir = 0
    cnt_max = 1
    x, y = shark_x, shark_y
    while q:
        cnt += 1
        nx, ny = x + ax[dir], y + ay[dir]
        # temp[nx][ny] = temp[x][y] + 1
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            break
        temp[nx][ny] = q.popleft()
        if cnt_max == cnt:
            cnt = 0
            dir = (dir + 1) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                cnt_max += 1
        x, y = nx, ny
        board = [x[:] for x in temp]

    # print("결과----------------------------------------------------")
    # for k in range(n):
    #     print(board[k])

print(result)
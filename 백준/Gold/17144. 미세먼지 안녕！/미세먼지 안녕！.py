import sys
from collections import deque
input = sys.stdin.readline

row, col, t = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(row)]

# 수정 필요

times = 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

while times < t:
    new_board = [[0] * col for _ in range(row)]
    clean = []

    for i in range(row):
        for j in range(col):
            if A[i][j] == -1:   # 공기청정기가 있으면
                clean.append((i, j))

            elif A[i][j] != 0:  # 미세먼지가 있으면
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    
                    if 0 <= nx < row and 0 <= ny < col and A[nx][ny] != -1:
                        new_board[nx][ny] += A[i][j] // 5
                        cnt += 1
                new_board[i][j] += A[i][j] - (A[i][j] // 5) * cnt

    new_board[clean[0][0]][clean[0][1]] = -1
    new_board[clean[1][0]][clean[1][1]] = -1
    A = new_board

    # 공기청정기 부분
    angle = [1, 1]
    now = 0
    a, b = clean[0][0], clean[0][1]
    na, nb = 0, 0

    while True:
        na, nb = a + dx[angle[0]], b + dy[angle[0]]
        if 0 <= na < row and 0 <= nb < col and A[na][nb] == -1:
            break
        if 0 <= na < row and 0 <= nb < col:
            next = A[na][nb]
            A[na][nb] = now
            now = next

            a, b = na, nb

        elif na < 0 or nb < 0 or na >= row or nb >= col:
            angle[0] = (angle[0] + 3) % 4
            na, nb = a, b

    
            

    angle = [1, 1]
    now = 0
    a, b = clean[1][0], clean[1][1]
    na, nb = 0, 0

    while True:
        na, nb = a + dx[angle[1]], b + dy[angle[1]]
        if 0 <= na < row and 0 <= nb < col and A[na][nb] == -1:
            break
        if 0 <= na < row and 0 <= nb < col:
            next = A[na][nb]
            A[na][nb] = now
            now = next

            a, b = na, nb

        elif na < 0 or nb < 0 or na >= row or nb >= col:
            angle[1] = (angle[1] + 1) % 4
            na, nb = a, b

    

        



    times += 1

# 미세먼지양 계산 for문, -1, 0 아니면


total = 0

for i in range(row):
    for j in range(col):
        if A[i][j] != -1:
            total += A[i][j]
print(total)
import sys

input = sys.stdin.readline

# 그냥 행렬로
dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]

stamps = set()
board = [[0]*101 for _ in range(101)]

N = int(input())
curves = []
for _ in range(N):
    y, x, d, g = map(int, input().split())
    curves.append((x, y, d, g))

dragon_curves = [[0]]
temp = []
for i in range(10):
    temp = dragon_curves[i][:]
    # print(temp)
    half = temp[::-1]
    for h in half:
        # print(h)
        temp.append(h+1)
    dragon_curves.append(temp)

for x, y, d, g in curves:
    board[x][y] = 1
    # x, y = x + dx[d], y + dy[d]
    # print("dragon:", dragon_curves[g])
    for i in dragon_curves[g]:
        dir = (i + d) % 4
        x, y = x + dx[dir], y + dy[dir]
        board[x][y] = 1
        stamps.add((x, y))

result = 0
# print("st:", len(stamps), sorted(stamps))

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

# for i in range(len(board)):
#     print(board[i])
print(result)

# 1
# 3 3 0 1
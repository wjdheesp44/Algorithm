import sys
input = sys.stdin.readline

M, n = map(int, input().split())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir = 1

for i in range(n):
    move, num = map(str, input().split())
    num = int(num)

    if move == 'MOVE':
        x += dx[dir] * num
        y += dy[dir] * num
    elif move == 'TURN':
        if num == 0:
            dir = (dir - 1) % 4
        elif num == 1:
            dir = (dir + 1) % 4
    # print(dir, x, y)
    if x < 0 or x >= M or y < 0 or y >= M:
        print(-1)
        exit(0)

print(y, x)

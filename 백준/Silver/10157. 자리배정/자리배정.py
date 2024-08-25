import sys
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
x, y = 1, 1
w, h = map(int, input().split())
K = int(input())


cnt = 1
dir = 0
toggleX = 1
toggleY = 1
while cnt < K and x > 0 and y > 0:
    if dir == 0:
        cnt += h - toggleY

        y += h - toggleY
        h -= toggleY
        if cnt == y:
            h += 1
        if cnt >= K:
            # print(cnt, K)
            y -= cnt - K

            break
    elif dir == 1:
        cnt += w - toggleX
        x += w - toggleX
        w -= toggleX
        if cnt >= K:
            # print(cnt, K)
            x -= cnt - K
    elif dir == 2:
        cnt += h - toggleY
        y -= h - toggleY
        h -= toggleY
        if cnt >= K:
            # print(cnt, K)
            y += cnt - K
    elif dir == 3:
        cnt += w - toggleX
        x -= w - toggleX
        # x += 1
        w -= toggleX
        if cnt >= K:
            # print(cnt, K)
            x += cnt - K
    # print(cnt, dir, x, y)

    dir = (dir + 1) % 4
if x < 1 or y < 1:
    print(0)
else:
    print(x, y)

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x, y, dir, cnt, arr):
    nx, ny = x + dx[dir], y + dy[dir]
    if 0 <= nx < 19 and 0 <= ny < 19 and board[x][y] == board[nx][ny]:
        arr.append((nx, ny))
        # print("dfs", nx, ny, cnt)
        return dfs(nx, ny, dir, cnt+1, arr)
    else:
        return cnt, arr


for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            for k in range(8):
                line_cnt, result = dfs(i, j, k, 1, [(i, j)])
                # print(line_cnt, result)
                if line_cnt == 5:
                    dir = (k + 4) % 8
                    nx, ny = i + dx[dir], j + dy[dir]
                    if 0 <= nx < 19 and 0 <= ny < 19 and board[i][j] == board[nx][ny]:
                        continue

                    print(board[i][j])
                    result.sort(key=lambda x: (x[1], x[0]))
                    # print(result)
                    print(result[0][0]+1, result[0][1]+1)
                    exit(0)
print(0)
import sys
input = sys.stdin.readline

cctv = [[], [0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(n, angles):
    global ans
    if n == k:
        ans = min(ans, cal(angles))
        return
    
    for i in range(4):  # cctv 한 대 당 4가지 방향의 경우의 수
        dfs(n+1, angles+[i])

def cal(angles):
    v = [[0] * col for _ in range(row)]

    for i in range(k):  # cctv 개수 만큼 경우의 수를 다 돌림
        x, y = cctv_pos[i]  # cctv의 x, y 좌표
        cctv_num = maps[x][y]   # cctv 번호
        angle = angles[i]   # cctv 방향의 경우의 수

        for dir in cctv[cctv_num]:  # cctv 번호에 해당하는 방향들을 돌림
            dir = (dir + angle) % 4
            nx, ny = x, y

            while True: # 방향대로 뻗어감
                nx, ny = nx + dx[dir], ny + dy[dir] # 쭉 뻗어나간 방향대로 누적해서 더함
                if nx < 0 or nx >= row or ny < 0 or ny >= col or maps[nx][ny] == 6:
                    break
                v[nx][ny] = 1
    cnt = 0
    for i in range(row):    # 사각지대 카운트
        for j in range(col):
            if maps[i][j] == 0 and v[i][j] == 0:
                cnt += 1
    return cnt


row, col = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(row)]

cctv_pos = []
for i in range(row):
    for j in range(col):
        if 1 <= maps[i][j] <= 5: 
            cctv_pos.append((i, j))

k = len(cctv_pos)
ans = row * col
        
dfs(0, [])
print(ans)
        
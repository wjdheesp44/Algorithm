import sys
input = sys.stdin.readline

snake_length = 1
angle = 1
time_cnt = 0
x, y = 1, 1
target = 0
visited = []
X = []
turn = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())

apple_cnt = int(input())
apple_pos = []

for i in range(apple_cnt):
    apple_pos.append(list(map(int, input().split())))

dir_change_cnt = int(input())

for i in range(dir_change_cnt):
    times, dir = input().split()
    times = int(times)
    X.append(times)
    turn.append(dir)

maps = [[0] * (n+1) for _ in range(n+1)]
for i, j in apple_pos:
    maps[i][j] = 2


while(1):
    snake_length += 1
    visited.append([x, y])

    nx = x + dx[angle]
    ny = y + dy[angle]
    
    time_cnt += 1

    if nx <= 0 or nx > n or ny <= 0 or ny > n or maps[nx][ny] == 1: # 뱀이 벽이나 자기자신에게 부딪히면 gameover
        print(time_cnt)
        break

    if maps[nx][ny] != 2:   # 이동한 칸에 사과가 없다면 -> 꼬리 부분 비워줌
        snake_length -= 1
        rx, ry = visited[time_cnt - snake_length]
        maps[rx][ry] = 0
    maps[nx][ny] = 1    # 현재 뱀이 있는 첫 번째 자리
    
    x, y = nx, ny

    if X[target] == time_cnt:   # X초가 끝난 뒤(현재 시간과 주어진 시간 비교), 회전
        if turn[target] == 'D':
            angle = (angle + 1) % 4
        elif turn[target] == 'L':
            angle = (angle + 3) % 4
        
        if target < dir_change_cnt - 1:
            target += 1
    
    
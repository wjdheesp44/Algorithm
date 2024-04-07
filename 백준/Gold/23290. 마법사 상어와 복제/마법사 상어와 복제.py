import sys
input = sys.stdin.readline

m, s = map(int, input().split())
fish = []

for _ in range(m):
    x, y, d = map(int, input().split())
    fish.append([x-1, y-1, d-1, 1])

shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1
v = [[0] * 4 for _ in range(4)]
boundary = set([(i, j) for j in range(4) for i in range(4)])

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def fish_move():
    for k in range(len(fish)):
        x, y, dir, cnt = fish[k]
        for i in range(8):
            nx, ny = x + dx[(dir - i)%8], y + dy[(dir - i)%8]

            # 격자 밖, 상어, 물고기 냄새
            if (nx, ny) in boundary and (nx, ny) != (shark_x, shark_y) and v[nx][ny] == 0:
                fish[k] = [nx, ny, (dir - i)%8, cnt]
                break


def shark_move():
    max_remove = -1
    del_set = set()
    for d1 in (2, 0, 6, 4):     # 상, 좌, 하, 우
        x1, y1 = shark_x + dx[d1], shark_y + dy[d1]
        if (x1, y1) not in boundary:
            continue
        for d2 in (2, 0, 6, 4):
            x2, y2 = x1 + dx[d2], y1 + dy[d2]
            if (x2, y2) not in boundary:
                continue
            for d3 in (2, 0, 6, 4):
                x3, y3 = x2 + dx[d3], y2 + dy[d3]
                if (x3, y3) not in boundary:
                    continue

                fish_remove = 0
                shark_in = set(((x1, y1), (x2, y2), (x3, y3)))
                for x, y, d, cnt in fish:
                    if (x, y) in shark_in:
                        fish_remove += cnt

                if max_remove < fish_remove:
                    max_remove, sh_x, sh_y  = fish_remove, x3, y3  # 사라진 물고기수, 상어 좌표
                    del_set = shark_in
                    
    for i in range(len(fish)-1, -1, -1):
        if (fish[i][0], fish[i][1]) in del_set: # 제거할 물고기라면
            v[fish[i][0]][fish[i][1]] = 3
            fish.pop(i)
    return sh_x, sh_y

def merge(fish):
    # 행, 열, 방향 순
    fish.sort(key=lambda x : (x[0], x[1], x[2]))
    i = 1
    while i < len(fish):
        if fish[i-1][:3] == fish[i][:3]:
            fish[i-1][3] += fish[i][3]
            fish.pop(i)
        else:
            i += 1

for _ in range(s):
    # 1. 복제 마법
    fish_copy = [x[:] for x in fish]

    # 2. 물고기 이동
    fish_move()

    # 3. 상어 이동
    shark_x, shark_y = shark_move()

    # 4. 물고기 냄새 삭제
    for i in range(4):
        for j in range(4):
            if v[i][j] > 0:
                v[i][j] -= 1
                
    fish += fish_copy
    merge(fish)

result = 0
# 결과 : 물고기 개수 반환
for i in range(len(fish)):
    result += fish[i][3]
print(result) 

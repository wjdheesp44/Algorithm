import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
small = 'abcdefghijklmnopqrstuvwxyz'
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(T):
    building = []
    h, w = map(int, input().split())
    building.append(['.'] * (w+2))
    for i in range(h):
        building.append(['.']+list(map(str, input().strip()))+['.'])
    building.append(['.'] * (w+2))

    keys = list(map(str, input().strip()))
    if '0' in keys:
        keys.pop(0)

    keys = [key.upper() for key in keys]

    doc = 0

    while True:
        q = deque()
        q.append((0, 0))
        visited = [[0]*(w+2) for _ in range(h+2)]
        visited[0][0] = 1
        new_key = False

        while q:
            x, y = q.popleft()
            if building[x][y] == '$':   # 문서를 발견
                doc += 1
                building[x][y] = '.'
            elif building[x][y] in small:   # 키 발견
                if building[x][y].upper() not in keys:
                    new_key = True
                    keys.append(building[x][y].upper())
                building[x][y] = '.'
            elif building[x][y] in big:    # 문 발견
                if building[x][y] not in keys:  # 열쇠가 없는 문
                    continue
                building[x][y] = '.'

            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h+2 and 0 <= ny < w+2 and not visited[nx][ny] and building[nx][ny] != '*':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if not new_key:
            break

    print(doc)
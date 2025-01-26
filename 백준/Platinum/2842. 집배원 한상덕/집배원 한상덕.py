import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(str, input())) for _ in range(N)]
heights = [list(map(int, input().split())) for _ in range(N)]

all_height = []
dx, dy = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
house = 0
sx, sy = -1, -1

for i in range(N):
    for j in range(N):
        if board[i][j] == 'P':
            sx, sy = i, j
        elif board[i][j] == 'K':
            house += 1
        all_height.append(heights[i][j])


all_height = sorted(set(all_height))

left, right = 0, 0
result = 1000000

while left <= right:
    visited = [[0] * N for _ in range(N)]
    q = deque()
    if all_height[left] <= heights[sx][sy] <= all_height[right]:
        visited[sx][sy] = 1
        q.append((sx, sy))
    visited_house = 0

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if all_height[left] <= heights[nx][ny] <= all_height[right]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    if board[nx][ny] == 'K':
                        visited_house += 1

    if visited_house == house:
        result = min(result, all_height[right] - all_height[left])
        left += 1
    elif right + 1 < len(all_height):
        right += 1
    else:
        break

print(result)
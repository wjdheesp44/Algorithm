import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
board = []
n = 2**N
for i in range(n):
    board.append(list(map(int, input().split())))

L = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for q_cnt in range(Q):  # Q
    l = 2**L[q_cnt]
    # 1. 2의 L승씩 나눔, 모든 부분 격자들 시계 방향 90도 회전
    temp = [[0]*n for _ in range(n)]
    if l != 1:
        for r in range(0, n, l):
            for c in range(0, n, l):
                for i in range(l):
                    for j in range(l):
                        temp[r+j][c+l-1-i] = board[r+i][c+j]
        board = [x[:] for x in temp]

    # 2. 얼음 3개 이상과 인접하지 않은 칸 -1 (인접한 칸 visited, 모두 탐색 후 visited 하지 않은 칸에 -1)
    melt = []
    for i in range(n):
        for j in range(n):
            ice_cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                    ice_cnt += 1
            if ice_cnt < 3:
                melt.append((i, j))

    result1 = 0
    for (i, j) in melt:
        if board[i][j] != 0:
            board[i][j] -= 1

    # 결과
    v = [[0] * n for _ in range(n)]
    def bfs(x, y):
        v[x][y] = 1
        q = deque()
        q.append((x, y))
        cnt = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and board[nx][ny] != 0:
                    cnt += 1
                    q.append((nx, ny))
                    v[nx][ny] = 1
        return cnt

    result2 = 0
    for i in range(n):
        for j in range(n):
            result1 += board[i][j]  # A[r][c]의 합
            if not v[i][j] and board[i][j] != 0:
                temp_result = bfs(i, j)
                result2 = max(result2, temp_result)

print(result1)
print(result2)
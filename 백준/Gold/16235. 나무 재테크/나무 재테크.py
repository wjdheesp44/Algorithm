import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, K = map(int, input().split())
A =  [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
ground = [[5]*(n+1) for _ in range(n+1)]

tree = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int,input().split())
    tree[x][y].append(z)


for _ in range(K):

    for i in range(1, n+1):
        for j in range(1, n+1):
            tree[i][j].sort()

            for k in range(len(tree[i][j])):   # 봄
                if ground[i][j] >= tree[i][j][k]:
                    ground[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                
                else:   # 여름
                    for _ in range(k, len(tree[i][j])): # 양분을 다 쓴 후니까
                        ground[i][j] += (tree[i][j].pop() // 2)

                    break   # for k 탈출

    for i in range(1, n+1):
        for j in range(1, n+1):
            for z in tree[i][j]:
                if z % 5 == 0:  # 번식나무
                    for k in range(8):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 < nx <= n and 0 < ny <= n:
                            tree[nx][ny].append(1)
                
            ground[i][j] += A[i][j]

result = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        result += len(tree[i][j])


print(result)


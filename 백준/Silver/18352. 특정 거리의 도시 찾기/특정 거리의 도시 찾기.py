import sys
from collections import deque
input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())
result = []

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start_v, depth):
    q = deque()
    q.append((start_v, depth))
    visited[start_v] = 1

    while q:
        x, dep = q.popleft()

        if dep == K:
            result.append(x)
            continue
        elif len(graph[x]) == 0:
            continue

        for i in range(len(graph[x])):
            nx = graph[x][i]
            if not visited[nx]:

                visited[nx] = 1
                q.append((nx, dep+1))

bfs(X, 0)
if not result:
    print(-1)
else:
    result.sort()
    for i in range(len(result)):
        print(result[i])
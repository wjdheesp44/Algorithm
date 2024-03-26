import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(num):
    visited.append(num)
    graph[num].sort()

    if len(visited) == n:
        return

    for v in graph[num]:
        if v not in visited:
            dfs(v)

def bfs(num):
    graph[num].sort()
    q = deque()
    q.append(num)
    visited.append(num)

    while q:
        cur_v = q.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                q.append(v)
                visited.append(v)

visited = []
dfs(v)
for i in visited:
    print(i, end=' ')

print()
visited = []
bfs(v)
for i in visited:
    print(i, end=' ')
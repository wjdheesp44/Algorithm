import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    cnt = 0
    visited = []
    q = deque()
    q.append(v)
    visited.append(v)

    while q:
        cur_v = q.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                cnt += 1
                q.append(v)
                visited.append(v)

    return cnt


print(bfs(1))
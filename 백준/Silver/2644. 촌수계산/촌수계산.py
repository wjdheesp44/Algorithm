import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start):
    visited = [0 for _ in range(n + 1)]
    visited[start] = 0

    q = deque()
    q.append(start)

    while q:
        person = q.popleft()
        if person == b:
            return visited[person]

        for v in graph[person]:

            if visited[v] == 0:
                visited[v] = visited[person] + 1
                q.append(v)
    return -1

print(bfs(graph, a))
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def bfs(start_v):
    q = deque()
    q.append(start_v)

    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = node   # 부모노드 설정
                q.append(i)

bfs(1)
result = visited[2:]
for i in range(len(result)):
    print(result[i])
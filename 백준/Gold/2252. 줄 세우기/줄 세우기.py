import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

in_degree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
q = deque()
answer = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)

for i in answer:
    print(i, end=' ')
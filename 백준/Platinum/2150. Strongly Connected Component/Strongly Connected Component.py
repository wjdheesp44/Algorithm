import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
reverse_graph = [[] for _ in range(V+1)]
stack = []
result = []

for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

def dfs(n, visited, stack):
    visited[n] = 1
    for next in graph[n]:
        if visited[next] == 0:
            dfs(next, visited, stack)
    stack.append(n)

def reverse_dfs(n, visited, stack):
    visited[n] = 1
    stack.append(n)
    for next in reverse_graph[n]:
        if visited[next] == 0:
            reverse_dfs(next, visited, stack)

visited = [0] * (V+1)
for i in range(1, V+1):
    if visited[i] == 0:
        dfs(i, visited, stack)

visited = [0] * (V+1)
while stack:
    ssc = []
    node = stack.pop()
    if visited[node] == 0:
        reverse_dfs(node, visited, ssc)
        result.append(sorted(ssc))

print(len(result))
results = sorted(result)

for i in results:
    print(*i, -1)


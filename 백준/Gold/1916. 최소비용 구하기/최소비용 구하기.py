import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())

dist = [1e9] * (N + 1)
dist[start] = 0

pq = [(0, start)]

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if dist[cur_node] < cur_cost:
        continue
    for next_node, next_cost in graph[cur_node]:
        total_cost = cur_cost + next_cost
        if total_cost < dist[next_node]:
            dist[next_node] = total_cost
            heapq.heappush(pq, (total_cost, next_node))

print(dist[end])
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def findCycle(start):
    isCycle = False
    q = deque()
    q.append(start)

    while q:
        cnt_node = q.popleft()
        if visited[cnt_node]:
            isCycle = True
        visited[cnt_node] = 1
        for adj_node in graph[cnt_node]:
            if visited[adj_node] == 0:
                q.append(adj_node)

    return isCycle


case_cnt = 0
while True:
    case_cnt += 1
    tree_cnt = 0
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        if not visited[i]:
            if not findCycle(i):
                tree_cnt += 1

    if tree_cnt > 1:
        print(f"Case {case_cnt}: A forest of {tree_cnt} trees.")
    elif tree_cnt == 1:
        print(f"Case {case_cnt}: There is one tree.")
    else:
        print(f"Case {case_cnt}: No trees.")

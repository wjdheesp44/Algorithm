import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = set()
    visited.add(start)
    q = deque()
    q.append((start, 0))

    while q:
        now, cnt = q.popleft()
        if now == brother:
            print(cnt)
            return
        for i in (-1, 1, now):
            next = now + i
            if 0 <= next <= 100000 and next not in visited:
                q.append((next, cnt+1))
                visited.add(next)

subin, brother = map(int, input().split())

bfs(subin)
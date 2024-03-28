import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
dir = [u, -d]

def bfs(start):
    visited = [0] * (f+1)
    q = deque()
    q.append((start, 0))

    while q:
        now, cnt = q.popleft()
        visited[now] = 1
        if now == g:
            print(cnt)
            return

        for d in dir:
            next = now + d
            if 0 < next <= f and visited[next] == 0:
                q.append((next, cnt+1))
                visited[next] = 1

    print("use the stairs")
    

bfs(s)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
a, b = map(int, input().split())
a, b = a-1, b-1

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    visited = [0] * N
    visited[a] = 0

    while q:
        # print(q)
        cur_idx, jump_cnt = q.popleft()
        if cur_idx == b:
            return jump_cnt
        # print(b // numbers[cur_idx])

        # 앞으로 점프
        for i in range(cur_idx + numbers[cur_idx], N, numbers[cur_idx]):
            if not visited[i]:
                visited[i] = 1
                q.append((i, jump_cnt + 1))

        # 뒤로 점프
        for i in range(cur_idx - numbers[cur_idx], -1, -numbers[cur_idx]):
            if not visited[i]:
                visited[i] = 1
                q.append((i, jump_cnt + 1))
    return -1

print(bfs(a, b))
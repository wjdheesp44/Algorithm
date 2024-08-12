import sys
from collections import deque
input = sys.stdin.readline


def bfs(a, b, c):
    visited = set()
    q = deque()
    q.append((0, 0, c))
    result = set()

    while q:
        x, y, z = q.popleft()
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        if x == 0:
            result.add((x, y, z))

        # A -> B
        if x + y > b:
            q.append((x - b + y, b, z))
        else:
            q.append((0, y + x, z))

        # A -> C
        if x + z > c:
            q.append((x - c + z, y, c))
        else:
            q.append((0, y, z + x))

        # B -> A
        if y + x > a:
            q.append((a, y - a + x, z))
        else:
            q.append((x + y, 0, z))

        # B -> C
        if y + z > c:
            q.append((x, y - c + z, c))
        else:
            q.append((x, 0, y + z))

        # C -> A
        if z + x > a:
            q.append((a, y, z - a + x))
        else:
            q.append((x + z, y, 0))

        # C -> B
        if z + y > b:
            q.append((x, b, z - b + y))
        else:
            q.append((x, y + z, 0))

    return sorted(result, reverse=True)

A, B, C = map(int, input().split())
result = bfs(A, B, C)

for i in range(len(result)):
    print(result[i][2], end=' ')

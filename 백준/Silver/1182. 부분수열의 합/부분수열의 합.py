import sys
input = sys.stdin.readline

def backtraking(v):
    global cnt
    if v == N:

        total = 0
        for i in range(N):
            if ch[i] == 1:
                total += graph[i]
                lst.append(graph[i])
        if total == S and len(lst) != 0:
            cnt += 1
        return

    ch[v] = 0
    backtraking(v+1)
    ch[v] = 1
    backtraking(v+1)

N, S = map(int, input().split())
graph = list(map(int, input().split()))
cnt = 0
ch = [0] * N
lst = []
backtraking(0)
print(cnt)
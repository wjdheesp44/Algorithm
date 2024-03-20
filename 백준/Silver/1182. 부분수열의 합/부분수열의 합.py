import sys
input = sys.stdin.readline

cnt = 0
lst = []

def dfs(v):
    global cnt
    if v == n:
        total = 0
        for i in range(n):
            if ch[i] == 1:
                total += input_lst[i]
                lst.append(input_lst[i])

        if total == s and len(lst) != 0:
            cnt += 1
        return
    
    ch[v] = 0
    dfs(v + 1)
    ch[v] = 1
    dfs(v + 1)

n, s = map(int, input().split())
input_lst = list(map(int, input().split()))
ch = [0] * n

dfs(0)
print(cnt)
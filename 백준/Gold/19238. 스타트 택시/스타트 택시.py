N, M, F = map(int, input().split())
arr = [[1]*(N+2)]+[[1]+list(map(int, input().split()))+[1] for _ in range(N)]+[[1]*(N+2)]

ci,cj = map(int, input().split())          
start_pos = set()
dest_pos = {}
for m in range(M):
    si,sj,ei,ej = map(int, input().split())
    start_pos.add((si,sj))                 
    dest_pos[(si,sj)]=(ei,ej)              

from collections import deque
def bfs_find(si,sj):        
    q = deque()
    v = [[0]*(N+2) for _ in range(N+2)]
    tlst = []

    q.append((si,sj))
    v[si][sj]=1

    while q:
        nq = deque()
        for ci,cj in q:
            if (ci,cj) in start_pos:
                tlst.append([ci,cj])

            for di,dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni,nj=ci+di,cj+dj
                if v[ni][nj]==0 and arr[ni][nj]==0:  
                    nq.append((ni,nj))
                    v[ni][nj]=v[ci][cj]+1

        if len(tlst)>0:
            tlst.sort()                
            ei,ej = tlst[0]
            return ei,ej,v[ei][ej]-1

        q=nq
    return 0,0,-1    

def bfs(si,sj,ei,ej):
    q = deque()
    v = [[0]*(N+2) for _ in range(N+2)]

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj=q.popleft()
        if (ci,cj)==(ei,ej):    
            return v[ci][cj]-1

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if v[ni][nj]==0 and arr[ni][nj]==0: 
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return -1

for _ in range(M):
    si,sj,dist=bfs_find(ci,cj)
    if dist==-1 or F<dist:      
        F=-1
        break
    F-=dist
    start_pos.remove((si,sj))

    ei,ej=dest_pos[(si,sj)]
    dist=bfs(si,sj,ei,ej)
    if dist==-1 or F<dist:      
        F=-1
        break

    F += dist
    ci,cj=ei,ej
print(F)
#입력값 받는 부분
n=int(input())
a,b=map(int,input().split())
m=int(input())

#기본 선언
graph=[[] for _ in range(n+1)]  #노드의 번호와 배열 번호 통일시키기 위해서 n이 아닌 n+1 사용
visited=[False for _ in range(n+1)]
result=0


for _ in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)



def dfs(v,num):
    global result
    # num+=1
    # print(visited)
    # print(v, num)
    # print()
    visited[v]=True
    if v==b:
        result = num
    
    for i in graph[v]:
        if not visited[i]:
            num += 1
            dfs(i,num)
            num -= 1

dfs(a,0)

if result==0:
    print(-1)
else:
    print(result)
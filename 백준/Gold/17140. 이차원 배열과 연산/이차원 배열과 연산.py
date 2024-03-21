from collections import Counter

def check_k(A):
    global r, c, cnt

    for ans in range(101):
        row = len(A)
        col = len(A[0])
        
        if 0 <= r < row and 0 <= c < col and A[r][c] == k:
            print(cnt)
            return
        else:
            cnt += 1
            if row >= col:
                A = cal(A)
            else: 
                A = list(map(list, zip(*A)))
                A = cal(A)
                A = list(map(list, zip(*A)))

    else:                 
        ans=-1
    print(ans)


def cal(A):   # 모든 행에 대해
    global r, c

    row = len(A)
    col = len(A[0])

    col_max = col
    
    temp1 = []
    for i in range(row):
        nH = Counter(A[i])
        nH = sorted(nH.items(), key = lambda item: (item[1], item[0]))

        temp2 = []
        for j in range(len(nH)):
            if nH[j][0] != 0:
                temp2.append(nH[j][0])
                temp2.append(nH[j][1])
        temp1.append(temp2)

        col_max = max(col_max, len(temp2))

    A = [[0] * col_max for _ in range(row)]
    for i in range(row):
        for j in range(len(temp1[i])):
            A[i][j] = temp1[i][j]
        A[i] = A[i][:100]
    
    return A

cnt = 0
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

r -= 1
c -= 1

check_k(A)

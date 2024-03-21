import sys
from collections import Counter

input = sys.stdin.readline

# 입력
r, c, k = map(int, input().split())

A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

def rc():
    max_len = 0
    for j in range(len(A)):
        a = [i for i in A[j] if i!= 0] # 정렬할 때 0은 무시
        a = Counter(a).most_common() # 수의 등장 횟수를 기준으로 정렬
        a.sort(key = lambda x: (x[1], x[0])) # 오름차순으로 정렬

        A[j] = [] # 새로운 배열을 선언하지 않고 A 배열을 재활용
        
        # 튜플로 이루어진 a를 1차원 배열로 만듦
        for key, value in a:
            A[j].append(key)
            A[j].append(value)
        
        # 길이는 최대 (수의 개수) * 2만큼 늘어날 수 있음
        if max_len < len(a) * 2:
            max_len = len(a) * 2

    for j in range(len(A)):
    	# 빈 칸은 0으로 채움
        for k in range(max_len - len(A[j])):
            A[j].append(0)
        # 처음 100개만 고려
        A[j] = A[j][:100]

for i in range(101):
    try:
        if A[r-1][c-1]==k:
            print(i)
            break
    except:
        pass
    
    # 행 개수 < 열 개수 → C 연산
    if len(A) < len(A[0]):
    	# transponse하여 정렬하고 다시 transponse
        A = list(zip(*A))
        rc()
        A = list(zip(*A))
    # 행 개수 >= 열 개수 → R 연산
    else:
        rc()

# 100초가 지나도 A[r][c] == k가 아니면 -1을 출력
else:
    print(-1)
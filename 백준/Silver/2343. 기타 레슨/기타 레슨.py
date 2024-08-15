import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lectures = list(map(int, input().split()))
# print(lectures)
lt, rt = max(lectures), sum(lectures)

while lt <= rt:
    mid = (lt + rt) // 2    # 블루레이 크기 제한
    total = 0
    cnt = 1 # 블루레이 개수 세기

    for n in lectures:
        if total + n > mid:
            cnt += 1
            total = 0
        total += n

    if cnt <= M:
        result = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(result)
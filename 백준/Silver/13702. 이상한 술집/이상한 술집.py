import sys
input = sys.stdin.readline

N, K = map(int, input().split())
alcohols = [int(input()) for _ in range(N)]

start, end = 1, sum(alcohols) // K
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(alcohol // mid for alcohol in alcohols if mid > 0)

    if cnt >= K:
        result = mid  # 가능한 최대 용량을 저장
        start = mid + 1  # 더 큰 용량을 찾기 위해 범위를 조정
    else:
        end = mid - 1  # 분배할 수 없는 경우 범위를 줄임

print(result)

import sys

input = sys.stdin.readline

def binary_search(lis, target):
    left, right = 0, len(lis)
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

T = int(input())

for t in range(1, T + 1):

    N, K = map(int, input().split())
    chart = list(map(int, input().split()))

    # LIS를 저장할 리스트
    lis = []

    for num in chart:
        # 직접 구현한 이분 탐색으로 위치를 찾음
        pos = binary_search(lis, num)
        if pos < len(lis):
            # lis[pos]가 존재하면 대체
            lis[pos] = num
        else:
            # lis[pos]가 없으면 새 값을 추가
            lis.append(num)

    # 결과 출력
    print(f'Case #{t}')
    if len(lis) >= K:
        print(1)
    else:
        print(0)

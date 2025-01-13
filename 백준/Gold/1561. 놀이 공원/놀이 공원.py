import math

# 입력 처리
n, m = map(int, input().split())
ride_times = list(map(int, input().split()))

# 이분 탐색 범위 초기화
start, end = 0, n * max(ride_times)
answer_time = 0

# 1. 이분 탐색으로 최소 시간 찾기
while start <= end:
    mid = (start + end) // 2
    total_rides = m  # 초기 상태에서 M명 탑승

    # mid 시간 동안의 총 탑승 인원 계산
    for time in ride_times:
        total_rides += mid // time

    if total_rides >= n:  # 충분히 태울 수 있는 경우
        answer_time = mid
        end = mid - 1  # 더 작은 시간 탐색
    else:  # 부족한 경우
        start = mid + 1  # 더 큰 시간 탐색

# 2. answer_time - 1까지의 총 탑승 인원 계산
total_rides = m  # 초기 상태에서 M명 탑승
for time in ride_times:
    total_rides += (answer_time - 1) // time

# 3. 마지막 아이가 타는 놀이기구 찾기
remaining = n - total_rides  # 마지막 아이까지 남은 인원 수
for i, time in enumerate(ride_times):
    if answer_time % time == 0:  # 놀이기구가 비어 있는 경우
        remaining -= 1
        if remaining == 0:
            print(i + 1)  # 1번부터 시작하는 놀이기구 번호
            break

import sys
input = sys.stdin.readline

N = int(input())

# 첫 번째 줄 입력 받기
arr = list(map(int, input().split()))
maxDP = arr[:]  # 최대값 DP 배열 초기화
minDP = arr[:]  # 최소값 DP 배열 초기화

# 나머지 줄 처리
for _ in range(N - 1):
    arr = list(map(int, input().split()))
    
    # 현재 줄에서 계산한 값을 갱신할 때 이전 값을 참조해야 하므로 임시 변수 사용
    newMaxDP = [0] * 3
    newMinDP = [0] * 3

    newMaxDP[0] = arr[0] + max(maxDP[0], maxDP[1])
    newMaxDP[1] = arr[1] + max(maxDP[0], maxDP[1], maxDP[2])
    newMaxDP[2] = arr[2] + max(maxDP[1], maxDP[2])

    newMinDP[0] = arr[0] + min(minDP[0], minDP[1])
    newMinDP[1] = arr[1] + min(minDP[0], minDP[1], minDP[2])
    newMinDP[2] = arr[2] + min(minDP[1], minDP[2])

    # 계산된 값을 DP 배열에 갱신
    maxDP = newMaxDP[:]
    minDP = newMinDP[:]

# 마지막 줄에서 최대값과 최소값 출력
print(max(maxDP), min(minDP))

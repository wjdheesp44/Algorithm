def func(x, y):
    global arr
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    tmp = 1
    i = 0
    while True:
        if tmp == K:  # K번째 사람이면 멈추기
            return x + 1, y + 1  # x,y가 1,1 부터 시작하므로
        arr[y][x] = True  # 지나간 점 체크
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < C and 0 <= ny < R):  # 다음 점이 범위안이고
            if arr[ny][nx] != True:  # 지나간 점이 아니라면
                x = nx  # 이동하기
                y = ny
                tmp += 1
            else:  # 지나간 점이면 방향 바꾸기
                i = (i + 1) % 4
        else:  # 다음 점이 범위를 벗어나면 방향 바꾸기
            i = (i + 1) % 4


C, R = map(int, input().split())
K = int(input())
arr = [[False for _ in range(C + 1)] for _ in range(R + 1)]  # 다음점까지 고려해서 1개씩 더 큰 배열 만들기
if K > C * R:
    print(0)
else:
    print(*func(0, 0))
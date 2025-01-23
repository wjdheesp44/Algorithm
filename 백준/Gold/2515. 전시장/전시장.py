import sys

input = sys.stdin.readline
# 입력 받기
N, S = map(int, input().split())
paintings = []

for _ in range(N):
    H, C = map(int, input().split())
    paintings.append((H, C))

paintings_dict = dict()
max_height = 0

# 그림 높이와 가격을 사전에 저장하고 최대 높이 계산
for H, C in paintings:
    max_height = max(max_height, H)
    if H in paintings_dict:
        paintings_dict[H] = max(paintings_dict[H], C)
    else:
        paintings_dict[H] = C

# DP 배열 생성
heights = [0] * (max_height + 1)

for h in range(1, max_height + 1):
    if h in paintings_dict:
        new_cost = paintings_dict[h]
        if h - S >= 0:
            new_cost += heights[h - S]
        heights[h] = max(heights[h - 1], new_cost)
    else:
        heights[h] = heights[h - 1]

# 결과 출력
print(heights[-1])
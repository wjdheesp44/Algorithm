import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
dp_small = graph[:]
dp_big = graph[:]

for i in range(N-1):
    graph = list(map(int, input().split()))

    temp_small = [0] * 3
    temp_small[0] = min(dp_small[0], dp_small[1]) + graph[0]
    temp_small[1] = min(dp_small[0], dp_small[1], dp_small[2]) + graph[1]
    temp_small[2] = min(dp_small[1], dp_small[2]) + graph[2]

    temp_big = [0] * 3
    temp_big[0] = max(dp_big[0], dp_big[1]) + graph[0]
    temp_big[1] = max(dp_big[0], dp_big[1], dp_big[2]) + graph[1]
    temp_big[2] = max(dp_big[1], dp_big[2]) + graph[2]

    dp_small = temp_small[:]
    dp_big = temp_big[:]

print(max(dp_big[0], dp_big[1], dp_big[2]), min(dp_small[0], dp_small[1], dp_small[2]))
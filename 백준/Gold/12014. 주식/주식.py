import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):

    N, K = map(int, input().split())
    chart = list(map(int, input().split()))

    # chart = []
    # for idx, i in enumerate(temp):
    #     chart.append((idx, i))

    # chart.sort(key=lambda x:(x[1], x[0]))
    # print(chart)
    length = [1] * N
    for k in range(N):
        for i in range(k):
            if chart[i] < chart[k]:
                length[k] = max(length[k], length[i]+1)

    # print(length)
    print(f'Case #{t}')
    if max(length) >= K:
        print(1)
    else:
        print(0)


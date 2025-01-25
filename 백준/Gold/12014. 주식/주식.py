import sys

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):

    N, K = map(int, input().split())
    chart = list(map(int, input().split()))

    lis = []
    
    for k in range(N):
        start, end = 0, len(lis)

        while start < end:
            mid = (start + end) // 2
            if lis[mid] < chart[k]:
                start = mid + 1
            else:
                end = mid

        if start < len(lis):
            lis[start] = chart[k]
        else:
            lis.append(chart[k])

    print(f'Case #{t}')
    if len(lis) >= K:
        print(1)
    else:
        print(0)
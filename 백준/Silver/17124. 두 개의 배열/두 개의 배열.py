import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    B.sort()
    sum = 0

    for num in A:
        closeNum = B[0]
        minDiff = abs(num - closeNum)
        lt = 0
        rt = m - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            if B[mid] == num:
                closeNum = num
                break
            elif B[mid] > num:
                rt = mid - 1
            else:
                lt = mid + 1

            cal = abs(num - B[mid])

            if minDiff > cal or (minDiff == cal and closeNum > B[mid]):
                minDiff = cal
                closeNum = B[mid]

        sum += closeNum

    print(sum)
import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())

x1 = list(map(int, input().split()))
x2 = list(map(int, input().split()))

x1.sort()
x2.sort()
result = 0

if N % 2 == 1:
    result += x1[-1]
    x1.pop()
    N -= 1

while N > 0:
    # print(x1, x2, N)
    if len(x1) >= 2 and len(x2) >= 1 and x1[-1] + x1[-2] >= x2[-1]:
        result += x1[-1] + x1[-2]
        x1.pop()
        x1.pop()
        N -= 2
        # print('1')
    elif len(x1) >= 2 and len(x2) >= 1 and x1[-1] + x1[-2] < x2[-1]:
        result += x2[-1]
        x2.pop()
        N -= 2
        # print('2')
    elif len(x2) > 0:
        result += x2[-1]
        x2.pop()
        N -= 2
        # print('3')
    else:
        result += x1[-1]
        x1.pop()
        N -= 1
        # print('4')


#     print("r:", result)
#
# print(x1, x2)
print(result)


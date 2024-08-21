import sys
input = sys.stdin.readline

N, K = map(int, input().split())
hamburger = list(input().strip())
table = [0] * N
num = 0

for i in range(N):
    if hamburger[i] == 'H':
        table[i] = 1

for blank in range(N):
    if hamburger[blank] == 'P':
        isEat = False

        for i in range(K, 0, -1):
            if 0 <= blank - i and table[blank - i]:
                table[blank - i] = 0
                isEat = True
                num += 1
                break
        for i in range(1, K+1):
            if isEat:
                break
            if blank + i < N and table[blank + i]:
                table[blank + i] = 0
                num += 1
                break
print(num)


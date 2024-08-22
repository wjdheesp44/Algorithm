import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
total = []
result = 0

for i in range(n):
    total.append([H[i], A[i]])

total.sort(key=lambda x : x[1])

for i in range(n):
    result += total[i][0] + total[i][1] * i

print(result)
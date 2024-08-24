import sys
input = sys.stdin.readline

N, K = map(int, input().split())

student = list(map(int,input().split()))
team = N // K
diff = []

for i in range(1, N):
    diff.append(student[i] - student[i-1])

diff.sort()
print(sum(diff[:N-K]))
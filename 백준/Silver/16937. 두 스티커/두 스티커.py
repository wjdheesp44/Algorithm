import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
R = []
C = []
area = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

for i in range(N):
    for j in range(i+1, N):

        if (C[i] + C[j] <= W and max(R[i], R[j]) <= H) or (C[i] + C[j] <= H and max(R[i], R[j]) <= W):
            area.append(R[i] * C[i]+R[j] * C[j])
        if (R[i] + C[j] <= W and max(R[j], C[i]) <= H) or (R[i] + C[j] <= H and max(R[j], C[i]) <= W):
            area.append(R[i]*C[i]+R[j]*C[j])
        if (R[j] + C[i] <= W and max(R[i], C[j]) <= H) or (R[j] + C[i] <= H and max(R[i], C[j]) <= W):
            area.append(R[i] * C[i] + R[j] * C[j])
        if (R[i] + R[j] <= W and max(C[j], C[i]) <= H) or (R[i] + R[j] <= H and max(C[j], C[i]) <= W):
            area.append(R[i] * C[i] + R[j] * C[j])

if area:
    print(max(area))
else:
    print(0)
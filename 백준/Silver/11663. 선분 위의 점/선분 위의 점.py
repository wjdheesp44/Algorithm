import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N, M = map(int, input().split())  
points = list(map(int, input().split()))  
segments = [tuple(map(int, input().split())) for _ in range(M)] 

points.sort()

results = []

for lt, rt in segments:
    left_idx = bisect_left(points, lt)
    right_idx = bisect_right(points, rt)
    results.append(right_idx - left_idx)

for result in results:
    print(result)
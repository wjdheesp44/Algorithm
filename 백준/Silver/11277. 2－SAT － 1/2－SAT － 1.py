import sys
from itertools import *

input = sys.stdin.readline
N, M = map(int, input().split())
boolean = [0, 1]
CNF = [list(map(int, input().split())) for _ in range(M)]
for bools in product(boolean, repeat=N):
    is_ok = True
    for i, j in CNF:
        xi, xj = bools[abs(i)-1], bools[abs(j)-1]
        if i < 0:
            xi = not xi
        if j < 0:
            xj = not xj
        if not (xi or xj):
            is_ok = False
            break
    if is_ok:
        print(1)
        break
else:
    print(0)

import sys

input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
maxBudget = int(input())
result = 0


lt = 1
rt = max(budgets)
while lt <= rt:
    mid = (lt + rt) // 2
    total = 0
    for budget in budgets:
        if budget <= mid:
            total += budget
        else:
            total += mid
    if total <= maxBudget:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(result)
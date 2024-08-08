import sys
input = sys.stdin.readline

def dfs(num, lst):
    if len(lst) == k+1:
        nums.append(lst)
        return

    for i in range(10):
        if i not in lst:
            if inequals[len(lst)-1] == '<':
                if num < i:
                    dfs(i, lst + [i])
            elif inequals[len(lst)-1] == '>':
                if num > i:
                    dfs(i, lst + [i])

k = int(input())
inequals = list(input().split())
nums = []

for i in range(10):
    dfs(i, [i])

print(''.join(map(str, nums[-1])))
print(''.join(map(str, nums[0])))
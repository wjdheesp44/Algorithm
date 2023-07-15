import sys

input = sys.stdin.readline
n = int(input())
a = map(int, input().split())

hash = {}
for num in a:
    hash[num] = hash.setdefault(num, 0) + 1

m = int(input())
b = map(int, input().split())
for num in b:
    print(hash.setdefault(num, 0), end=' ')
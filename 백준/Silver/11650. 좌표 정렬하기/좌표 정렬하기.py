import sys

num = int(sys.stdin.readline())
numbers = []

for _ in range(num):
  x, y = map(int, sys.stdin.readline().split())
  numbers.append((x, y))

numbers.sort()

for i in range(num):
  print(numbers[i][0], numbers[i][1])
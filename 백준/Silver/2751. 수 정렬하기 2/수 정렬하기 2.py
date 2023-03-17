import sys

cnt = int(input())
book = []

for i in range(cnt):
  num = int(sys.stdin.readline())
  book.append(num)

book.sort()
for i in book:
  print(i)
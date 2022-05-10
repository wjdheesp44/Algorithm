num = int(input())

for i in range(num, 0, -1):
  for j in range(i):
    print("*", end="")
  print()
    
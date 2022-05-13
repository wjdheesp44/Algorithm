num = int(input())

for i in range(num):
  for j in range(1, i+1):
    print(" ", end="")
  for j in range(num-i, 0, -1):
    print("*", end="")
  print()
num = int(input())
for i in range(num):
  for j in range(num-i-1, 0, -1):
    print(" ", end="")
  for j in range(0, (i+1)*2-1):
    print("*", end="")
  print()

for i in range(num-1):
  for j in range(i+1):
    print(" ", end="")
  for j in range((num-1-i)*2-1, 0, -1):
    print("*", end="")
  print()
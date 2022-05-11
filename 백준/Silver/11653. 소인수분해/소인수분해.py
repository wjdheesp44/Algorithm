num = int(input())
n = 2

while True:
  if num == 1:
    break
  if num % n == 0:
    print(n)
    num /= n
  else:
    n += 1
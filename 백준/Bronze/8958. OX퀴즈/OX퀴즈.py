cnt = int(input())

for i in range(cnt):
  count_circle = 0
  sum_circle = 0
  check = list(input())
  for j in check:
    if j == 'O':
      count_circle += 1
      sum_circle += count_circle
    else:
      count_circle = 0
  print(sum_circle)
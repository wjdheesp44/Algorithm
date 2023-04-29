num = int(input())

for i in range(num):
  h, w, n = map(int, input().split())
  one = (n // h) + 1
  floor = (n % h)*100
  if floor == 0:
    floor = h*100
    one = n // h
  
  total = floor + one
  print(total)
money = int(input())

num = 1000-money
cnt = 0

array = [500, 100, 50, 10, 5, 1]

for pay in array:
  cnt += num // pay
  num %= pay

print(cnt)
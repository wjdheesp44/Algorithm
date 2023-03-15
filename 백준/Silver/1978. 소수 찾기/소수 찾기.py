cnt = int(input())
num = list(map(int, input().split()))
decimal_cnt = 0

for i in range(cnt):
  count = 0
  for j in range(2, int(num[i])+1):
    if int(num[i]) % j == 0:
      count += 1
  if count == 1:
    decimal_cnt += 1

print(decimal_cnt)
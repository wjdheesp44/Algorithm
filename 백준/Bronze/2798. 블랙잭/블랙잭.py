import sys

num, max = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

result = max
sum_result = 0

for i in range(num):
  for j in range(i+1, num):
    for k in range(j+1, num):
      sum = numbers[i] + numbers[j] + numbers[k]
      if (max - sum) < result and (max - sum) >= 0:
        result = max - sum
        sum_result = sum
    
print(sum_result)
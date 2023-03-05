cnt = int(input())
num = list(map(int, input().split()))

sum = 0
for i in num:
  sum += i
  
result = (sum/len(num))/max(num)*100
print(result)
import sys

num = int(sys.stdin.readline())
age_name = []

for i in range(num):
  age_name.append(list(sys.stdin.readline().split()))
  
age_name.sort(key=lambda a:int(a[0]))
for i in range(num):
  print(age_name[i][0], age_name[i][1])
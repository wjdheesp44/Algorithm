import sys
input = sys.stdin.readline

n = int(input())

time = [0 for _ in range(n)]
price = [0 for _ in range(n)]

for i in range(n):
    time[i], price[i] = map(int, input().split())

day = 0
total_lst = []

def calculate(day, total):
    if day >= n:
        total_lst.append(total)
        return 
    
    if day + time[day] < n + 1:
        calculate(day + time[day], total + price[day])
    calculate(day+1, total) 

for i in range(n):
    calculate(i, 0)

total = max(total_lst)
print(total)


    
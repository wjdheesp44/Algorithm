x, y = map(int, input().split())

lastdayarr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekarr = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0

for i in range(x-1):
  day += lastdayarr[i]
day += y
print(weekarr[day % 7]) 
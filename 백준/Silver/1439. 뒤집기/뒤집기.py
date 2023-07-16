import sys
input = sys.stdin.readline

number = input()

arr = list(map(int, number[:len(number)-1]))

cnt0 = 0
cnt1 = 0

for i in range(len(arr)-1):
    if arr[i] == 1 and arr[i+1] == 0:
        cnt1 += 1
    elif arr[i] == 0 and arr[i+1] == 1:
        cnt0 += 1

if arr[len(arr)-1] == 1:
    cnt1 += 1
elif arr[len(arr)-1] == 0:
    cnt0 += 1

if cnt1 > cnt0:
    print(cnt0)
else:
    print(cnt1)
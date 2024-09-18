import sys
input = sys.stdin.readline

N = int(input())
result = []

for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if i == k or j == k:
                continue
            else:
                result.append((i, j, k))

for cnt in range(N):
    num, strike, ball = map(int, input().split())
    num_first = num // 100
    num_sec = (num // 10) % 10
    num_third = num % 10
    input_num = (num_first, num_sec, num_third)
    new_result = []
    for number in result:
        tmp_strike = 0
        tmp_ball = 0
        for j in range(3):
            if number[j] == input_num[j]:
                tmp_strike += 1
            elif number[j] in input_num:
                tmp_ball += 1
        if tmp_strike == strike and tmp_ball == ball:
            new_result.append(number)
    result = new_result

print(len(result))
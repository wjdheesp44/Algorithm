import sys
from collections import deque 
gear = []
gear_move = []
input = sys.stdin.readline

for i in range(4):
    gear.append(deque(map(int, input().strip())))
    
k = int(input())
for i in range(k):
    gear_move.append(list(map(int, input().split())))

def left_check(number, dir):
    if number == 0 or gear[number-1][2] == gear[number][6]:
        return
    if gear[number-1][2] != gear[number][6]:
        left_check(number-1, -dir)
        gear[number-1].rotate(-dir)

def right_check(number, dir):
    if number == 3 or gear[number][2] == gear[number+1][6]:
        return
    if gear[number][2] != gear[number+1][6]:
        right_check(number+1, -dir)
        gear[number+1].rotate(-dir)

for i in range(k):
    move = gear_move[i][0] - 1
    left_check(move, gear_move[i][1])
    right_check(move, gear_move[i][1])
    gear[move].rotate(gear_move[i][1])

total = 0
for i in range(4):
    if gear[i][0] == 1:
        total += 2 ** i

print(total)
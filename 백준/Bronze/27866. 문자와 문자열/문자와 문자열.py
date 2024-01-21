def solution(s, num):
    for i in s:
        if i == s[num - 1]:
            return i


s = list(map(str, input().strip()))
num = int(input())
print(solution(s, num))
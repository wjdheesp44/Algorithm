def solution(n):
    sum = 0
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            sum += i 
    else:
        for i in range(2, n+1, 2):
            sum += i ** 2
    return sum
def solution(num, n):
    while True:
        if num % n > n:
            continue
        elif num % n < n and num % n > 0:
            return 0
        else:
            return 1
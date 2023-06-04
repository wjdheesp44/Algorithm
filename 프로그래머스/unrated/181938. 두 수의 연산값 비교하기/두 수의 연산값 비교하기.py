def solution(a, b):
    strA = str(a)
    strB = str(b)
    answer = 0
    if int(strA+strB) >= 2*a*b:
        return int(strA+strB)
    else:
        return 2*a*b
    
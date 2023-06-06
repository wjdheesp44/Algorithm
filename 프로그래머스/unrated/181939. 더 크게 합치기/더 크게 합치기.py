def solution(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    
    if int(ab) >= int(ba):
        return int(ab)
    else:
        return int(ba)
def solution(a, d, included):
    answer = 0
    if included[0]:
        answer = a
    
    for i in range(1, len(included)):
        if included[i]:
            answer += a+d*i
    
    return answer
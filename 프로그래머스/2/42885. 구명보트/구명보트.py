def solution(people, limit):
    lst = []
    answer = 0
    i = 0
    people.sort()    
    
    start = 0
    end = len(people) - 1
    
    while True:
        if start > end:
            break
        elif start == end:
            answer += 1
            break
            
        if people[start] + people[end] <= limit:
            start += 1
        
        answer += 1
        end -= 1
            
    return answer
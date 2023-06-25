def solution(num_list):
    last = len(num_list)-1
    lasttwo = last-1
    if num_list[last] > num_list[lasttwo]:
        num_list.append(num_list[last]-num_list[lasttwo])
    else: 
        num_list.append(num_list[last]*2)
    return num_list
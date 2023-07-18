def solution(participant, completion):
    hash = {}
    for num in participant:
        hash[num] = hash.setdefault(num, 0) + 1

    for num in completion:
        hash[num] = hash.setdefault(num, 0) - 1

    for num in participant:
        if hash.setdefault(num, 0) != 0:
            return num
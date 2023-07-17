import collections
def solution(participant, completion):
    num = collections.Counter(participant) - collections.Counter(completion)
    return list(num.keys())[0]
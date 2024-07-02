import math

def solution(progresses, speeds):
    answer = []
    stack = []

    for i, (progress, speed) in enumerate(zip(progresses, speeds)):
        date = math.ceil((100-progress)/speed)

        if not stack or stack[-1][0] < date:
            stack.append([date, 1])

        else:
            stack[-1][1] += 1

    for i, cnt in stack:
        answer.append(cnt)

    return answer
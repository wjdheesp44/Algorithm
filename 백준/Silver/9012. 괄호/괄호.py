n = int(input())
ps = []

for _ in range(n):

    ps.append(input())

def inValid(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(")")
        else:
            if stack:
                stack.pop()
            elif not stack:
                return False
    return not stack

for i in range(n):
    if inValid(ps[i]):
        print("YES")
    else:
        print("NO")
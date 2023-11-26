def isValid(s):
    stack = []
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    return not stack

while True:
    s = input()

    if s == ".":
        break
    
    if isValid(s):
        print("yes")
    else:
        print("no")
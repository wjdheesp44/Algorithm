str = input()
str = list(str)

for i in str:
    if i.isupper():
        print(i.lower(), end='')
    elif i.islower():
        print(i.upper(), end='')

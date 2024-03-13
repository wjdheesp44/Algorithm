a = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = a
remaining_student = []
for student in students:
    remaining_student.append(student - b)

for num in remaining_student:
    if num > 0:
        cnt += num // c
        if num % c != 0:
            cnt += 1

print(cnt)

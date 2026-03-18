students = [tuple(input().split()) + (i + 1,) for i in range(5)]
students = [(student[0],int(student[1]),student[2]) for student in students]
students.sort(key=lambda x : x[0])

print("name")
for student in students:
    print(*student)

students.sort(key=lambda x : -x[1])
print()
print("height")
for student in students:
    print(*student)

# Please write your code here.

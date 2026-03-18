students = [tuple(map(int, input().split())) + (i + 1,) for i in range(5)]

students.sort(key=lambda x : x[0])

print("name")
for student in students:
    print(*student)

students.sort(key=lambda x : -x[1])

print("height")
for student in students:
    print(*student)

# Please write your code here.

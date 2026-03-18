n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    a, h, w = input().split()
    name.append(a)
    height.append(int(h))
    weight.append(int(w))

students=[(name[i],height[i],weight[i]) for i in range(n)]
students.sort(key= lambda x : (x[1],-x[2]))

for student in students :
    print(*student)
class student :
    def __init__(self,name,a,b,c) :
        self.name=name
        self.a=int(a)
        self.b=int(b)
        self.c=int(c)

N=int(input())
students=[]
for _ in range(N):
    n,a,b,c=input().split()
    students.append(student(n,a,b,c))
students.sort(key=lambda x : x.a+x.b+x.c)
for i in students:
    print(i.name, i.a, i.b, i.c)
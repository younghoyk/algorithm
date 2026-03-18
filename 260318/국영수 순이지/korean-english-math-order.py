class student :
    def __init__(self,name,kor,eng,math) :
        self.name=name
        self.kor=int(kor)
        self.eng=int(eng)
        self.math=int(math)

n= int(input())
students=[]
for _ in range(n):
    name,kor,eng,math=input().split()
    students.append(student(name,kor,eng,math))
students.sort(key=lambda x : (-x.kor, -x.eng, -x.math))
for student in students :
    print(student.name,student.kor, student.eng, student.math)


class person :
    def __init__(self,name,height,weight) :
        self.name=name
        self.height=int(height)
        self.weight=int(weight)
    
n=int(input())
people=[]
for i in range(n):
    n,h,w=input().split()
    people.append(person(n,h,w))
people.sort(key=lambda x : x.height)
for A in people:
    print(A.name,A.height,A.weight)
    
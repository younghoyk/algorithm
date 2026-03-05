A,B=map(int,input().split())
if A%2==0 :
    A+=1
for i in range(A,B+1,2):
    print(i, end= " ")
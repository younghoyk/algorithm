n = int(input())
l=[tuple(map(int,input().split())) + (i+1,) for i in range(n)]

l.sort(key= lambda x : (abs(x[0])+abs(x[1]),x[2]))

for a in l :
    print(l[2])



# Please write your code here.
N=int(input())
point=list(map(int,input().split()))

points=[]
for i in len(point) :
    points.append([i+1,point[i]])

points.sort(key=lambda x : x[1])

t=1
for i in points :
    i.append(t)
    t+=1

points.sort(key=lambda x : x[0])

for i in points :
    print(i[2])


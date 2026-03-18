n = int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]

def in_range(x,y) :
    return x>=0 and x<n and y>=0 and y<n

dx=[1,0,-1,0]
dy=[0,-1,0,1]

cnt=0

for i in range(n):
    for j in range(n):
        a=0
        for k in range(4):
            if matrix[i+dx[k]][j+dy[k]] ==1 and in_range(i+dx[k],j+dy[k]) :
                a+=1
        if a==3 :
            cnt+=1
        
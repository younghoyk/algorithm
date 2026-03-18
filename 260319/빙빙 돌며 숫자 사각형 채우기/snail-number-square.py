n,m=map(int,input().split())

def in_matrix(x,y) :
    return x>=1 and x<=n and y>=1 and y<=m

matrix=[[0]*(m+1) for _ in range(n+1)]

dir=0

dx,dy=[0,1,0,-1],[1,0,-1,0]

t=1
x,y=1,1
while t<=m*n : 
    matrix[x][y]=t
    nx,ny=x+dx[dir],y+dy[dir]
    if in_matrix(nx,ny) and matrix[nx][ny]==0 :
        x,y=nx,ny
    else :
        dir=(dir+1)%4
        x,y=x+dx[dir],y+dy[dir]
    t+=1
for i in range(n):
    for j in range(m):
        print(matrix[i+1][j+1],end=" ")
    print()

        
    
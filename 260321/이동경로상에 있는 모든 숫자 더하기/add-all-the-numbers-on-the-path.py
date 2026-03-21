n,t=map(int,input().split())
cmds=list(input())
matrix=[list(map(int,input().split())) for _ in range(n)]


x,y=(n-1)//2,(n-1)//2

dx,dy=[-1,0,1,0],[0,1,0,-1]
dir=0
total=matrix[x][y]

def in_matrix(x,y):
    return 0<=x<n and 0<=y<n
for cmd in cmds :
    if cmd == "R" :
        dir=(dir+1) %4

    
    elif cmd == "L" :
        dir=(dir+3) % 4
    else :
        nx,ny=x+dx[dir],y+dy[dir]
        if in_matrix(nx,ny) :
            x,y=nx,ny
            total+=matrix[x][y]
print(total)
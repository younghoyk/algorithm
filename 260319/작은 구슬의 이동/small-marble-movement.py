n,t = map(int,input().split())
r,c,d=input().split()
r,c=int(r),int(c)

in_direction={
    "U":0,
    "R" :1,
    "D" : 2,
    "L" : 3
}

def in_range(x,y) :
    return x>=1 and x<=n and y>=1 and y<=n

dx,dy=[-1,0,1,0],[0,1,0,-1]
dir=in_direction[d]

for _ in range(t):
    nx,ny=r+dx[dir],c+dy[dir]
    if in_range(nx,ny) ==1 :
        r,c=nx,ny
    else :
        dir=(dir+2)%4
print(r,c)

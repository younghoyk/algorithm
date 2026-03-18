x,y=0,0
direction=0
command=list(input())
dx,dy=[0,1,0,-1],[1,0,-1,0]

for i in command :
    if i =="L":
        direction= (direction+3) %4
    elif i == "R" :
        direction=(direction+1)%4
    else :
        x,y=x+dx[direction],y+dy[direction]
print(x,y)


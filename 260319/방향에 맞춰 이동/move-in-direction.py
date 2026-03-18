n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dir_mapper={
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}
dx=[1,0,-1,0]
dy=[0,-1,0,1]

x,y=0,0
for i in range(n) :
    A=dir_mapper[dir[i]]
    x,y=x+dist[i]*dx[A],y+dist[i]*dy[A]

print(x,y)
# Please write your code here.
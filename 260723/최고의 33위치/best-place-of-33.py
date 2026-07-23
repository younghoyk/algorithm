n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans=0
for i in range(0,n-2) :
    for j in range(0,n-2) :
        temp=0
        for x in range(0,3):
            for y in range(0,3) :
                if grid[i+x][j+y] == 1 :
                    temp +=1
        if temp>ans :
            ans = temp

print(ans)

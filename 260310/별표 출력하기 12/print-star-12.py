N=int(input())
matrix=[[" "]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        matrix[0][j]="*"
        if j %2 ==1 and i<=j :
            matrix[i][j]="*"
for i in range(N):
    for j in range(N):
        print(matrix[i][j],end=" ")
    print()

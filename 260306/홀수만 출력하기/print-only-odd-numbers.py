N= int(input())
arr=[int(input()) for _ in range(N)]
for i in arr :
    if i %2==1 and i%3==0 :
        print(i)
N=int(input())
ans=[]
for i in range(1,N+1):
    if i %2 ==0 or (i%3==0 and i%9!=0):
        continue
    if str(i)[0]=="5" :
        continue
    ans.append(spr(i))
print(f"{' '.join(ans))")
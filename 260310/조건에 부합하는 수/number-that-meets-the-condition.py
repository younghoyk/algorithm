A=int(input())
ans=[]
for i in range(1,A):
    if i %2==0 and i % 4!=0 :
        continue
    if (i //8) % 2 ==0 :
        continue
    if (i % 7) <4 :
        continue
    ans.append(i)
print(f"{" ".join(ans)}")
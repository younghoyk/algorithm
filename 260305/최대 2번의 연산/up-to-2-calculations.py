a=int(input())
for i in range(2):
    if a%2==0 :
        a/=a
    if a%2==1:
        a=(a+1)/2
print(a)
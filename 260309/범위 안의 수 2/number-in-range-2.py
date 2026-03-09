sum_val=0
num=0
for i in range(10) :
    N=int(input())
    if N>=0 and N<=200 :
        sum_val+=N
        num+=1
print(f"{sum_val} {sum_val/num:.1f}")
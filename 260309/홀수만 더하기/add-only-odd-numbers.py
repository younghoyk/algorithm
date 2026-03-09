N=int(input())
val_sum=0
for i in range(N):
    K=int(input())
    if K %2 ==1 and K %3 ==0 :
        val_sum+=K
print(val_sum)
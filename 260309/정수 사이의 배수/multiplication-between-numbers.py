A,B=map(int,input().split())
sum_val
for i in range(A,B+1) :
    if i % 5 ==0 or i % 7 ==0 :
        sum_val += i
print(f"{sum_val} {sum_val/(B-A):.1f}")

    
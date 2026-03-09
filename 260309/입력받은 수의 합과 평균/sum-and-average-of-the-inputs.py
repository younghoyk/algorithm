N=int(input())
sum_val=0
for _ in range(N):
    A=int(input())
    sum_val+=A
print(f"{sum_val} {sum_val/N:.1f}")
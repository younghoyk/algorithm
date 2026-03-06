A,B=map(int,input().split())
print(f"{A//B}.",end="")
re=A%B
for i in range(20):
    re*=10
    print(re//B,end="")
    re%=B
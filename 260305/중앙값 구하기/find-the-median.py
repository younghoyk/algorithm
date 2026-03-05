A,B,C=map(int,input().split())
if A>B and A>C :
    if B>C :
        print(B)
    else :
        print(C)
elif A<B and A<C :
    if B>C :
        print(C)
    else :
        print(B)
else :
    print(A)
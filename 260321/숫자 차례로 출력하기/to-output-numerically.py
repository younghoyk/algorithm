n = int(input())

def prt1(n) :
    if n ==0 :
        return
    prt(n-1)
    print(n,end=" ")

def prt2(n) :
    if n ==0 :
        return
    print(n,end=" ")
    prt(n-1)

prt1(n)
print()
prt2(n)

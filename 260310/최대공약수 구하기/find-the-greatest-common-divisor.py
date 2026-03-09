n, m = map(int, input().split())

def fine_gcp(n,m) :
    gcp=0
    for i in range(1,min(n,m)+1):
        if n % i ==0 and m % i ==0 :
            gcp=i
    print(gcp)

fine_gcp(n,m)
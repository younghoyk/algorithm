ma,ea=map(int,input().split())
mb,eb=map(int,input().split())

if ma>mb or (ma==mb and ea>= eb):
    print("A")
else :
    print("B")
N=int(input())
for i in range(1,N+1):
    check=0
    
    for j in range(len(str(i))):
        if str(i)[j] == "3" or str(i)[j] == "6" or str(i)[j] == "9":
            check=1
    if check ==1 or i%3==0 :
        print(0,end=" ")
    else :
        print(i,end=" ")
c1,t1=input().split()
c2,t3=input().split()
c3,t3=input().split()
count=0

if c1=="Y" and c2=="Y" :
    if int(t1)>=37 and int(t2)>37 :
        print("E")
elif c1=="Y" and c3=="Y" :
    if int(t1)>=37 and int(t3)>37 :
        print("E")
elif c2=="Y" and c3=="Y" :
    if int(t2)>=37 and int(t3)>37 :
        print("E")
else :
    print("N")
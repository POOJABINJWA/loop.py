a=int(input("enter the number :"))
c=0
i=1
while i<=a:
    if a%i==0:
        c=c+1
    i=i+1
if c==2:
    print("prime")
else:
    print("not")            


i=1
while i<=100:
    if i%2!=0 and i%3!=0 and i%5!=0:
        print(i ,"prime")
    elif i==2 or i==3 or i==5 :  
        print(i,"prime") 
    # else:
        # print()     
    i=i+1

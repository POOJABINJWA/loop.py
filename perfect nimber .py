a=int(input("enter the numbre"))
c=a
i=1
sum=0
while i<a:
    if a%i==0:
        sum=sum+i
    i=i+1
if c==sum:
    print("perfect") 
else:
    print("not")       

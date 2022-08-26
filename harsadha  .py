n=int(input("enter the number"))
c=n
rem=0
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
if c%sum==0:
    print("harsadh number")
else:
    print("not")    

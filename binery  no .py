a=int(input("enter the number"))
i=0
sum=0
while a>0:
    b=a%10
    sum=sum+b*2**i
    a=a//10
    i=i+1
print(sum)    

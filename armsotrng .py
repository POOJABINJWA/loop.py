a=int(input("enter the number :"))
c=a
sum=0
while a>0:
    sum=sum+(a%10)**3
    a=a//10
if c==sum:
    print("armsotrng number")
else:
    print("not")        
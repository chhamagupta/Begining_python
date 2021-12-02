num=int(input("enter a number"))
temp=num
rev=int
while(num>0):
    rev=num%10
    sum=sum+(rev*rev*rev)
    num=num//10
if(temp==sum):
     print("armstrong")
else:
     print("not amstrong")

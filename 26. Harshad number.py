Link :  https://prepinsta.com/python-program/checking-harshad-number-or-not-using-python/

n=int(input("Enter a number : "))
x=n
sum=0
while x>0:
    rem=x%10
    sum=sum+rem
    x=x//10

if n%sum==0:
    print(n, "is harshad number")

else :
    print(n , "is not harshad number ")

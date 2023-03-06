Link : https://prepinsta.com/python-program/to-check-automorphic-number/

n= int(input("Enter a number : "))
x=n 
square=n**2
t=10
flag=0
while n>0:
    r= square%t
    if r==x : 
        flag =1
        break
    n=n//10
    t=t*10

if flag ==1:
    
    print(x, " is Automorphic number ")
else:
    print(x, " is not Automorphic number ") 
 

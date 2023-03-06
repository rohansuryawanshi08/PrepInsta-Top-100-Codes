Link : https://prepinsta.com/python-program/check-for-perfect-square/
 
n=int(input("Enter a number: "))
flag=0
for i in range(1,n):
    if i*i==n:
        flag=1
        break

if flag==1 :
    print("Its a perfect square")

else:
    print("Its not perfect square")

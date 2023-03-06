Link : https://prepinsta.com/python-program/to-check-whether-a-number-is-a-strong-number-or-not/

n=int(input("Enter a number: "))
sum=0
num=n
while n>0:

    digit=n%10 # pichese digit kam krne use krte ye logic
    fact=1

    for i in range(1, digit+1):
        fact=fact*i

    sum=sum+fact
    n=n//10

if sum==num:
    print('It is strong number')

else:
    print("It is not strong number ")

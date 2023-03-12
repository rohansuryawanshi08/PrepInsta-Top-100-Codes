Link : https://prepinsta.com/python-program/find-number-of-integers-which-has-exactly-x-divisors/
    
def divisors(n):
    devisors=0
    for i in range(1,n//2+1):
        if n%i==0:
            devisors+=1

    return devisors


n=int(input("Enter a number: "))
print(divisors(n))

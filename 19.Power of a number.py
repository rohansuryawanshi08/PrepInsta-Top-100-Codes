Link : https://prepinsta.com/python-program/find-power-of-a-given-number/
    
def power_num(num,power):
    ans=num**power
    return f"Power of {num} is {ans}" 

num=int(input("Enter a number: "))
power= int(input(" Enter a power: "))
print(power_num(num ,power))



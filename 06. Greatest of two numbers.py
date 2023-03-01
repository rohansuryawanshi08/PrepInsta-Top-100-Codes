Link : https://prepinsta.com/python-program/find-greatest-of-two-numbers/
    
    
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1,num2 = input(f"Input first number and Second number comma separed : ").split(",")

print(max_of_two(num1, num2))

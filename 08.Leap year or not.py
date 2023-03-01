
Link : https://prepinsta.com/python-program/check-leap-year-or-not/

input_year=int(input("Enter a year : "))
def leap_year(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        return f"{year} is leap year"
    else:
        return f"{year} is not leap year"
    
print(leap_year(input_year))

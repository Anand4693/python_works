

def exponent(base,power=1):
    result = bass ** power

print(exponent(3))


# write a function is_leap_year with one parameter year
# return True if year is leap year else return false

def is_leap_year(year):

    if year % 100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    else:

        return False
    
print(is_leap_year(2024))

"""

Q1) 
    create a function is_prime with one parameter num
    return True if number is prime else return False
"""

"""
Q2)
    Create a function gcd with two param num2, num2
    return gcd of num1,num2
"""

"""
Q3

Create a function is_plaindrome with one parameter num
return True if num us palindrome else return False
"""
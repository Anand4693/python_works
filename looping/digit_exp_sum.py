
# number = 123

# digit_count = 3

# 3**3 + 2**3 + 1**3

# len() return length of the non-integer object.

# len(str()) return length of the integer object.



#set number
#find digit_count
#set sum as O

#loop
    #extract digit
    #exponent
    #add exponent with sum
    #remove last digit
#display sum

number = 12

count = len(str(number))

sum = 0

while(number !=0):

    digit = number % 10

    exponent = digit ** count

    sum = sum + exponent

    number = number // 10

print(sum)


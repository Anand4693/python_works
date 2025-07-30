
# step1: set sum as 0
# step2: last_digit
# step3: add 1st_digit with sum
# step4: floor

number = 174

sum = 0

while (number !=0): #174 !=0 

    digit = number % 10 #174%10=17

    sum += digit #sum +=17

    number = number // 10 #174//10 = 

print(sum)
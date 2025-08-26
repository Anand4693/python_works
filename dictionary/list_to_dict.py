
numbers = [2,3,4,5,6]

square_dict = {}

# Output = {"2":4,"3":9,"4":16,"5":35,"6":36}

for num in numbers:

    square_dict[num] = num**2

# Using update method
    square_dict.update({num:num**2})

print(square_dict)


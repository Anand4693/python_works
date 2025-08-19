# create a list expenses [10000,12000,13000,14000]
# update 12000 as 12500
# display all expenses
# display total expenses
# display highest expense
# display avg expense


#  -ve         -4   -3    -2   -1  
expenses = [10000,12000,13000,14000]
#   +ve       0     1     2     3
expenses[1] = 12500

# iterate

# indexing

for i in range(0,len(expenses)):

    print(expenses[i])


for e in expenses:

    print(e)

# To find the total expenses using indexing

total_exp = 0

for i in range(0,len(expenses)):

    total_exp += expenses[i]

print(total_exp)

# using the buildin functions, we can find the avg, highest expense

# Total expenses
total_exp = sum(expenses)
print(total_exp)

# To find the costly expense (highest number)

costly_exp = max(expenses)
print(costly_exp)

# To find the less expense (lowest number)
lowest_exp = min(expenses)
print(lowest_exp)



# data type: represents the type of value that variable can hold

# int, float, string, bool

# number = 123
# print(type(number))

# company_name = "Luminar technolab"

#print(type(company_name))
#rating = 5.0
#print(type(rating))

#is_open = True
#print(type(is_open))

# readbill_total
# read number of dines
# read tip_amount
# calculate individual split

bill_total = int(input("enter bill total:"))
dines = int(input("enter number of dines"))
tip_amount = int(input("enter tip amount"))
total_amount = bill_total + tip_amount

individual_split = total_amount/dines
print("Everyone needs to put",individual_split,"as part of share")
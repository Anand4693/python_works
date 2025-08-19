

# H => holiday
# P => present
# L => leave
attendance = ["H","P","P","P","P","L","H","H","P","P","P","P","L","H"]

# company_total number of working days

# total_number of leaves

# how many leave taken consecutively

working_days = 0
for a in attendance:

    if a!="H":

        working_days += 1

print('The total number of working days',working_days)

for a in attendance:
    holidays = 0

    if a == "H":

        holidays +=1

print('The total number of leaves are', holidays)
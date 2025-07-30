
# bill_amount => read bill amount

# dines_counts => read dines amount

# calculate tip as 12% of bill amount

# add 8% of GST along with bill amount

# calculate total amount and individual amount


bill_amount = int(input("Enter the bill amount"))

dines_count = int(input("Enter number of dines"))

tip_amount = (12/100) * bill_amount

gst_amount = (8/100) * bill_amount

total_amount = bill_amount + tip_amount + gst_amount

individual_amount = total_amount / dines_count

print("The tip amount is",tip_amount)

print("The total GST is",gst_amount)

print("The total bill amount including GST and tip is",total_amount,"and share for each person is",individual_amount)


"A shopkeeper purchase a product at price of rs x, by adding y % profit"

"what will be the selling price"

# purchase_price

# profit_margin

# Selling_price.

purchase_price = int(input("Enter the purchase price"))

profit_margin = int(input("Enter the profit margin in %"))

GST = 8

profit = (profit_margin / 100) * purchase_price

selling_price = purchase_price + profit

gst_amount = (GST/100)*selling_price

total_amount = selling_price + gst_amount

print("The new selling price including GST is",total_amount)

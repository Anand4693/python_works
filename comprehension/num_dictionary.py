arr = [6,7,8,9,10]

# {6:36,7:49,6:64,,,,}

square_dict = {num: num**2 for num in arr}

print(square_dict)


orders = ["tea","dosa","tea","ghee-roast","tea","cofee","tea","idly","dosa"]

# {"tea":3,"dosa:2"}

order_count = {o:orders.count(o) for o in orders}

print(order_count)

#collections and collection methods

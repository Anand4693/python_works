
product = {"code":"skull123","title":"Linen shirt","brand":"peterengland","price":17000}


# add offer as 1000 if offer exist else update offer as current offer + 500

if "offer" in product:

    product["offer"]+=500

else:

    product["offer"] = 1000

print(product)

books = [
    ["randamoozham",450,"mt",560],
    ["goatlife",560,"benyamin",570],
    ["arachar",450,"meera",506]
]

# display title of each book

for b in books:

    print(b[0])

# display the price of the books

for b in books:

    print(b[3])


all_book_titles = [b[0]for b in books]
print(all_book_titles)

food_items = [
    ["tea","veg",12],
    ["coffee","veg",20],
    ["dosa","veg",60],
    ["gheeroast","veg",80],
    ["masalaroast","veg",120],
    ["eggfriedrice","non-veg",160],
    ["vegfriedrice","veg",120]
]

# To print all the names of the dish

all_item_name = [it[0] for it in food_items]
print(all_item_name)

# display veg item names

all_veg_items = [it[0] for it in food_items if it[1]=="veg"]
print(all_veg_items)

# items available under 100rs

price_filter = [it[0] for it in food_items if it[2]<100]
print(price_filter)


bikes = [
    ["passion-pro","hero",89000,"petrol",125],
    ["passion-plus","hero",90000,"petrol",125],
    ["activa","honda",120000,"petrol",125],
    ["xpulse","hero",139000,"petrol",150],
    ["hunter","re",200000,"petrol",350],
    ["Unicorn","honda",160000,"petrol",150],
    ["R15","yamaha",210000,"petrol",150],
    ["duke390","KTM",400000,"petrol",373],
    ["s1 pro","OLA",140000,"EV",120],
    ["ather 450X","ather",160000,"EV",150]
]

#display the names of all bikes
all_bike_names = [b[0]for b in bikes]
print(all_bike_names)


# display all bikes prices
all_bike_price = [b[2]for b in bikes]
print(all_bike_price)

# display the fuel variants
fuel_variants = [b[3]for b in bikes]
print(fuel_variants)

# display price under 1 lakh
price_variants = [b[2]for b in bikes if b[2]<100000]
print(price_variants)

# display ev bikes
ev_vehicles = [b[3]for b in bikes if b[3]=="EV"]
print(ev_vehicles)

# define a function which receives 1 parameter that is list return list[2]

def get_price(lst):

    return lst[2]

costly_bike = max(bikes,key=get_price)

print("Costly bike", costly_bike)
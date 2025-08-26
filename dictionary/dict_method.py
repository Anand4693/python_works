# class dict:

#   def get(key) - To get the value using key
#   def pop(key)
#   def keys()
#   def values()
#   def items()
#   def update()

fruits = {"a":"apple","b":"banana","c":"cherry","d":"dragon-fruit"}


# Using items methond - Returns key and value
for k,v in fruits.items():
    
    print(k,v)

# Using get(key)

print(fruits.get("ab"))
print(fruits)
#Output = None


# To update
fruits.update (o="orange")
fruits.update(e="egg-fruit")
print (fruits)


# Using values()
for v in fruits.values():

    print(v)

# Using key methond
for k in fruits.keys():

    print(k)

# Using pop method
popped_value = fruits.pop("d")

print(popped_value)


# Using get method
#all_value = fruits.keys["ba"]

#print(all_value)
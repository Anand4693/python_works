# set
# define set (),{10,20,30}
# all elements in set are unique
# unordered
# class set
    # def union() - To combine everthing
    # def intersection()
    # def difference()
    # def add(object)
    # def issubset()
    # def symmeteric_difference




customer1_order = {"tea","dosa","idly"}
customer1_order.add("fresh-lime")
print(customer1_order)

set_a = {10,20,30}
set_b = {100,10,200,20,300,30}
print(set_a.issubset(set_b))
print(set_b.issuperset(set_a))


# To remove the common elements using symmetrical difference

set_a = {1,2,3,4}

set_b = {3,4,5,6}

symm = set_a.symmetric_difference(set_b)

print(symm)
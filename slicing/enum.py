

arr = [10,11,12,13]
#       0  1  2  3

for i in range(0,len(arr)):

    print(i,arr[i])

# Using enumerate method
for index,element in enumerate(arr):

    print(index,element)
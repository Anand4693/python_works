#To find the common numbers from 2 arrs

arr1 = [10,11,20,17,18,10]

arr2 = [20,10,12,17]

#Method 1

for num in arr1:

    if arr2.count(num)>0:

        print(num)


#Method 2

for num in arr1:

    if num in arr2:
        
        print(num)
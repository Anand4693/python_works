

# BMI calculate

# read height
# read weight

# BMI = weight_in_kg / height_in_meters ** 2

weight_in_kg = int(input("Enter weight in KG"))

height_in_cm = int(input("Enter height in CM"))

height_in_meter = height_in_cm / 100

BMI = weight_in_kg / height_in_meter ** 2

print("Person with height", height_in_meter, "and weight",weight_in_kg,"has body mass eqaul to",BMI)
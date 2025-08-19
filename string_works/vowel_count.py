
text = "pneumonoultramicroscopicsilicovolcanoconiosisA".casefold()

vowels = "aeiou"

v_count = 0

# set text
# set vowels
# set v_count
# extract each character from text
# check character in vowels
# increment v_count with one

for ch in text:

    if ch in vowels:

        v_count+=1

print(f"vowel count = {v_count}")
        
    
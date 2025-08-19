
# read a text from user and display vowel count and consonant count

# set text

# set vowels

# set v_count as 0

# set c_count as 0

# extract each character from text
    #check character is vowel if yes increment v_count else increment c_count

# display v_count and c_count

text = input("Enter text").casefold()

vowels = "aeiou"

v_count = 0

c_count = 0

for ch in text:
    
    if ch in vowels:

        v_count+=1
    
    elif ch.isalpha():

        c_count+=1

print("vowel count is",v_count)

print("consonant count is",c_count)

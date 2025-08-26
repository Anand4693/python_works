

text = "goodmorning"

char_count = {}


for ch in set(text):
    
    ch_count = text.count(ch)

    char_count[ch] = ch_count

# In single line

    char_count[ch] = text.count(ch)

print(char_count)



max_frequency = 0

max_frequency_dictionary = {}

for k,v in char_count.items():

    if v > max_frequency:

        max_frequency = v

        max_frequency_dictionary.clear()

        max_frequency_dictionary[k] = v

    print(max_frequency_dictionary)

    

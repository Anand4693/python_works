
#new_arr = [num+1 if num>5 else num-1 for num in new_arr]

#print(new_arr)

# create a new list of words starting with vowels

words = ["apple","banana","carrot","drumstick","egg","fish"]

vowel_words = [w for w in words if w[0].lower() in "aeiou"]

print(vowel_words)

# print longest word from words

longest_word = max(words,key=len)

print(longest_word)

# print shortest word from words

shortest_word = min(words,key=len)

print(shortest_word)

# To find the length of each words

word_dictionary = {w:len(w) for w in words}

print(word_dictionary)
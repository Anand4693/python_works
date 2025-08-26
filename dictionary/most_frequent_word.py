# text = "this is a python program to find most recursive word this python program is simple"

# display most frequest word


text = "this is a python program to find most recursive word this python program is simple"

# Split text into words
words = text.split()

# Create a dictionary to count word frequencies
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Find the most frequent word
most_frequent = max(word_count, key = word_count.get)

print(f"The most frequent word is: '{most_frequent}' (Count: {word_count[most_frequent]})")

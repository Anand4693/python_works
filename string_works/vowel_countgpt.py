
def count_vowels(word):
    vowels = "aeiou"
    vowel_count = {}

    for letter in word:
        if letter in vowels:
            vowel_count[letter] = vowel_count.get(letter, 0) + 1

    return vowel_count

# Word to check
word = "pneumonoultramicroscopicsilicovolcanoconiosis"

# Count vowels
vowels_found = count_vowels(word)

# Print results
print(f"Vowels in '{word}':")
for vowel, count in vowels_found.items():
    print(f"{vowel}: {count}")
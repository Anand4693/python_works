
arr = ["word","madam","racecar","car"]

palindrome_words = [w for w in arr if w == w[:: -1]]

print("The palindromes are",palindrome_words)

reversed_array = arr[::-1]
print(reversed_array)


"""sequence[1:5]
sequence[1:5]
sequence[3:]
sequence[:]
sequence[::2]
sequence[::-1]"""
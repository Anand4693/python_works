"""""
Definition:
Slicing means extracting a part (subsequence) from a sequence
like a list, string or tuple using a special syntax.
"""

"""
syntax
sequence[start:stop:step]
"""

word = "pythonprogramming"
#       01234567890123456

sliced_word = word[:6] #skip start => starts from begining
print(sliced_word)

sliced_word2 = word[6:]
print(sliced_word2)

sliced_word3 = word[::3]
print(sliced_word3)

sliced_word4 = word[::]
print(sliced_word4)

reverse_word = word[:: -1]
print(reverse_word)


# display longest_palindrome_subsrting
# CEC, ACECA, RACECAR

def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(word):
    n = len(word)
    longest = ""
    
    for i in range(n):
        for j in range(i, n):
            substr = word[i:j+1]
            if is_palindrome(substr) and len(substr) > len(longest):
                longest = substr
                
    return longest

# Example usage
word = input("Enter a word: ")
result = longest_palindrome(word)
print("Longest palindrome:", result)

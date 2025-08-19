
# word1 = "silent"
# word2 = "listen"
# chk for anagram

word1 = "silent"
word2 = "listen"

# Using sorted function

srt_w1 = sorted(word1)
srt_w2 = sorted(word2)

print(srt_w1 == srt_w2)

#Using set function

print(set(word1)==set(word2) and len(word1)==len(word2))


word1 = "bcade"
word2 = "abcd"

word1_list = list(word1)

word2_list = list(word2)

word1_list.sort()

word2_list.sort()

print(word2_list == word1_list)





# word_count

text = "hello hai hello hai hai"

# step1 : split text into words

words = text.split(" ")

# step2 : create an empty dictionary

wc = {}

# step3 extract each from words

for w in words:

    # add w as key and value as 1 if w not exist else update w as current value + 1

    if w in wc:

        wc[w]+=1
    
    else:

        wc[w]=1

print(wc)
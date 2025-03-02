sentence="hello world how are you"
word_list = sentence.split(" ")
res=""
print(word_list)

for word in word_list:
    res+=word[0]

print(res)
# #inefficient
# words = ["mahmud", "kabir", "sadik"]
# sentence = ""
# for word in words:
#     sentence+=word+""
#     print(sentence.strip())

# efficient
words = ["mahmud", "kabir", "sadik"]
sentence = "".join(words)
print(sentence)
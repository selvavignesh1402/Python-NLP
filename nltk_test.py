import nltk

from nltk.tokenize import word_tokenize, sent_tokenize



text = "Hello, world! How are you today?"
words = word_tokenize(text)
sentences = sent_tokenize(text)

print("Words:", words)
print("Sentences:", sentences)

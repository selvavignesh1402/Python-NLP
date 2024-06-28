import nltk

from nltk.tokenize import word_tokenize,sent_tokenize

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer

from nltk.stem import WordNetLemmatizer

from nltk.chunk import RegexpParser

text=input("Enter a Text: ")

words=word_tokenize(text)

sen=sent_tokenize(text)

stop=set(stopwords.words("english"))

filter=[]

for word in words:
    if word.lower() not in stop:
        filter.append(word)

stemmer=PorterStemmer()

stem=[stemmer.stem(word) for word in filter]

pos_tag=nltk.pos_tag(filter)

lemen=WordNetLemmatizer()

lem=[lemen.lemmatize((word)) for word in filter]

grammer=r""" 
    NP: {<DT>?<JJ>*<NN>}
"""
chunk=RegexpParser(grammer)

chunks=chunk.parse(pos_tag)


print("The Words of the given text: ")
print(words)

print("The Sentences of the given text: ")
print(sen)

print("The Filtered Words: ")
print(filter)

print("The Stemmed Words: ")
print(stem)

print("POS: ")
for word,tag in pos_tag:
    print(word," - ", tag)

print("The Lemmentaizd Words: ")
print(lem)

print("The Chunnked Words: ")
print(chunks)
# chunks.draw()
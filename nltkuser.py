import nltk
import numpy


from nltk.tokenize import word_tokenize,sent_tokenize

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer

from nltk.stem import WordNetLemmatizer

from nltk.chunk import RegexpParser

from nltk import pos_tag, ne_chunk

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

postag=nltk.pos_tag(filter)

lemen=WordNetLemmatizer()

lem=[lemen.lemmatize((word)) for word in filter]

grammer=r""" 
    NP: {<DT>?<JJ>*<NN>}
        }<IN>{
"""
chunk=RegexpParser(grammer)

chunks=chunk.parse(postag)

# text="Apple is looking at buying U.K. startup for $1 billion. Elon Musk is the CEO of SpaceX."
# tokens = word_tokenize(text)
# pos_tags1 = pos_tag(tokens)
# ner=ne_chunk(pos_tags1)

# ner=ne_chunk(postag)


print("The Words of the given text: ")
print(words)

print("The Sentences of the given text: ")
print(sen)

print("The Filtered Words: ")
print(filter)

print("The Stemmed Words: ")
print(stem)

print("POS: ")
for word,tag in postag:
    print(word," - ", tag)

print("The Lemmentaizd Words: ")
print(lem)

print("The Chunnked and Chinnked Words: ")
print(chunks)

for chunk in chunks:
        if hasattr(chunk, 'label'):
            print(f"{chunk.label()}: {' '.join(c[0] for c in chunk)}")
        else:
            print(' '.join(c[0] for c in chunk))
# chunks.draw()
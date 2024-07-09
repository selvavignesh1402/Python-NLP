# Introduction to NLP and spaCy
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from collections import Counter

# Installation of spaCy
# !pip install spacy
# !python -m spacy download en_core_web_sm

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# The Doc Object for Processed Text
text = "Natural Language Processing (NLP) is a fascinating field."
doc = nlp(text)
print(doc)

# Sentence Detection
sentences = list(doc.sents)
print(sentences)

# Tokens in spaCy
tokens = [token.text for token in doc]
print(tokens)

# Stop Words
stop_words = [token.text for token in doc if token.is_stop]
print(stop_words)

# Lemmatization
lemmas = [token.lemma_ for token in doc]
print(lemmas)

# Word Frequency
word_freq = Counter([token.text for token in doc if not token.is_stop and not token.is_punct])
print(word_freq.most_common())

# Part-of-Speech Tagging
pos_tags = [(token.text, token.pos_) for token in doc]
print(pos_tags)

# Visualization: Using displaCy
displacy.render(doc, style="dep")

# Preprocessing Functions
def preprocess(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    lemmas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return tokens, lemmas

tokens, lemmas = preprocess(text)
print(tokens)
print(lemmas)

# Rule-Based Matching Using spaCy
matcher = Matcher(nlp.vocab)
pattern = [{"LOWER": "natural"}, {"LOWER": "language"}, {"LOWER": "processing"}]
matcher.add("NLP_PATTERN", [pattern])
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

# Dependency Parsing Using spaCy
for token in doc:
    print(f"{token.text} -> {token.dep_} -> {token.head.text}")

# Tree and Subtree Navigation
for token in doc:
    subtree = [t.text for t in token.subtree]
    print(f"{token.text}: {subtree}")

# Shallow Parsing
noun_chunks = list(doc.noun_chunks)
print(noun_chunks)

# Named-Entity Recognition
entities = [(ent.text, ent.label_) for ent in doc.ents]
print(entities)

# Visualization: Using displaCy for entities
displacy.render(doc, style="ent")

# Conclusion
print("NLP with spaCy provides powerful tools for text processing and analysis.")

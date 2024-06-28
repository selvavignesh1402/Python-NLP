import nltk
from nltk.tokenize import word_tokenize

text = "The sun set over the horizon, painting the sky in hues of orange and pink. Birds chirped their final songs of the day as the world prepared for night. A gentle breeze rustled the leaves, whispering secrets of the past. Stars began to twinkle, each one telling a story of distant galaxies."

words = word_tokenize(text)

print(words)

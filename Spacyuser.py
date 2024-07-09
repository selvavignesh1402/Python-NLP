import spacy
import neuralcoref
from spacy import displacy
from textblob import TextBlob
from transformers import MarianMTModel,MarianTokenizer,pipeline

nlp=spacy.load('en_core_web_lg')

neuralcoref.add_to_pipe(nlp)

q_pipe=pipeline("question-answering")

text=input("Enter a Text: ")

doc = nlp(text)

relations = []

print("Word In The Text: ")
for i in doc:
    words=i.doc
    print(words)

print("StopWords In The Text: ")
for i in doc:
    if not i.is_stop:
        swords=i.doc
        print(swords)

print("Lemma In The Text: ")
print("Token : Lemma")
for i in doc:
    lemma=i.lemma_
    print(f"{i.doc}  :  {lemma}")

print("POS In The Text: ")
for i in doc:
    pos=i.pos_
    tag=spacy.explain(i.tag_)
    print(f"{i.doc} : {pos} : {tag}")

print("NER In The Text: ")
for i in doc.ents:
    print(f"{i.text} : {i.label_} : {spacy.explain(i.label_)}")

print("Relation in Text:")
for sent in doc.sents:
    for ent in sent.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE","DATE","NORP"]:
            for token in sent:
                if token.dep_ in ["attr", "nsubj", "dobj", "pobj", "conj", "appos", "acl", "relcl"]:
                    relations.append((ent.text, token.text, sent.text))


for name, rela, context in relations:
    print(f"Relation: {name} -> {rela}")
    print(f"Explanation: '{name}' is related to '{rela}' in the context of '{context}'\n")

context = text + "\n\n"
for _, _, ctx in relations:
    context += ctx + "\n"

print("Sentiment In The Text: ")
blob=TextBlob(doc.text)
sentiment=blob.sentiment
print(f"Sentiment : {sentiment}")


print("Corefrence ResolutionIn The Text: ")
if doc._.has_coref:
    for cluster in doc._.coref_clusters:
        print(cluster.mentions)

def answer_question(question,context):
    result=q_pipe(question=question,context=context)
    return result['answer']

question=input("Enter a Question : ")
answer=answer_question(question,text)
print(f"Answer: {answer}")


displacy.serve(doc,style="ent")

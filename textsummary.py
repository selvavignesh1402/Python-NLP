# from transformers import pipeline  # Imports the pipeline function from the Hugging Face transformers library.

# # Load the question-answering pipeline
# nlp = pipeline("question-answering")  # Creates a question-answering pipeline using a pre-trained model.

# def answer_question(context, question):  # Defines a function to get an answer for a given question and context.
#     result = nlp(question=question, context=context)  # Calls the pipeline to process the question and context.
#     return result['answer']  # Extracts and returns the answer from the pipeline's result.

# # Example usage
# context = """  # Defines an example context (a block of text with information about LanguageTool).
# LanguageTool is an open-source grammar, style, and spell checker. It is available as a standalone application,
# browser extension, and web service. It supports multiple languages and provides a variety of features to enhance
# the writing process.
# """
# question = "What is LanguageTool?"  # Defines an example question asking about LanguageTool.

# answer = answer_question(context, question)  # Calls the function with the example context and question.
# print("Answer:", answer)  # Prints the answer to the console.


import spacy
from transformers import pipeline

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

q_pipe=pipeline("question-answering")

# Input text
text = input("Enter Text: ")

# Process the text
doc = nlp(text)

# List to store relations with explanations
relations = []

# Print named entities in the text
print("NER In The Text:")
for i in doc.ents:
    print(f"{i.text} : {i.label_}")

# Extract and explain relations in the text
print("Relation in Text:")
for sent in doc.sents:
    for ent in sent.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE","DATE","NORP"]:
            for token in sent:
                if token.dep_ in ["attr", "nsubj", "dobj", "pobj", "conj", "appos", "acl", "relcl"]:
                    relations.append((ent.text, token.text, sent.text))

# Print relations with explanations
for name, rela, context in relations:
    print(f"Relation: {name} -> {rela}")
    print(f"Explanation: '{name}' is related to '{rela}' in the context of '{context}'\n")

context = text + "\n\n"
for _, _, ctx in relations:
    context += ctx + "\n"


def answer_question(question,context):
    result=q_pipe(question=question,context=context)
    return result['answer']

question=input("Enter a Question : ")
answer=answer_question(question,text)
print(f"Answer: {answer}")


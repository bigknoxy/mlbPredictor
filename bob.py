# from transformers import pipeline

# # Load the question answering pipeline
# qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', tokenizer='distilbert-base-cased')

# # Ask a question
# question = "What is the capital of France?"
# context = "France is a country located in Western Europe. Its capital is Paris."

# # Get the answer
# answer = qa_pipeline(question=question, context=context)

# # Print the answer
# print(answer['answer'])


from pybaseball import batting_stats_bref
from transformers import pipeline
import pandas as pd

# # Load the question answering pipeline
# qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', tokenizer='distilbert-base-cased')
# Load a different question answering pipeline
qa_pipeline = pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad', tokenizer='bert-large-uncased-whole-word-masking-finetuned-squad')

# Get all of this season's batting data so far
batting_stats = batting_stats_bref()

# Output the DataFrame to a CSV file
batting_stats.to_csv('data/batting_stats.csv', index=False)

# Print a message indicating that the file was saved
print("The batting stats have been saved to a CSV file.")

# Convert the DataFrame to a string
context = batting_stats.to_string(index=False)

# Prompt the user to enter a question
question = input("Enter a question: ")

# Get the answer
answer = qa_pipeline(question=question, context=context)

# Print the answer
print(answer['answer'])


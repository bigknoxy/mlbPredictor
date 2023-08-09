import spacy
from pybaseball import batting_stats_bref

# Load the English language model in spaCy
nlp = spacy.load('en_core_web_sm')

# Define a dictionary that maps column headers to their names and synonyms
column_map = {
    'BA': ['batting average', 'average', 'avg'],
    'HR': ['home runs'],
    'RBI': ['runs batted in'],
    'OPS': ['on-base plus slugging'],
    # Add additional column headers here
}

# Get all of this season's batting data so far
batting_stats = batting_stats_bref()

# Define a function to answer questions about baseball statistics
def answer_question(question):
    # Parse the question using spaCy
    doc = nlp(question)

    # Identify the named entities in the question
    entities = [ent.text for ent in doc.ents]

    # Construct a query to the DataFrame based on the named entities
    query = ''
    for entity in entities:
        for column, synonyms in column_map.items():
            if entity.lower() in [s.lower() for s in synonyms]:
                query += f"{column} == {batting_stats[column].max()}"

    # Check if a query was constructed
    if query == '':
        return 'Sorry, I could not understand the question.'

    # Execute the query and get the answer
    answer = batting_stats.query(query)['Name'].values[0]

    return answer

# Prompt the user to enter a question
question = input("Enter a question: ")

# Get the answer
answer = answer_question(question)

# Print the answer
print(answer)

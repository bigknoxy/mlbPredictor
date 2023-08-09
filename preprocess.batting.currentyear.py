import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pybaseball import batting_stats_bref

# Get all of this season's batting data so far
batting_stats = batting_stats_bref()

# Load the English language model in spaCy
nlp = spacy.load('en_core_web_sm')

# Load nltk punkt
nltk.download(['punkt','wordnet'])

# Load the NLTK stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Initialize the NLTK lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary that maps column headers to their names and synonyms
column_map = {
    'BA': ['batting average', 'average', 'avg', 'batting avg'],
    'HR': ['home runs', 'dingers', 'HR'],
    'RBI': ['runs batted in', 'ribbies', 'RBI'],
    'OPS': ['on-base plus slugging','onbase plus slugging','on base plus slugging', 'on-base percentage plus slugging percentage', 'OPS'],
    'PA': ['plate appearances', 'PA'],
    'AB': ['at-bats', 'at bats', 'AB'],
    'R': ['runs', 'R'],
    'H': ['hits', 'hit', 'H'],
    '2B': ['doubles', '2B'],
    '3B': ['triples', '3B'],
    'BB': ['walks', 'BB','base on balls'],
    'IBB': ['intentional walks','free passes', 'free pass', 'IBB'],
    'SO': ['strikeouts', 'Ks', 'SO'],
    'HBP': ['hit by pitch', 'hit by pitches', 'HBP'],
    'SH': ['sacrifice hits', 'sacrifice bunts', 'SH'],
    'SF': ['sacrifice flies', 'SF'],
    'GDP': ['ground into double play', 'double play', 'GDP'],
    'SB': ['stolen bases', 'SB'],
    'CS': ['caught stealing', 'CS'],
    # Add additional column headers here
}

# Define a function to answer a question using the batting stats DataFrame
def answer_question(question):
    # Tokenize the question
    tokens = word_tokenize(question)

    # Remove stop words and lemmatize the tokens
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.lower() not in stop_words]

    # Match the tokens to column headers
    keys = []
    for token in tokens:
        for key, values in column_map.items():
            if token in values:
                keys.append(key)

    # Find the highest value in the matching column
    if len(keys) == 0:
        return "Sorry, I could not understand the question."
    else:
        column = max(keys, key=lambda x: batting_stats[x].max())
        player = batting_stats.loc[batting_stats[column] == batting_stats[column].max(), 'Name'].iloc[0]
        return f"{player} has the highest {column}."

# Example usage
question = "Who has the highest batting average? minimum of 50 AB"
answer = answer_question(question)
print(answer)

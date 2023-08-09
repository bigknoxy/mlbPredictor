from pybaseball import batting_stats_bref
import pandas as pd

# Get all of this season's batting data so far
batting_stats = batting_stats_bref()

# Output the DataFrame to a CSV file
batting_stats.to_csv('data/batting_stats.csv', index=False)

# Print a message indicating that the file was saved
print("The batting stats have been saved to a CSV file.")

# Define a function to answer questions about baseball statistics
def answer_question(question):
    # Load the batting statistics from the CSV file
    batting_stats = pd.read_csv('data/batting_stats.csv')

    # Convert the question to lowercase for easier matching
    question = question.lower()

    # Define a set of rules for answering questions
    if 'highest batting average' in question:
        # Find the player with the highest batting average
        player = batting_stats.loc[batting_stats['BA'].idxmax()]['Name']
        answer = f"The player with the highest batting average is {player}."
    elif 'most home runs' in question:
        # Find the player with the most home runs
        player = batting_stats.loc[batting_stats['HR'].idxmax()]['Name']
        answer = f"The player with the most home runs is {player}."
    else:
        answer = "I'm sorry, I don't know the answer to that question."

    return answer

# Prompt the user to enter a question
question = input("Enter a question: ")

# Get the answer
answer = answer_question(question)

# Print the answer
print(answer)

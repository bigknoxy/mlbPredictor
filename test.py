import pandas as pd
import transformers

# Load the CSV file
df = pd.read_csv('data/todaysGames.csv')

# Prepare the data for training
df = df.dropna()
df = df.reset_index(drop=True)

# Create a language model
model = transformers.AutoModelForSequenceClassification.from_pretrained('bert-base-uncased')

# Train the language model
model.train(df, mode=True)

# Use the model to make predictions
predictions = model.predict(df)

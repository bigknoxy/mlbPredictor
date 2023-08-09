from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the trained model
model = T5ForConditionalGeneration.from_pretrained('./results')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

# Get user input
input_text = input("Enter your question: ")

# Tokenize the input
inputs = tokenizer.encode(input_text, return_tensors='pt')

# Generate output
outputs = model.generate(inputs)
output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print the generated output
print("Generated Answer:", output_text)

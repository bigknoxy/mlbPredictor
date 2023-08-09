# Install the required libraries
# pip install --upgrade transformers datasets

# Import the required libraries
from transformers import T5ForConditionalGeneration, T5Tokenizer
from datasets import load_dataset

# Load the dataset of question-answer pairs
# dataset = load_dataset('csv', data_files='train/qa_dataset.csv', delimiter='\t')
dataset = load_dataset('csv', data_files='train/qa_dataset.csv', delimiter='\t', split='train')


# Initialize the T5 tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

# Fine-tune the model on the dataset
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer

training_args = Seq2SeqTrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',  # Change the evaluation strategy to match save strategy
    learning_rate=1e-4,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    num_train_epochs=1,
    weight_decay=0.01,
    push_to_hub=False,
    logging_dir='./logs',
    logging_steps=10,
    save_strategy='epoch',  # Change the save strategy to match evaluation strategy
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    greater_is_better=True,
)


def preprocess_function(examples):
    # Tokenize the inputs and targets
    inputs = [f"question: {example['question']} context: {example['context']}" for example in examples]
    targets = [example['answer'] for example in examples]
    model_inputs = tokenizer(inputs, max_length=512, padding="max_length", truncation=True)

    # Update the model inputs with the targets
    model_inputs["labels"] = tokenizer(targets, max_length=512, padding="max_length", truncation=True)["input_ids"]
    return model_inputs

# trainer = Seq2SeqTrainer(
#     model=model,
#     args=training_args,
#     train_dataset=dataset['train'].map(preprocess_function),
#     eval_dataset=dataset['validation'].map(preprocess_function),
# )

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'].map(preprocess_function),
    eval_dataset=dataset['train'].map(preprocess_function),
)



trainer.train()

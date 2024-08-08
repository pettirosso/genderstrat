import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Define [PAD] token as the padding token
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Load your extracted text from the PDF
with open("extracted_text.txt", "r") as text_file:
    data = text_file.read()

# Tokenize the data
inputs = tokenizer(data, return_tensors='pt', truncation=True, padding=True, max_length=512)

# Create labels by shifting the input_ids by one position
labels = inputs['input_ids'].clone()

# Convert inputs to a dataset
dataset = [{
    "input_ids": input_id,
    "attention_mask": mask,
    "labels": label
} for input_id, mask, label in zip(inputs["input_ids"], inputs["attention_mask"], labels)]

# Load the model and resize the token embeddings
model = AutoModelForCausalLM.from_pretrained("gpt2")
model.resize_token_embeddings(len(tokenizer))

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=1,
    num_train_epochs=1,
    logging_dir='./logs',
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

# Train the model
trainer.train()

# Save the fine-tuned model and tokenizer
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")


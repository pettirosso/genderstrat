# genderstrat# Fine-Tuned GPT-2 Chatbot with Streamlit

This project demonstrates how to fine-tune a GPT-2 model on custom text data and deploy it as a chatbot using Streamlit. The chatbot allows users to interact with the fine-tuned model and generate responses based on the custom data.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Fine-Tuning the Model](#fine-tuning-the-model)
- [Running the Streamlit Chatbot](#running-the-streamlit-chatbot)

## Overview

This project fine-tunes a pre-trained GPT-2 model on a custom dataset and deploys it as an interactive chatbot. The fine-tuned model can generate responses that are relevant to the specific domain of the training data.

## Requirements



- Python 3.8 or higher
- [GitHub Codespaces](https://github.com/features/codespaces) or a local development environment
- Required Python packages:
  - `torch`
  - `datasets`
  - `transformers`
  - `streamlit`

## Setup

Extract text from the pdf via 

extract_text.py

Install dependencies:

Install the required Python packages if you haven't already:

bash
Code kopieren
pip install torch datasets transformers streamlit

## Fine-Tuning the Model


Run the fine-tuning script:

The train_model.py script will fine-tune the GPT-2 model using your custom text data.

python train_model.py

This script will:

Tokenize the input data.
Fine-tune the GPT-2 model.
Save the fine-tuned model in the ./fine_tuned_model directory.
Verify fine-tuning:

After training, ensure the model generates relevant responses by running the test_fine_tuned_model.py script:

python test_fine_tuned_model.py

This script will generate a response based on a sample input to verify that the model has been fine-tuned correctly.

## Running the Streamlit Chatbot

Run the Streamlit app:



streamlit run chatbot_app.py
Interact with the chatbot:

Open the URL provided by Streamlit in your browser.
Enter a question or prompt to interact with the chatbot.
The chatbot will generate a response based on the fine-tuned model.
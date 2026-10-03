# AI Chatbot

## What I Built

I built a basic AI chatbot using Python, Streamlit, and Ollama. The chatbot allows the user to send messages and receive responses from the Gemma 3 AI model.

## Technology Used

- Python 3.12
- Streamlit
- Ollama
- Gemma 3:1b

## How It Works

The user enters a message in the Streamlit interface. The Python application sends the message to the local Ollama server. Ollama sends the conversation to the Gemma 3 model, receives the AI response, and displays it in the chatbot interface.

## How to Run

First, make sure Ollama is running and the Gemma model is installed.

Then run:

```bash
.venv\Scripts\python.exe -m streamlit run app.py
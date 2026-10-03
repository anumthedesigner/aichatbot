import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

with st.sidebar:
    st.header("🤖 AI Chatbot")
    st.write("Powered by Ollama + Gemma 3:1b")
    st.write("Ask anything and get an AI response.")
    st.caption("Model: Gemma 3:1b")
            
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()        
st.title("🤖 AI Chatbot")
st.write("Chat with Gemma 3 using Ollama.")

SYSTEM_PROMPT = """
You are a helpful and friendly AI assistant.
Give clear and simple answers.
For technical questions, explain things step by step.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Type your message...")

if user_message:
    st.chat_message("user").markdown(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = ollama.chat(
                    model="gemma3:1b",
                    messages=messages
                )

                ai_response = response["message"]["content"]
                st.markdown(ai_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })

            except Exception as e:
                st.error(f"Error: {e}")

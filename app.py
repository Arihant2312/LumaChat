from dotenv import load_dotenv
import os
import streamlit as st
from streamlit_chat import message
import google.generativeai as genai

# Load environment and configure API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Choose model
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Get Gemini response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit Page Config
st.set_page_config(page_title="LumaChat.ai", page_icon="🤖", layout="wide")

# Sidebar - Theme Toggle
st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Choose Theme", ["🌞 Light", "🌙 Dark"])

# Custom styling based on theme
if theme == "🌙 Dark":
    st.markdown("""
        <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput, .stTextArea, .stButton, .stSelectbox {
            background-color: #262730 !important;
            color: white !important;
        }
        .chat-bubble-user {
            background-color: #1f77b4;
            color: white;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
        }
        .chat-bubble-bot {
            background-color: #2c2f36;
            color: white;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
        }
        /* Typing animation */
        @keyframes typing {
            0% { content: '•' }
            33% { content: '••' }
            66% { content: '•••' }
            100% { content: '•' }
        }
        .typing-indicator {
            font-size: 24px;
            color: #ffffff;
            animation: typing 1s infinite;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .chat-bubble-user {
            background-color: #cce5ff;
            color: black;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
        }
        .chat-bubble-bot {
            background-color: #f1f1f1;
            color: black;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
        }
        /* Typing animation */
        @keyframes typing {
            0% { content: '•' }
            33% { content: '••' }
            66% { content: '•••' }
            100% { content: '•' }
        }
        .typing-indicator {
            font-size: 24px;
            color: #000000;
            animation: typing 1s infinite;
        }
        </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #0061F2;'>🤖 LumaChat.ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Ask anything, I’m ready to help!</p>", unsafe_allow_html=True)

# Session state to store messages
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input
with st.form("chat_input", clear_on_submit=True):
    user_input = st.text_input("💬 Your message", placeholder="Type your question here...")
    submitted = st.form_submit_button("🚀 Send")

# On submit
if submitted and user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Show typing indicator
    typing_indicator = st.empty()
    typing_indicator.markdown("<div class='typing-indicator'>•</div>", unsafe_allow_html=True)

    # Get Gemini response
    with st.spinner("LumaChat.ai is typing..."):
        bot_response = get_gemini_response(user_input)

    # Remove typing indicator and show the bot's response
    typing_indicator.empty()

    # Append bot response
    st.session_state.chat_history.append({"role": "bot", "content": bot_response})

# Show chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'><b>You:</b><br>{chat['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'><b>LumaChat.ai:</b><br>{chat['content']}</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    "<hr><p style='text-align:center; color:gray;'>Made with ❤️ by Arihant Jain</p>",
    unsafe_allow_html=True
)

import streamlit as st
import google.generativeai as genai

# Configure API Key from Secrets - SECURE
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(page_title="Zaidiii AI", page_icon="🤖", layout="centered")

# Custom Styling (Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #00d4ff; text-align: center; font-weight: 700; }
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Zaidiii AI")
st.caption("⚡ Family Special AI Assistant | Fast, Smart & Secure")

# System Instruction for Zaidiii AI
system_prompt = (
    "You are Zaidiii AI, an intelligent, respectful, and extremely helpful AI assistant "
    "created for Zaid and his family."

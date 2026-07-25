import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Zaidiii AI", page_icon="🤖", layout="centered")
st.title("🤖 Zaidiii AI")
st.caption("Tumhari Family Special AI Assistant | ChatGPT Style")

# API Key connect
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Chat history ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar - Clear Chat ka button
with st.sidebar:
    st.header("Settings")
    if st.button("🗑️ Nayi Chat Shuru Karo"):
        st.session_state.messages = []
        st.rerun()

# Pehle wali chat dikhao
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Naya sawal wala box
if prompt := st.chat_input("Zaidiii se kuch bhi poocho..."):
    
    # User ka message add karo
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ka jawab
    with st.chat_message("assistant"):
        with st.spinner("Zaidiii soch rahi hai..."):
            try:
                model = genai.GenerativeModel('gemini-1.0-pro')
                response = model.generate_content(prompt)
                st.markdown(response.text)
                
                # AI ka jawab bhi save karo
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                st.error(f"Masla aa gaya: {e}")

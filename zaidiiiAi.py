import streamlit as st
import google.generativeai as genai
genai.configure (api_key=AQ.Ab8RN6K9JpG-Kaq9I-PsQ1xCSMy6TMP-qjY2IiJteLdjAgcfVw)
# Page Config
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

# Secure API Key Entry from Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    st.markdown("---")
    st.info("💡 Tip: Aap API Key ko Streamlit Secrets me save kar sakte hain taake bar bar enter na karni pare.")

if api_key:
    genai.configure(api_key=api_key)
    
    # System Instruction for Zaidiii AI
    system_prompt = (
        "You are Zaidiii AI, an intelligent, respectful, and extremely helpful AI assistant "
        "created for Zaid and his family. Answer clearly, accurately, and politely."
    )
    
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_prompt)

    # Chat History Maintain karna
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    if prompt := st.chat_input("Zaidiii AI se kuch bhi poochhein..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                history = [
                    {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                    for m in st.session_state.messages[:-1]
                ]
                chat = model.start_chat(history=history)
                response = chat.send_message(prompt)
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error: {str(e)}")
else:
    st.warning("👈 Pehle Sidebar mein apni Free Google API Key daraj (enter) karein.")

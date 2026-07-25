import streamlit as st
from groq import Groq

st.set_page_config(page_title="Zaidiii AI", page_icon="✨", layout="centered")

# PYARA THEME CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="st"] {
        font-family: 'Poppins', sans-serif;
    }

   .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

   .stChatMessage {
        border-radius: 20px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    div[data-testid="stChatMessageContent-user"] {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
    }

    div[data-testid="stChatMessageContent-assistant"] {
        background: white;
        color: #333;
    }

    h1 {
        text-align: center;
        color: white;
        font-weight: 600;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

   .stChatInput {
        border-radius: 25px!important;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ Zaidiii AI")
st.caption("Tumhari apni personal AI - Fast, Smart, Pyari")

# Groq Client
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("GROQ_API_KEY Secrets me lagao janiii")
    st.stop()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Salam Janiii! 💜 Main Zaidiii hun. Kya poochna hai aaj?"})

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Poocho janiii..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Zaidiii soch rahi hai... ✨"):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

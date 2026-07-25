import streamlit as st
from groq import Groq

st.set_page_config(page_title="Zaidiii AI", page_icon="✨", layout="wide")

# SAFE CLEAN WHITE THEME
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="st"] { font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { background-color: #ffffff; }
   .main { background-color: #f8f9fa; }
    
   .welcome-box {
        background: white;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        margin: 20px auto;
        max-width: 700px;
        border: 1px solid #e9ecef;
    }
    
   .stChatMessage {
        background: white;
        border-radius: 12px;
        padding: 16px;
        margin: 10px 0;
        border: 1px solid #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("✨ Zaidiii AI")
    st.button("💬 AI Chat", use_container_width=True)
    st.button("📝 Write copy", use_container_width=True)
    st.button("🖼️ Image generation", use_container_width=True)
    st.button("💻 Write code", use_container_width=True)
    st.divider()
    st.button("⚙️ Settings", use_container_width=True)

# MAIN WELCOME
st.markdown("""
<div class="welcome-box">
    <h1>Welcome to Zaidiii</h1>
    <p>Get started by asking Zaidiii AI anything.</p>
    <br>
    <p>✍️ Write copy &nbsp;&nbsp;&nbsp; 🖼️ Image generation &nbsp;&nbsp;&nbsp; 💻 Write code</p>
</div>
""", unsafe_allow_html=True)

# Groq Client
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("GROQ_API_KEY Secrets me lagao janiii")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask Zaidiii anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Zaidiii soch rahi hai..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

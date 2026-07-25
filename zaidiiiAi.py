import streamlit as st
from groq import Groq

st.set_page_config(page_title="Zaidiii", page_icon="🤖", layout="centered")

# TUMHARI PIC BACKGROUND WALA CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    html, body, [class*="st"] { font-family: 'Poppins', sans-serif; }

    /* PURA BACKGROUND TUMHARI PIC */
   .stApp {
        background-image: url("https://i.ibb.co/your-bike-pic.jpg"); /* pehle pic upload karo imgbb pe */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* UPAR KAALA TRANSPARENT LAYER */
   .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        z-index: -1;
    }

    /* WELCOME BOX GLASS EFFECT */
  .welcome-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 30px 20px;
        text-align: center;
        margin: 20px 10px;
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
    }
  .welcome-box h1 {
        color: white;
        font-size: 28px;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* CHAT BUBBLES */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.1);
        color: white;
    }

    /* INPUT BOX */
    [data-testid="stChatInput"] {
        background: rgba(255, 255, 255, 0.2)!important;
        backdrop-filter: blur(15px);
        border-radius: 25px!important;
        padding: 10px 20px!important;
        border: 1px solid rgba(255,255,255,0.3);
        color: white!important;
    }
    [data-testid="stChatInput"] input { color: white!important; }
</style>
""", unsafe_allow_html=True)

# Groq Client
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("GROQ_API_KEY Secrets me lagao janiii")
    st.stop()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mode" not in st.session_state:
    st.session_state.mode = "AI Chat"

# WELCOME
st.markdown(f"""
<div class="welcome-box">
    <h1>🤖 Welcome to Zaidiii</h1>
    <p><b>Mode: {st.session_state.mode}</b></p>
    <p>Ask me anything janiii ❤️</p>
</div>
""", unsafe_allow_html=True)

# CHAT HISTORY
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# INPUT
if prompt := st.chat_input(f"Zaidiii se poocho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Soch rahi hun..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

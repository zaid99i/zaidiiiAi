import streamlit as st
from groq import Groq

# APP KA NAAM
MY_NAME = "Zaidiii" # <--- Yahan tumhara naam

st.set_page_config(
    page_title=f"Zaidiii by {MY_NAME}", # Zaidiii by Zaidiii
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# MOBILE AESTHETIC CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="st"] { font-family: 'Poppins', sans-serif; }
 .stApp { background: linear-gradient(180deg, #FF5F6D 0%, #FFC371 100%); }
    #MainMenu, header, footer {visibility: hidden;}
 .welcome-box {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 35px 25px;
        text-align: center;
        margin: 30px 15px;
        border: 1px solid rgba(255,255,255,0.3);
        color: white;
    }
 .welcome-box h1 { color: white; font-size: 32px; font-weight: 700; }
    [data-testid="stChatMessage"] { background: rgba(255, 255, 255, 0.9); border-radius: 20px; padding: 15px 20px; margin: 12px 15px; }
    [data-testid="stChatMessageUser"] { background: #FF5F6D; color: white; }
    [data-testid="stChatInput"] { background: rgba(255, 255, 255, 0.95)!important; border-radius: 30px!important; padding: 15px 25px!important; margin: 0 15px 20px 15px; }
    [data-testid="stSidebar"] { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); }
</style>
""", unsafe_allow_html=True)

# Groq Client
try: client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except: st.error("GROQ_API_KEY Secrets me lagao janiii"); st.stop()

# Session state
if "messages" not in st.session_state: st.session_state.messages = []
if "mode" not in st.session_state: st.session_state.mode = "AI Chat"
def set_mode(mode): st.session_state.mode = mode; st.session_state.messages = []

# SIDEBAR
with st.sidebar:
    st.title(f"🤖 Zaidiii by {MY_NAME}") # Zaidiii by Zaidiii
    st.caption("Your Smart Assistant")
    st.markdown("### **Choose Mode**")
    if st.button("💬 AI Chat", use_container_width=True): set_mode("AI Chat")
    if st.button("📝 Write Copy", use_container_width=True): set_mode("Write Copy")
    if st.button("🖼️ Image Prompt", use_container_width=True): set_mode("Image Prompt")
    if st.button("💻 Write Code", use_container_width=True): set_mode("Write Code")
    if st.button("✍️ Write Story", use_container_width=True): set_mode("Write Story")
    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True): st.session_state.messages = []; st.rerun()

import streamlit as st
from groq import Groq

st.set_page_config(page_title="Zaidiii AI", page_icon="🤖", layout="wide")

# AESTHETIC BACKGROUND + ROBOT THEME
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="st"] { font-family: 'Inter', sans-serif; }
    
    /* AESTHETIC GRADIENT BACKGROUND */
   .main {
        background: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);
    }
    
    /* GLASS SIDEBAR */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.3);
    }
    
    /* GLASS CARD */
  .welcome-box {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        margin: 20px auto;
        max-width: 700px;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
  .stChatMessage {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 16px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
  .stButton>button {
        background: white;
        border-radius: 12px;
        border: 1px solid #ddd;
    }
  .stButton>button:hover {
        background: #f0f0f0;
        transform: scale(1.02);
    }
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

def set_mode(mode, prompt):
    st.session_state.mode = mode
    st.session_state.input_text = prompt
    st.rerun()

# SIDEBAR WITH ROBOT 🤖
with st.sidebar:
    st.title("🤖 Zaidiii AI")
    st.caption("Your Smart Assistant")
    
    if st.button("💬 AI Chat", use_container_width=True):
        set_mode("AI Chat", "")
    if st.button("📝 Write Copy", use_container_width=True):
        set_mode("Write Copy", "Write marketing copy for: ")
    if st.button("🖼️ Image Prompt", use_container_width=True):
        set_mode("Image Prompt", "Describe an image of: ")
    if st.button("💻 Write Code", use_container_width=True):
        set_mode("Write Code", "Write Python code for: ")
    if st.button("📊 Data Analysis", use_container_width=True):
        set_mode("Data Analysis", "Analyze this data: ")
    if st.button("✍️ Write Story", use_container_width=True):
        set_mode("Write Story", "Write a story about: ")
    
    st.divider()
    if st.button("⚙️ Settings", use_container_width=True):
        set_mode("

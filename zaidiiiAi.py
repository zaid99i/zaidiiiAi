import streamlit as st
from groq import Groq

st.set_page_config(page_title="Zaidiii AI", page_icon="✨", layout="wide")

# SCRIPT WALA CLEAN WHITE THEME
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="st"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e9ecef;
    }
    
    /* Main */
   .main { background-color: #f8f9fa; }
    
    /* Center Card */
   .center-card {
        background: white;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        margin: 20px auto;
        max-width: 700px;
    }
    
    /* Quick Action Buttons */
   .quick-btn {
        background: #f1f3f5;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        cursor: pointer;
        transition: 0.2s;
    }
   .quick-btn:hover { background: #e9ecef; }
    
   .stChatMessage {
        background: white;
        border-radius: 12px;
        padding: 16px;
        margin: 10px 0;
        border: 1px solid #e9ecef;
    }
    
  .stChatInput {
        border-radius: 12px!important;
        background: white!important;
        border: 1px solid #dee2e6!important;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("✨ Zaidiii AI")
    st.button("💬 AI Chat", use_container_width=True)
    st.button("📝 Write copy", use_container_width=True)
    st.button("🖼️ Image generation", use_container_width=True)
    st.button("🎥 Create avatar", use_container_width=True)
    st.button("💻 Write code", use_container_width=True)
    st.divider()
    st.button("⚙️ Settings", use_container_width=True)

# MAIN
st.markdown("""<div class="center-card">
    <h1>Welcome to Zaidiii</h1>
    <p>Get started by Zaidiii AI. Ask anything and I'll help you.</p>
    
    <div style="display: flex; gap: 10px; margin-top: 20px; justify-content: center;">
        <div class="quick-btn">✍️<br>Write copy</div>
        <div class="quick-btn">🖼️<br>Image generation</div>
        <div class="quick-btn">📊<br>Create avatar</div>
        <div class="quick-btn">💻<br>Write code</div>
    </div>
</div>""", unsafe_allow_html=True)

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

if prompt := st.chat_input("Summarize this article..."):
    st.session_state.messages.append

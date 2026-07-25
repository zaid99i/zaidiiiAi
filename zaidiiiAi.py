import streamlit as st
from groq import Groq

st.set_page_config(page_title="Zaidiii AI", page_icon="🤖", layout="wide")

# AESTHETIC BACKGROUND
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="st"] { font-family: 'Inter', sans-serif; }
    
 .main {
        background: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);
    }
    
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
    }
    
.welcome-box {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin: 20px auto;
        max-width: 700px;
        border: 1px solid rgba(255,255,255,0.3);
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
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

def set_mode(mode, prompt):
    st.session_state.mode = mode
    st.session_state.input_text = prompt

# SIDEBAR WITH ROBOT
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
        set_mode("Settings", "")

# MAIN WELCOME
st.markdown(f"""
<div class="welcome-box">
    <h1>🤖 Welcome to Zaidiii</h1>
    <p><b>Active Mode: {st.session_state.mode}</b></p>
    <p>Ask me anything and I'll help you!</p>
</div>
""", unsafe_allow_html=True)

# CHAT HISTORY
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# INPUT
if prompt := st.chat_input(f"Ask Zaidiii in {st.session_state.mode} mode..."):
    full_prompt = prompt
    
    if st.session_state.mode == "Write Copy":
        full_prompt = "Act as a professional copywriter. " + prompt
    elif st.session_state.mode == "Write Code":
        full_prompt = "Act as an expert programmer. Give clean code with comments. " + prompt
    elif st.session_state.mode == "Image Prompt":
        full_prompt = "Describe this image in detail for AI image generation: " + prompt
    elif st.session_state.mode == "Data Analysis":
        full_prompt = "Act as a data analyst. " + prompt
    elif st.session_state.mode == "Write Story":
        full_prompt = "Act as a creative storyteller. " + prompt
    
    st.session_state.messages.append({"role": "user", "content": full_prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Zaidiii soch rahi hai..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
